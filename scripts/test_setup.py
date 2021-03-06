#! /usr/bin/python
from pip._internal import main as pip_main
import sys

if __name__ == '__main__':
    python_version = sys.version_info

    deps = [
        "execnet>=1.0.9",
        "pytest",
        "pyzmq",
        "sqlalchemy",
        "Jinja2",
    ]

    print("Setting up dependencies...")
    result = pip_main(["install"] + deps)
    sys.exit(result)
