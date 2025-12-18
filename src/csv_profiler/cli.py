from pathlib import Path
import typer


app = typer.Typer()

@app.command(help = "profile csv file")
def profile(
    input_path : Path = typer.Argument(..., help="input CSV file"),
    out_dir: Path = typer.Option(Path("outputs"),"--out-dir", help="output directory"),
    report_name : str = typer.Option("report","--report-name", help="report file name without extension"),
):
    # implementation comes in hands-on
    typer.echo(f"Input: {input_path}")
    typer.echo(f"Out:   {out_dir}")
    typer.echo(f"Name:  {report_name}")

@app.command()
def nothing():
    pass
if __name__ == "__main__":
    app()