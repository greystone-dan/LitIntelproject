import os
from collections.abc import Generator
from datetime import date as date_type, datetime
from pathlib import Path

from dotenv import load_dotenv
from pgvector.sqlalchemy import Vector
from sqlalchemy import (
	Date,
	DateTime,
	Float,
	Integer,
	JSON,
	ForeignKey,
	String,
	Text,
	UniqueConstraint,
	URL,
	create_engine,
	func,
	text,
)
from sqlalchemy.orm import DeclarativeBase, Mapped, Session, mapped_column, sessionmaker
from sqlalchemy.orm import relationship

PROJECT_ROOT = Path(__file__).resolve().parent.parent
# Prefer project-local settings over inherited shell variables.
load_dotenv(PROJECT_ROOT / ".env", override=True)
load_dotenv(Path(__file__).resolve().parent / ".env", override=True)

def _database_url() -> str | URL:
	postgres_user = os.getenv("POSTGRES_USER")
	postgres_password = os.getenv("POSTGRES_PASSWORD")
	postgres_host = os.getenv("POSTGRES_HOST")
	postgres_port = os.getenv("POSTGRES_PORT")
	postgres_db = os.getenv("POSTGRES_DB")

	# Prefer explicit POSTGRES_* settings when present so stale inherited
	# DATABASE_URL values do not override project-local database settings.
	if any(
		[
			postgres_user,
			postgres_password,
			postgres_host,
			postgres_port,
			postgres_db,
		]
	):
		return URL.create(
			drivername="postgresql+psycopg2",
			username=postgres_user or "postgres",
			password=postgres_password or "postgres",
			host=postgres_host or "localhost",
			port=int(postgres_port or "5432"),
			database=postgres_db or "caselibrary",
		)

	configured_url = (os.getenv("DATABASE_URL") or "").strip()
	if configured_url:
		return configured_url

	return URL.create(
		drivername="postgresql+psycopg2",
		username=os.getenv("POSTGRES_USER", "postgres"),
		password=os.getenv("POSTGRES_PASSWORD", "postgres"),
		host=os.getenv("POSTGRES_HOST", "localhost"),
		port=int(os.getenv("POSTGRES_PORT", "5432")),
		database=os.getenv("POSTGRES_DB", "caselibrary"),
	)


DATABASE_URL = _database_url()

engine = create_engine(DATABASE_URL, pool_pre_ping=True)
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)


class Base(DeclarativeBase):
	pass


class Case(Base):
	__tablename__ = "cases"

	id: Mapped[int] = mapped_column(Integer, primary_key=True)
	title: Mapped[str] = mapped_column(String(255), nullable=False, index=True)
	court: Mapped[str] = mapped_column(String(255), nullable=False, index=True)
	jurisdiction: Mapped[str | None] = mapped_column(String(100), nullable=True, index=True)
	date: Mapped[date_type] = mapped_column(Date, nullable=False, index=True)
	citation: Mapped[str | None] = mapped_column(String(255), nullable=True, index=True)
	docket_number: Mapped[str | None] = mapped_column(String(255), nullable=True, index=True)
	secondary_citation: Mapped[str | None] = mapped_column(String(255), nullable=True)
	summary: Mapped[str | None] = mapped_column(Text, nullable=True)
	full_text: Mapped[str | None] = mapped_column(Text, nullable=True)
	source_html: Mapped[str | None] = mapped_column(Text, nullable=True)
	issues: Mapped[list[str] | None] = mapped_column(JSON, nullable=True)
	metadata_json: Mapped[dict[str, object] | None] = mapped_column(JSON, nullable=True)
	source_url: Mapped[str | None] = mapped_column(String(2048), nullable=True)
	source_name: Mapped[str | None] = mapped_column(String(255), nullable=True)
	source_id: Mapped[str | None] = mapped_column(String(255), nullable=True, index=True)
	source_type: Mapped[str | None] = mapped_column(String(100), nullable=True)
	dataset_version: Mapped[str | None] = mapped_column(String(100), nullable=True)
	upstream_license: Mapped[str | None] = mapped_column(Text, nullable=True)
	scraped_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), nullable=True)
	language: Mapped[str | None] = mapped_column(String(10), nullable=True)
	full_text_hash: Mapped[str | None] = mapped_column(String(64), nullable=True, index=True)
	processing_status: Mapped[str] = mapped_column(
		String(30), nullable=False, server_default="raw", index=True
	)
	cases_cited: Mapped[list[str] | None] = mapped_column(JSON, nullable=True)
	cases_citing: Mapped[list[str] | None] = mapped_column(JSON, nullable=True)
	citing_cases_count: Mapped[int | None] = mapped_column(Integer, nullable=True)
	embedding: Mapped[list[float] | None] = mapped_column(Vector(1536), nullable=True)
	created_at: Mapped[datetime] = mapped_column(
		DateTime(timezone=True), server_default=func.now(), nullable=False
	)

	chunks = relationship("CaseChunk", back_populates="case")
	sources = relationship("CaseSource", back_populates="case", cascade="all, delete-orphan")
	outgoing_citations = relationship(
		"Citation",
		foreign_keys="Citation.source_case_id",
		back_populates="source_case",
	)
	incoming_citations = relationship(
		"Citation",
		foreign_keys="Citation.target_case_id",
		back_populates="target_case",
	)
	metrics = relationship("CitationMetrics", uselist=False, back_populates="case")
	statute_references = relationship(
		"StatuteReference",
		foreign_keys="StatuteReference.source_case_id",
		back_populates="source_case",
		cascade="all, delete-orphan",
	)
	judge_links = relationship("CaseJudgeProfile", back_populates="case", cascade="all, delete-orphan")
	tags = relationship("CaseTag", back_populates="case", cascade="all, delete-orphan")
	tagging_statuses = relationship(
		"CaseTaggingStatus", back_populates="case", cascade="all, delete-orphan"
	)


