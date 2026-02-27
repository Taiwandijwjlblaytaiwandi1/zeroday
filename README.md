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
