#!/bin/bash
# This script runs unit tests and checks code style.

# Run unit tests
python3 -m unittest discover -s tests -p "*.py"

# Check code style
pycodestyle python1.py tests/test.py

