import sys
from pathlib import Path
from csv_profiler.io import read_csv_rows
from csv_profiler.profiling import basic_profile
from csv_profiler.render import write_json, write_markdown

# Add the local src/ directory so imports work when running main.py directly
ROOT = Path(__file__).resolve().parent
SRC_DIR = ROOT / "src"
if str(SRC_DIR) not in sys.path:
    sys.path.insert(0, str(SRC_DIR))


def main() -> None:
    rows = read_csv_rows("data/sample.csv")
    report = basic_profile(rows)
    write_json(report, "outputs/report.json")
    write_markdown(report, "outputs/report.md")
    print("Wrote outputs/report.json and outputs/report.md")
if __name__ == "__main__":
    main()