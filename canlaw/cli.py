import argparse
import logging

from .embeddings import embed_all_court_cases
from .db import repair_case_metadata
from .hf_loader import ingest_courts_to_db


def main():
    logging.basicConfig(level=logging.INFO, format="%(levelname)s %(message)s")
    parser = argparse.ArgumentParser()
    parser.add_argument("command", choices=["ingest_courts", "embed_courts", "repair_staging"])
    parser.add_argument(
        "--courts",
        nargs="*",
        default=None,
        help="Optional court codes to ingest or embed: FC RPD FCA SCC",
    )
    parser.add_argument("--batch-size", type=int, default=16, help="Embedding batch size")
    args = parser.parse_args()

    if args.command == "ingest_courts":
        counts = ingest_courts_to_db(courts=args.courts)
        for court, count in counts.items():
            print(f"{court}: {count} records processed")
    elif args.command == "embed_courts":
        count = embed_all_court_cases(courts=args.courts, batch_size=args.batch_size)
        print(f"embedded: {count}")
    elif args.command == "repair_staging":
        count = repair_case_metadata(batch_size=args.batch_size)
        print(f"repaired: {count}")


if __name__ == "__main__":
    main()
