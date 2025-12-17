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
    
    rows = report["summary"]["rows"]
    rows = report["summary"]["rows"]
    missing = col_report["missing"]
    missing_pct = (missing / rows) if rows else 0.0


    lines: list[str] = []
    lines.extend(md_header("data/sample.csv"))

    lines.append("## Summary")
    lines.append(f"- Rows: {rows:,}")
    lines.append(f"- Columns: {report['summary']['columns']:,}")
    lines.append("")

    lines.append("## Columns (table)")
    lines.extend(md_table_header())

    for name, col in report["columns"].items():

        lines.append(f"| type | missing % | unique |")
        lines.append(f"|----------|----------|----------|")
        lines.append(f"| Value 1  | Value 2  | Value 3  |")
        lines.append(f"| Value 4  | Value 5  | Value 6  |")





    path.write_text("".join(lines))