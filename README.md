# ZeroDay Scaffold

Initial executable scaffold for a proof-first vulnerability discovery platform.

## Quick start

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e . pytest
pytest
zeroday scan . --output findings.json
```

## Fast language-only testing (no project download each time)

Use built-in samples to quickly test one language:

```bash
PYTHONPATH=src python -m zeroday.cli scan --language python --use-sample
PYTHONPATH=src python -m zeroday.cli scan --language javascript --use-sample
PYTHONPATH=src python -m zeroday.cli scan --language c_family --use-sample
```

Or scan your own target but filter a single language:

```bash
PYTHONPATH=src python -m zeroday.cli scan /path/to/repo --language python
```
