from __future__ import annotations

import argparse
import json
from pathlib import Path

from .scanner import scan_project


def main() -> None:
    parser = argparse.ArgumentParser(prog="zeroday")
    sub = parser.add_subparsers(dest="command", required=True)

    scan_parser = sub.add_parser("scan", help="Scan a project directory")
    scan_parser.add_argument("target", type=Path)
    scan_parser.add_argument("--output", "-o", type=Path)

    args = parser.parse_args()

    if args.command == "scan":
        result = scan_project(args.target.resolve())
        payload = json.dumps(result, indent=2)
        if args.output:
            args.output.write_text(payload, encoding="utf-8")
            print(f"Wrote scan output to {args.output}")
        else:
            print(payload)


if __name__ == "__main__":
    main()