class JudgeProfile(Base):
	__tablename__ = "judge_profiles"

	id: Mapped[int] = mapped_column(Integer, primary_key=True)
	slug: Mapped[str] = mapped_column(String(255), nullable=False, unique=True, index=True)
	display_name: Mapped[str] = mapped_column(String(255), nullable=False)
	normalized_name: Mapped[str] = mapped_column(String(255), nullable=False, unique=True, index=True)
	primary_court: Mapped[str | None] = mapped_column(String(255), nullable=True, index=True)
	aliases: Mapped[list[str] | None] = mapped_column(JSON, nullable=True)
	created_at: Mapped[datetime] = mapped_column(
		DateTime(timezone=True), server_default=func.now(), nullable=False
	)
	updated_at: Mapped[datetime] = mapped_column(
		DateTime(timezone=True), server_default=func.now(), nullable=False, onupdate=func.now()
	)

	case_links = relationship("CaseJudgeProfile", back_populates="judge_profile", cascade="all, delete-orphan")


class CaseJudgeProfile(Base):
	__tablename__ = "case_judge_profiles"
	__table_args__ = (UniqueConstraint("case_id", "judge_profile_id", name="uq_case_judge_profile"),)

	id: Mapped[int] = mapped_column(Integer, primary_key=True)
	case_id: Mapped[int] = mapped_column(
		Integer, ForeignKey("cases.id", ondelete="CASCADE"), nullable=False, index=True
	)
	judge_profile_id: Mapped[int] = mapped_column(
		Integer, ForeignKey("judge_profiles.id", ondelete="CASCADE"), nullable=False, index=True
	)
	raw_name: Mapped[str] = mapped_column(String(255), nullable=False)
	created_at: Mapped[datetime] = mapped_column(
		DateTime(timezone=True), server_default=func.now(), nullable=False
	)

	case = relationship("Case", back_populates="judge_links")
	judge_profile = relationship("JudgeProfile", back_populates="case_links")


class CaseSource(Base):
	__tablename__ = "case_sources"

	id: Mapped[int] = mapped_column(Integer, primary_key=True)
	case_id: Mapped[int] = mapped_column(
		Integer, ForeignKey("cases.id", ondelete="CASCADE"), nullable=False, index=True
	)
	source_type: Mapped[str] = mapped_column(String(100), nullable=False, index=True)
	source_name: Mapped[str | None] = mapped_column(String(255), nullable=True)
	source_id: Mapped[str | None] = mapped_column(String(255), nullable=True)
	source_url: Mapped[str | None] = mapped_column(String(2048), nullable=True)
	dataset_version: Mapped[str | None] = mapped_column(String(100), nullable=True)
	upstream_license: Mapped[str | None] = mapped_column(Text, nullable=True)
	scraped_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), nullable=True)
	is_primary: Mapped[bool] = mapped_column(default=False, nullable=False)
	raw_hash: Mapped[str | None] = mapped_column(String(64), nullable=True, index=True)
	metadata_json: Mapped[dict[str, object] | None] = mapped_column(JSON, nullable=True)
	created_at: Mapped[datetime] = mapped_column(
		DateTime(timezone=True), server_default=func.now(), nullable=False
	)
	updated_at: Mapped[datetime] = mapped_column(
		DateTime(timezone=True), server_default=func.now(), nullable=False
	)

	case = relationship("Case", back_populates="sources")


