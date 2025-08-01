"""Command line interface for the best practices examples."""

import typer
from rich.console import Console
from rich.table import Table

app = typer.Typer(
    name="best-practices",
    help="Python Best Practices CLI",
    add_completion=False,
)
console = Console()


@app.command()
def hello(name: str = typer.Argument(..., help="Name to greet")) -> None:
    """Say hello to someone."""
    console.print(f"[green]Hello {name}![/green]")


@app.command()
def info() -> None:
    """Show information about this project."""
    table = Table(title="Python Best Practices")

    table.add_column("Category", style="cyan", no_wrap=True)
    table.add_column("Tools", style="magenta")
    table.add_column("Status", justify="center")

    table.add_row("Testing", "pytest, coverage, hypothesis", "✅")
    table.add_row("Code Quality", "black, ruff, mypy", "✅")
    table.add_row("CLI", "typer, rich", "✅")
    table.add_row("Documentation", "mkdocs, mkdocstrings", "✅")

    console.print(table)


if __name__ == "__main__":
    app()

