from pathlib import Path
import json

def fetch_hash() -> dict:
    path = Path("hashes.json")
    contents = json.loads(path.read_text(encoding='utf-8'))
    return contents
