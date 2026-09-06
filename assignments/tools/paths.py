from pathlib import Path
import tomllib


ROOT = Path(__file__).resolve().parents[1]

with open(ROOT / "paths.toml", "rb") as f:
    CONFIG = tomllib.load(f)


def path(section: str, name: str) -> Path:
    value = CONFIG[section][name]
    return (ROOT / value).resolve()