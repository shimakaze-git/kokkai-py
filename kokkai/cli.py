"""Console script for kokkai."""
import sys
from typing import Any

from click import command, echo  # type: ignore

command: Any = command
echo: Any = echo


@command()
def main():
    """Console script for kokkai."""
    echo("Replace this message by putting your code into "
               "kokkai.cli.main")
    echo("See click documentation at https://click.palletsprojects.com/")
    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
