"""Console script for python_app_1."""
import sys
import click


@click.command()
def main(args=None):
    """Console script for python_app_1."""
    click.echo("Replace this message by putting your code into "
               "python_app_1.cli.main")
    click.echo("See click documentation at https://click.palletsprojects.com/")
    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
