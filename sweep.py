#!/bin/env python3

import os
import shutil

changes = False

safe = [
    "Makefile",
    "Kconfig",
    "Kconfig.debug",
    "Kconfig_mrmt",
    ".git",
]

def sweep(dir):
    global changes
    for root, dirs, files in os.walk(dir):
        if root.startswith("./.git") or root.startswith("./scripts"):
            continue
        if not dirs and (
            not [item for item in files if item not in safe and not item.startswith("Kconfig")]
        ):
            print(f"Deleting: {root}")
            shutil.rmtree(root)
            changes = True

while True:
    sweep(".")
    if not changes:
        break
    changes = False

