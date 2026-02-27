from __future__ import annotations

import argparse
import json
from pathlib import Path

from .scanner import LANGUAGE_CHOICES, scan_project


SAMPLE_MAP = {
    "python": "samples/python",
    "javascript": "samples/javascript",
    "c_family": "samples/c_family",
}


def main() -> None:
    parser = argparse.ArgumentParser(prog="zeroday")
    sub = parser.add_subparsers(dest="command", required=True)

    scan_parser = sub.add_parser("scan", help="Scan a project directory")
    scan_parser.add_argument("target", type=Path, nargs="?", default=Path("."))
    scan_parser.add_argument("--output", "-o", type=Path)
    scan_parser.add_argument("--language", choices=sorted(LANGUAGE_CHOICES))
    scan_parser.add_argument(
        "--use-sample",
        action="store_true",
        help="Scan built-in sample files for the selected language.",
    )

    args = parser.parse_args()

    if args.command == "scan":
        target = args.target.resolve()
        if args.use_sample:
            if not args.language:
                raise SystemExit("--use-sample requires --language")
            repo_root = Path(__file__).resolve().parents[2]
            target = repo_root / SAMPLE_MAP[args.language]

        if not target.exists() or not target.is_dir():
            raise SystemExit(f"Target path must exist and be a directory: {target}")

        result = scan_project(target, language=args.language)
        payload = json.dumps(result, indent=2)
        if args.output:
            args.output.write_text(payload, encoding="utf-8")
            print(f"Wrote scan output to {args.output}")
        else:
            print(payload)


if __name__ == "__main__":
    main()
