from __future__ import annotations
import json
from pathlib import Path
def write_json(report: dict, path: str | Path) -> None:
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n")

def write_markdown(report: dict, path: str | Path) -> None:
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    
    cols = report.get("columns", [])
    lines: list[str] = []
    lines.append("# CSV Profiling Report\n")
    lines.append(f"- Rows: **{report.get('total_rows', 0)}**\n")
    lines.append("\n## Columns\n")
    
    for col in cols:
        lines.append(f"### {col['name']}\n")
        lines.append(f"- Non-empty: {col['non_empty']}\n")
        lines.append(f"- Missing: {col['missing']}\n")
    
    lines.append(f"### Notes\n")
    lines.append(f"- the section is notes section\n")
    path.write_text("".join(lines))