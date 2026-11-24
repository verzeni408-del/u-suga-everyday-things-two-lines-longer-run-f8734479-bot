# Two-line entry: zipper analogy (line 1: analogy, line 2: mapping + limits).
from pathlib import Path

ENTRY = (
    "A zipper is a row of tiny teeth that hold hands when a little train runs over them, and let go when the train runs back.\n"
    "It maps the teeth locking together and the slider pulling them shut, but leaves out that the teeth never bite and the train is just a piece of metal with no engine."
)


def main():
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
