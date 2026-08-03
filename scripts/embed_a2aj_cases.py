"""Chunk and embed raw A2AJ cases. This is the first paid API operation."""
import os
import sys
from hashlib import sha256
from pathlib import Path

from openai import OpenAI
from sqlalchemy import delete, select

# Allow running this file directly via "python scripts/...py".
PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
	sys.path.insert(0, str(PROJECT_ROOT))

from backend.database import Case, CaseChunk, SessionLocal

MODEL = os.getenv("OPENAI_EMBEDDING_MODEL", "text-embedding-3-small")
CHUNK_CHARS = 6000
OVERLAP_CHARS = 600
PRICE_PER_MILLION_TOKENS = 0.02


def chunks(text: str) -> list[str]:
	result = []
	start = 0
	while start < len(text):
		end = min(start + CHUNK_CHARS, len(text))
		result.append(text[start:end])
		if end == len(text):
			break
		start = end - OVERLAP_CHARS
	return result


def main() -> None:
	limit = int(os.getenv("A2AJ_EMBED_LIMIT", "25"))
	source_type = os.getenv("A2AJ_EMBED_SOURCE_TYPE", "a2aj_curated")
	client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])

	with SessionLocal() as session:
		cases = list(session.scalars(
			select(Case).where(Case.source_type == source_type, Case.processing_status == "raw").order_by(Case.id).limit(limit)
		))
		all_chunks = []
		for case in cases:
			case_chunks = chunks(case.full_text or "")
			all_chunks.extend((case, index, text) for index, text in enumerate(case_chunks))

		total_tokens = sum(max(1, len(text) // 4) for _, _, text in all_chunks)
		print(f"cases={len(cases)} chunks={len(all_chunks)} estimated_tokens={total_tokens}")
		print(f"estimated_embedding_cost=${total_tokens / 1_000_000 * PRICE_PER_MILLION_TOKENS:.4f}")
		responses = []
		for start in range(0, len(all_chunks), 100):
			batch = all_chunks[start:start + 100]
			response = client.embeddings.create(
				model=MODEL,
				input=[text for _, _, text in batch],
			)
			responses.extend(response.data)

		by_case = {}
		for (case, index, text), item in zip(all_chunks, responses):
			embedding = item.embedding
			session.add(CaseChunk(
				case_id=case.id,
				chunk_index=index,
				text=text,
				text_hash=sha256(text.encode("utf-8")).hexdigest(),
				token_estimate=max(1, len(text) // 4),
				embedding=embedding,
				embedding_model=MODEL,
			))
			by_case.setdefault(case.id, []).append(embedding)

		for case in cases:
			vectors = by_case[case.id]
			case.embedding = [sum(vector[index] for vector in vectors) / len(vectors) for index in range(len(vectors[0]))]
			case.processing_status = "embedded"
			case.metadata_json = {**(case.metadata_json or {}), "embedding_model": MODEL, "embedding_chunk_count": len(vectors)}
		session.commit()
		print(f"embedded_cases={len(cases)}")


if __name__ == "__main__":
	main()