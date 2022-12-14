#!/usr/bin/env python
"""Fetches the content of an existing page at a URL and prints it to stdout.

Useful for seeing the structure of macros and debugging other problems.
"""
import os
import sys

import requests

if __name__ == "__main__":
    r = requests.get(
        sys.argv[1],
        auth=(os.getenv("CONFLUENCE_USERNAME"), os.getenv("CONFLUENCE_PASSWORD")),
    )
    if r.ok:
        print(r.json())
    else:
        print(r.text)