class CaseChunk(Base):
	__tablename__ = "case_chunks"

	id: Mapped[int] = mapped_column(Integer, primary_key=True)
	case_id: Mapped[int] = mapped_column(
		Integer, ForeignKey("cases.id", ondelete="CASCADE"), nullable=False, index=True
	)
	chunk_set: Mapped[str] = mapped_column(String(50), nullable=False, index=True, default="legacy")
	chunk_index: Mapped[int] = mapped_column(Integer, nullable=False)
	chunk_label: Mapped[str | None] = mapped_column(String(255), nullable=True)
	paragraph_start: Mapped[int | None] = mapped_column(Integer, nullable=True)
	paragraph_end: Mapped[int | None] = mapped_column(Integer, nullable=True)
	text: Mapped[str] = mapped_column(Text, nullable=False)
	text_hash: Mapped[str] = mapped_column(String(64), nullable=False, index=True)
	token_estimate: Mapped[int] = mapped_column(Integer, nullable=False)
	embedding: Mapped[list[float] | None] = mapped_column(Vector(1536), nullable=True)
	embedding_model: Mapped[str | None] = mapped_column(String(100), nullable=True)
	created_at: Mapped[datetime] = mapped_column(
		DateTime(timezone=True), server_default=func.now(), nullable=False
	)

	case = relationship("Case", back_populates="chunks")
	citations = relationship("Citation", back_populates="chunk")
	statute_references = relationship("StatuteReference", back_populates="chunk")
	local_embeddings = relationship(
		"CaseChunkEmbedding",
		back_populates="chunk",
		cascade="all, delete-orphan",
	)


class CaseChunkEmbedding(Base):
	__tablename__ = "case_chunk_embeddings"
	__table_args__ = (
		UniqueConstraint("chunk_id", "model_name", name="uq_chunk_embedding_model"),
	)

	id: Mapped[int] = mapped_column(Integer, primary_key=True)
	chunk_id: Mapped[int] = mapped_column(
		Integer, ForeignKey("case_chunks.id", ondelete="CASCADE"), nullable=False, index=True
	)
	model_name: Mapped[str] = mapped_column(String(255), nullable=False, index=True)
	dimensions: Mapped[int] = mapped_column(Integer, nullable=False)
	embedding: Mapped[list[float]] = mapped_column(Vector(1024), nullable=False)
	created_at: Mapped[datetime] = mapped_column(
		DateTime(timezone=True), server_default=func.now(), nullable=False
	)

	chunk = relationship("CaseChunk", back_populates="local_embeddings")


class CaseTag(Base):
	__tablename__ = "case_tags"
	__table_args__ = (
		UniqueConstraint(
			"case_id",
			"category",
			"value",
			"taxonomy_version",
			name="uq_case_tag_taxonomy",
		),
	)

	id: Mapped[int] = mapped_column(Integer, primary_key=True)
	case_id: Mapped[int] = mapped_column(
		Integer, ForeignKey("cases.id", ondelete="CASCADE"), nullable=False, index=True
	)
	category: Mapped[str] = mapped_column(String(100), nullable=False, index=True)
	value: Mapped[str] = mapped_column(String(255), nullable=False, index=True)
	score: Mapped[float] = mapped_column(Float, nullable=False)
	evidence: Mapped[str] = mapped_column(Text, nullable=False)
	source: Mapped[str] = mapped_column(String(50), nullable=False, index=True)
	taxonomy_version: Mapped[str] = mapped_column(String(100), nullable=False, index=True)
	created_at: Mapped[datetime] = mapped_column(
		DateTime(timezone=True), server_default=func.now(), nullable=False
	)

	case = relationship("Case", back_populates="tags")


