import json
from pathlib import Path


def load_json_schema(filename: str):
    base_dir = Path(__file__).parent.parent.joinpath("src", "api", "schemas").joinpath(filename)
    with open(base_dir, encoding="utf-8") as schema_file:
        return json.loads(schema_file.read())
