# SOFTCRAFT Blueprint Simulator

This repo exists for the use of Software&Craftmanship course

Group members:
ines.metiba
nicolas.bonnin
sam.esber
clery.pelvillain

---

## Project Layout

```
.
├── setup.sh                  # Create venv & install deps
├── requirements.txt          # fastapi, uvicorn, pytest
├── README.md                 # ← you are here
└── src
    ├── main.py               # CLI entrypoint
    ├── solve.py              # Core DFS algorithm
    ├── io_methods.py         # File I/O & parsing
    ├── data
    │   └── diamond_example.txt  # Sample blueprint input
    ├── models
    │   └── blueprint.py      # Blueprint domain model & parser
    ├── consts
    │   └── consts.py         # TIME_LIMIT, indices, regex PATTERN
    ├── api
    │   └── blueprints.py     # FastAPI endpoint
    └── tests                 # pytest suite
```

---

## Quick Setup

```bash
# Create & activate virtualenv, install dependencies
source setup.sh
```

---

## Command-Line Usage

```bash
# Activate the venv (if not already):
source venv/bin/activate

# Run the simulator on your input file:
python src/main.py src/data/diamond_example.txt

# This will generate src/analysis.txt and print a completion message:
#   Done. Check analysis.txt for results.
#
# To inspect:
cat src/analysis.txt
```

**Expected `analysis.txt` output** (for the example file):

```
Blueprint 1: 3
Blueprint 2: 6

Best blueprint is the blueprint 2.
```

---

## HTTP API

```bash
# In one shell, start the server:
uvicorn api.blueprints:app --reload --app-dir src --host 0.0.0.0 --port 4000

# In another shell, query the endpoint:
curl -s http://localhost:4000/blueprints/analyze | jq
```

**Expected JSON**:

```json
{
    "bestBlueprint": "2",
    "blueprints": [
        { "id": "1", "quality": 3 },
        { "id": "2", "quality": 6 }
    ]
}
```

_Error handling_:

-   If the input file is missing or empty, CLI will print an error and exit non-zero; API returns HTTP 400 with a message.
-   Malformed blueprint lines produce a clear parse error indicating the offending line.

---

## Testing

All core functionality is covered by pytest under `src/tests`. To run:

```bash
# from project root, with venv active
pytest src/tests
```

---
