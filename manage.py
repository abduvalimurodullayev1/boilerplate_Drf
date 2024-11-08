#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
from pathlib import Path

import environ


def main():
    """Run administrative tasks."""
    base_dir = Path(__file__).resolve().parent
    environ.Env().read_env(os.path.join(base_dir, ".env"))

    """
    change settings module to core.settings.test when running tests
    """

    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()
