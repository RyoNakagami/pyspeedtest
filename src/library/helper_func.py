# src/library/helper_func.py
from pathlib import Path
import tomllib

def get_version() -> str:
    """
    Return the package version from pyproject.toml (Poetry).
    Returns '0.0.0' if file or version not found.
    """
    # src/library から pyproject.toml は 2 階層上
    pyproject_file = Path(__file__).parents[2] / "pyproject.toml"

    if not pyproject_file.exists():
        return "0.0.0"

    try:
        with pyproject_file.open("rb") as f:
            pyproject_data = tomllib.load(f)
        version = pyproject_data.get("tool", {}).get("poetry", {}).get("version")
        return version or "0.0.0"
    except Exception:
        return "0.0.0"
