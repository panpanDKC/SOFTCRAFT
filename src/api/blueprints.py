from fastapi import FastAPI, HTTPException
from io_methods import parse_blueprints
from solve import compute_qualities

app = FastAPI()


@app.get("/blueprints/analyze")
def analyze():
    try:
        blueprints = parse_blueprints("src/data/diamond_example.txt")
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

    qualities = compute_qualities(blueprints)
    best_id = max(qualities, key=lambda x: x[1])[0]
    return {
        "bestBlueprint": str(best_id),
        "blueprints": [{"id": str(id_), "quality": quality} for id_, quality in qualities],
    }
