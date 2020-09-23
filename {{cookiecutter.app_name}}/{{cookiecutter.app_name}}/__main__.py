#!/usr/bin/env python

import argparse

from . import __version__


def set_up_cli():
    """Set up parser for {{ cookiecutter.app_name }} entry point.

    """
    parser = argparse.ArgumentParser(prog="{{ cookiecutter.app_name }}")
    parser.add_argument(
        "--version", action="version", version=f"%(prog)s version {__version__}",
    )

    # my CLI arguments here

    return parser


def main():
    parser = set_up_cli()
    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
