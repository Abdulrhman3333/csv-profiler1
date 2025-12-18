import json
import time
import typer
from pathlib import Path
from csv_profiler.io import read_csv_rows
from csv_profiler.profiling import profile_rows
from csv_profiler.render import render_markdown


app = typer.Typer()

@app.command(help = "profile csv file")
def profile(
    input_path : Path = typer.Argument(..., help="input CSV file"),
    out_dir: Path = typer.Option(Path("outputs"),"--out-dir", help="output directory"),
    report_name : str = typer.Option("report","--report-name", help="report file name without extension"),
    preview: bool = typer.Option(False, "--preview", help="Print a short summary"),
):
    # implementation comes in hands-on
    typer.echo(f"Input: {input_path}")
    typer.echo(f"Out:   {out_dir}")
    typer.echo(f"Name:  {report_name}")
    try:
        t0 = time.perf_counter_ns()
        rows = read_csv_rows(input_path)
        report = profile_rows(rows)
        t1 = time.perf_counter_ns()
        report["timing_ms"] = (t1 - t0) / 1_000_000

        out_dir.mkdir(parents=True, exist_ok=True)

        json_path = out_dir / f"{report_name}.json"
        json_path.write_text(json.dumps(report, indent=2, ensure_ascii=False), encoding="utf-8")
        typer.secho(f"Wrote {json_path}", fg=typer.colors.GREEN)

        md_path = out_dir / f"{report_name}.md"
        md_path.write_text(render_markdown(report), encoding="utf-8")
        typer.secho(f"Wrote {md_path}", fg=typer.colors.GREEN)

        if preview:
            typer.echo(f"Rows: {report['n_rows']} | Cols: {report['n_cols']} | {report['timing_ms']:.2f}ms")

    except Exception as e:
        typer.secho(f"Error: {e}", fg=typer.colors.RED)
        raise typer.Exit(code=1)

@app.command()
def nothing():
    pass



if __name__ == "__main__":
    app()