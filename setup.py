#!/usr/bin/env python
"""
Modern setup.py that forwards to pyproject.toml configuration.
This is kept for backward compatibility with tools that still expect setup.py.
"""

from setuptools import setup

if __name__ == "__main__":
    setup()