class CaseTaggingStatus(Base):
	__tablename__ = "case_tagging_status"
	__table_args__ = (
		UniqueConstraint("case_id", "taxonomy_version", name="uq_case_tagging_status"),
	)

	id: Mapped[int] = mapped_column(Integer, primary_key=True)
	case_id: Mapped[int] = mapped_column(
		Integer, ForeignKey("cases.id", ondelete="CASCADE"), nullable=False, index=True
	)
	taxonomy_version: Mapped[str] = mapped_column(String(100), nullable=False, index=True)
	tags_count: Mapped[int] = mapped_column(Integer, nullable=False)
	tagged_at: Mapped[datetime] = mapped_column(
		DateTime(timezone=True), server_default=func.now(), nullable=False
	)

	case = relationship("Case", back_populates="tagging_statuses")


class IngestionRun(Base):
	__tablename__ = "ingestion_runs"

	id: Mapped[int] = mapped_column(Integer, primary_key=True)
	source_type: Mapped[str] = mapped_column(String(100), nullable=False, index=True)
	source_name: Mapped[str | None] = mapped_column(String(255), nullable=True)
	run_type: Mapped[str] = mapped_column(String(50), nullable=False, index=True)
	status: Mapped[str] = mapped_column(String(30), nullable=False, server_default="started", index=True)
	started_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now(), nullable=False)
	finished_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), nullable=True)
	records_seen: Mapped[int | None] = mapped_column(Integer, nullable=True)
	records_ingested: Mapped[int | None] = mapped_column(Integer, nullable=True)
	records_updated: Mapped[int | None] = mapped_column(Integer, nullable=True)
	records_failed: Mapped[int | None] = mapped_column(Integer, nullable=True)
	metadata_json: Mapped[dict[str, object] | None] = mapped_column(JSON, nullable=True)


class Citation(Base):
	__tablename__ = "citations"

	id: Mapped[int] = mapped_column(Integer, primary_key=True)
	source_case_id: Mapped[int] = mapped_column(
		Integer, ForeignKey("cases.id", ondelete="CASCADE"), nullable=False, index=True
	)
	target_case_id: Mapped[int | None] = mapped_column(
		Integer, ForeignKey("cases.id", ondelete="CASCADE"), nullable=True, index=True
	)
	citation_kind: Mapped[str] = mapped_column(String(20), nullable=False, server_default="unknown", index=True)
	citation_text: Mapped[str | None] = mapped_column(Text, nullable=True)
	normalized_citation: Mapped[str | None] = mapped_column(Text, nullable=True, index=True)
	provenance: Mapped[str] = mapped_column(String(20), nullable=False, server_default="local", index=True)
	chunk_id: Mapped[int | None] = mapped_column(
		Integer, ForeignKey("case_chunks.id", ondelete="SET NULL"), nullable=True, index=True
	)
	offset_start: Mapped[int | None] = mapped_column(Integer, nullable=True)
	offset_end: Mapped[int | None] = mapped_column(Integer, nullable=True)
	unresolved: Mapped[bool] = mapped_column(default=False, nullable=False)

	source_case = relationship("Case", foreign_keys=[source_case_id], back_populates="outgoing_citations")
	target_case = relationship("Case", foreign_keys=[target_case_id], back_populates="incoming_citations")
	chunk = relationship("CaseChunk", back_populates="citations")


class CitationMetrics(Base):
	__tablename__ = "citation_metrics"

	case_id: Mapped[int] = mapped_column(
		Integer, ForeignKey("cases.id", ondelete="CASCADE"), primary_key=True
	)
	in_degree: Mapped[int | None] = mapped_column(Integer, nullable=True)
	out_degree: Mapped[int | None] = mapped_column(Integer, nullable=True)
	pagerank: Mapped[float | None] = mapped_column(Float, nullable=True)

	case = relationship("Case", back_populates="metrics")


class StatuteReference(Base):
	__tablename__ = "statute_references"

	id: Mapped[int] = mapped_column(Integer, primary_key=True)
	source_case_id: Mapped[int] = mapped_column(
		Integer, ForeignKey("cases.id", ondelete="CASCADE"), nullable=False, index=True
	)
	chunk_id: Mapped[int | None] = mapped_column(
		Integer, ForeignKey("case_chunks.id", ondelete="SET NULL"), nullable=True, index=True
	)
	offset_start: Mapped[int | None] = mapped_column(Integer, nullable=True)
	offset_end: Mapped[int | None] = mapped_column(Integer, nullable=True)
	reference_text: Mapped[str | None] = mapped_column(Text, nullable=True)
	normalized_reference: Mapped[str | None] = mapped_column(Text, nullable=True, index=True)
	reference_kind: Mapped[str] = mapped_column(String(20), nullable=False, index=True)

	source_case = relationship("Case", back_populates="statute_references")
	chunk = relationship("CaseChunk", back_populates="statute_references")


