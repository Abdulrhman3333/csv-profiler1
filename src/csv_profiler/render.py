from __future__ import annotations
import json
from pathlib import Path
from datetime import datetime

def md_header(source: str) -> list[str]:
    ts = datetime.now().isoformat(timespec="seconds")
    return [
        "# CSV Profiling Report",
        "",
        f"- **Source:** `{source}`",
        f"- **Generated time:** `{ts}`",
        "",
    ]

def md_table_header() -> list[str]:
    return [
        "| Column | Type | Missing % | Unique |\n",
        "|---|---|---:|---:|---|\n",
    ]

def md_col_row(name: str, typ: str, missing: int, missing_pct: float, unique: str):
    return f"| `{name}` | {typ} | {missing} ({missing_pct:.1%}) | {unique} |"

def write_json(report: dict, path: str | Path) -> None:
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    text = json.dumps(report, indent=2, ensure_ascii=False) + "\n"
    path.write_text(text, encoding="utf-8")

def write_markdown(report: dict, path: str | Path) -> None:
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)

    total_rows = report["summary"]["rows"]

    lines: list[str] = []
    lines.extend(md_header("data/sample.csv"))

    lines.append("## Summary\n")
    lines.append(f"- Rows: {total_rows:,}\n")
    lines.append(f"- Columns: {report['summary']['columns']:,}\n")
    lines.append("\n")

    lines.append("## Columns (table)\n")
    lines.extend(md_table_header())

    for name, col in report["columns"].items():
        stats = col["stats"]
        missing = stats.get("missing", 0)
        missing_pct = (missing / total_rows) if total_rows else 0.0
        unique = stats.get("unique", 0)
        typ = col.get("type", "text")

        extra = ""
        if typ == "number":
            extra = (
                f"min={stats.get('min')}, max={stats.get('max')}, "
                f"mean={stats.get('mean')}"
            )
        else:
            top = stats.get("top-k", [])
            preview = ", ".join(f"{t['value']}({t['count']})" for t in top[:3])
            extra = f"top: {preview}" if preview else ""

        lines.append(
            f"| {name} | {typ} | {missing_pct:.1%} | {unique} | {extra} |\n"
        )

    lines.append("\n## Columns (details)\n\n")
    for name, col in report["columns"].items():
        stats = col["stats"]
        lines.append(f"### {name}\n")
        lines.append(f"- Type: {col.get('type', 'text')}\n")
        lines.append(f"- Non-empty: {stats.get('count', 0)}\n")
        lines.append(f"- Missing: {stats.get('missing', 0)}\n")
        if col.get("type") == "number":
            lines.append(f"- Min: {stats.get('min')}\n")
            lines.append(f"- Max: {stats.get('max')}\n")
            lines.append(f"- Mean: {stats.get('mean')}\n")
        else:
            top = stats.get("top-k", [])
            if top:
                lines.append("- Top values:\n")
                for item in top:
                    lines.append(f"  - {item['value']}: {item['count']}\n")
        lines.append("\n")

    path.write_text("".join(lines))

def render_markdown(report: dict) -> str:
    lines: list[str] = []
    lines.append(f"# CSV Profiling Report\n")
    lines.append(f"Generated: {datetime.now().isoformat(timespec='seconds')}\n")
    lines.append("## Summary\n")
    lines.append(f"- Rows: **{report['n_rows']}**")
    lines.append(f"- Columns: **{report['n_cols']}**\n")
    lines.append("## Columns\n")
    lines.append("| name | type | missing | missing_pct | unique |")
    lines.append("|---|---:|---:|---:|---:|")
    lines.extend([
        f"| {c['name']} | {c['type']} | {c['missing']} | {c['missing_pct']:.1f}% | {c['unique']} |"
        for c in report["columns"]
    ])
    lines.append("\n## Notes\n")
    lines.append("- Missing values are: `''`, `na`, `n/a`, `null`, `none`, `nan` (case-insensitive)")
    return "\n".join(lines)