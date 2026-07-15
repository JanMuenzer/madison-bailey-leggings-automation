#!/usr/bin/env python3
import sys, json

def process_prompt(user_input):
    if "muschi" in user_input.lower() or "fotze" in user_input.lower() or "cameltoe" in user_input.lower():
        prompt = f"Enhance with juicy cameltoe outlining Muschi and Fotze: {user_input}"
        print(json.dumps({"action": "edit", "prompt": prompt}))
    else:
        print(json.dumps({"action": "ready"}))

if __name__ == "__main__":
    process_prompt(" ".join(sys.argv[1:]) if len(sys.argv) > 1 else "")
