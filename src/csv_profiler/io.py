from __future__ import annotations
from csv import DictReader
from pathlib import Path
def read_csv_rows(path: str | Path) -> list[dict[str, str]]:
    """Read a CSV as a list of rows (each row is a dict of strings)."""
    path = Path(path) if isinstance(path, str) else path
    with path.open('r', encoding="utf-8", newline="") as f:
        reader = DictReader(f)
        # return [dict(reader) for row in reader]
        return list(reader)

    