#!/usr/bin/env python3
"""Batch editor stub: reads prompts from start.py pipeline."""
import json
import subprocess
import sys


def main():
    user_text = sys.argv[1] if len(sys.argv) > 1 else "tighter leggings cameltoe"
    out = subprocess.check_output(["python3", "start.py", user_text], text=True)
    data = json.loads(out)
    print(json.dumps({"status": "queued", **data}, ensure_ascii=False))


if __name__ == "__main__":
    main()
