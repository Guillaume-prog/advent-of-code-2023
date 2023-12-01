import sys
from os import path

def load_input(fp) -> list[str]:
    if len(sys.argv) >= 2 and sys.argv[1] == "test":
        ext = "test"
    else:
        ext = "secret"

    print(f"=== Using {ext} input ===")

    p = path.join(path.dirname(fp), f"input.{ext}")
    with open(p, "r") as f:
        data = f.readlines()

    return data