class A2AJCase(Base):
	__tablename__ = "a2aj_cases"

	id: Mapped[int] = mapped_column(Integer, primary_key=True)
	a2aj_case_id: Mapped[str] = mapped_column(Text, unique=True, index=True, nullable=False)
	neutral_citation: Mapped[str | None] = mapped_column(Text, nullable=True, index=True)
	court: Mapped[str | None] = mapped_column(Text, nullable=True)
	decision_date: Mapped[date_type | None] = mapped_column(Date, nullable=True, index=True)
	cases_cited: Mapped[list[str] | None] = mapped_column(JSON, nullable=True)
	cases_citing: Mapped[list[str] | None] = mapped_column(JSON, nullable=True)
	citing_cases_count: Mapped[int | None] = mapped_column(Integer, nullable=True)

	case_map = relationship("A2AJCaseMap", uselist=False, back_populates="a2aj_case")


class A2AJCitationEdge(Base):
	__tablename__ = "a2aj_citation_edges"

	id: Mapped[int] = mapped_column(Integer, primary_key=True)
	source_a2aj_case_id: Mapped[str] = mapped_column(Text, nullable=False, index=True)
	target_a2aj_case_id: Mapped[str | None] = mapped_column(Text, nullable=True, index=True)
	normalized_citation: Mapped[str | None] = mapped_column(Text, nullable=True, index=True)


class A2AJCaseMap(Base):
	__tablename__ = "a2aj_case_map"

	a2aj_case_id: Mapped[str] = mapped_column(
		Text, ForeignKey("a2aj_cases.a2aj_case_id", ondelete="CASCADE"), primary_key=True
	)
	local_case_id: Mapped[int] = mapped_column(
		Integer, ForeignKey("cases.id", ondelete="CASCADE"), nullable=False, index=True
	)

	a2aj_case = relationship("A2AJCase", back_populates="case_map")
	local_case = relationship("Case")


class FCProceduralHistory(Base):
	__tablename__ = "fc_procedural_history"

	id: Mapped[int] = mapped_column(Integer, primary_key=True)
	imm_number: Mapped[str] = mapped_column(String(50), nullable=False, unique=True, index=True)
	style_of_cause: Mapped[str | None] = mapped_column(Text, nullable=True)
	judge: Mapped[str | None] = mapped_column(String(120), nullable=True)
	leave_decision: Mapped[str | None] = mapped_column(String(30), nullable=True, index=True)
	leave_date: Mapped[date_type | None] = mapped_column(Date, nullable=True)
	jr_decision: Mapped[str | None] = mapped_column(String(40), nullable=True)
	jr_decision_date: Mapped[date_type | None] = mapped_column(Date, nullable=True)
	case_status: Mapped[str | None] = mapped_column(String(40), nullable=True, index=True)
	latest_activity_date: Mapped[date_type | None] = mapped_column(Date, nullable=True)
	full_activity_text: Mapped[str | None] = mapped_column(Text, nullable=True)
	entries_json: Mapped[list | None] = mapped_column(JSON, nullable=True)
	conflict_flag: Mapped[bool] = mapped_column(default=False)
	fetched_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), nullable=True)


class FCActivityCase(Base):
	__tablename__ = "fc_activity_cases"
	__table_args__ = (
		UniqueConstraint("citation", name="uq_fc_activity_case_citation"),
		UniqueConstraint("source_key", name="uq_fc_activity_case_source_key"),
	)

	id: Mapped[int] = mapped_column(Integer, primary_key=True)
	source_key: Mapped[str] = mapped_column(String(255), nullable=False, unique=True, index=True)
	citation: Mapped[str | None] = mapped_column(String(255), nullable=True, index=True)
	year: Mapped[int | None] = mapped_column(Integer, nullable=True, index=True)
	case_name: Mapped[str | None] = mapped_column(Text, nullable=True)
	date_filed: Mapped[date_type | None] = mapped_column(Date, nullable=True, index=True)
	city_filed: Mapped[str | None] = mapped_column(String(255), nullable=True)
	nature: Mapped[str | None] = mapped_column(Text, nullable=True)
	case_class: Mapped[str | None] = mapped_column(String(120), nullable=True)
	track: Mapped[str | None] = mapped_column(String(120), nullable=True)
	source_url: Mapped[str | None] = mapped_column(String(2048), nullable=True)
	scraped_timestamp: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), nullable=True)
	raw_payload: Mapped[dict[str, object] | None] = mapped_column(JSON, nullable=True)
	created_at: Mapped[datetime] = mapped_column(
		DateTime(timezone=True), server_default=func.now(), nullable=False
	)
	updated_at: Mapped[datetime] = mapped_column(
		DateTime(timezone=True), server_default=func.now(), nullable=False, onupdate=func.now()
	)

	documents = relationship("FCActivityDocument", back_populates="case", cascade="all, delete-orphan")
	classification = relationship("FCActivityClassification", back_populates="source_case", uselist=False, cascade="all, delete-orphan")


class FCActivityClassification(Base):
	__tablename__ = "fc_activity_classifications"

	id: Mapped[int] = mapped_column(Integer, primary_key=True)
	source_case_id: Mapped[int] = mapped_column(Integer, ForeignKey("fc_activity_cases.id", ondelete="CASCADE"), nullable=False, unique=True, index=True)
	source_key: Mapped[str] = mapped_column(String(255), nullable=False, index=True)
	imm_number: Mapped[str | None] = mapped_column(String(255), nullable=True, index=True)
	year: Mapped[int | None] = mapped_column(Integer, nullable=True, index=True)
	case_name: Mapped[str | None] = mapped_column(Text, nullable=True)
	date_filed: Mapped[date_type | None] = mapped_column(Date, nullable=True, index=True)
	city_filed: Mapped[str | None] = mapped_column(String(255), nullable=True)
	nature: Mapped[str | None] = mapped_column(Text, nullable=True)
	case_class: Mapped[str | None] = mapped_column(String(120), nullable=True)
	track: Mapped[str | None] = mapped_column(String(120), nullable=True)
	source_url: Mapped[str | None] = mapped_column(String(2048), nullable=True)
	scraped_timestamp: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), nullable=True)
	classification_json: Mapped[dict[str, object]] = mapped_column(JSON, nullable=False)
	classifier_version: Mapped[str] = mapped_column(String(80), nullable=False)
	classified_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now(), nullable=False)
	updated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now(), nullable=False, onupdate=func.now())

	source_case = relationship("FCActivityCase", back_populates="classification")


class FCActivityDocument(Base):
	__tablename__ = "fc_activity_documents"
	__table_args__ = (
		UniqueConstraint("case_id", "re_no", "docno", name="uq_fc_activity_document_identity"),
		UniqueConstraint("case_id", "re_no", "docno", "entry_hash", name="uq_fc_activity_document_fallback"),
	)

	id: Mapped[int] = mapped_column(Integer, primary_key=True)
	case_id: Mapped[int] = mapped_column(
		Integer, ForeignKey("fc_activity_cases.id", ondelete="CASCADE"), nullable=False, index=True
	)
	re_no: Mapped[str | None] = mapped_column(String(50), nullable=True, index=True)
	docno: Mapped[str | None] = mapped_column(String(120), nullable=True, index=True)
	doc_dt: Mapped[date_type | None] = mapped_column(Date, nullable=True, index=True)
	recorded_entry: Mapped[str | None] = mapped_column(Text, nullable=True)
	entry_hash: Mapped[str | None] = mapped_column(String(64), nullable=True, index=True)
	raw_document: Mapped[dict[str, object] | None] = mapped_column(JSON, nullable=True)
	created_at: Mapped[datetime] = mapped_column(
		DateTime(timezone=True), server_default=func.now(), nullable=False
	)

	case = relationship("FCActivityCase", back_populates="documents")


def get_db() -> Generator[Session, None, None]:
	db = SessionLocal()
	try:
		yield db
	finally:
		db.close()


def init_db() -> None:
	from . import models

	with engine.begin() as connection:
		connection.execute(text("CREATE EXTENSION IF NOT EXISTS vector"))
	Base.metadata.create_all(bind=engine)
