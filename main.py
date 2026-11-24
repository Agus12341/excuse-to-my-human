import os

TEXT = "I completed it in a parallel branch. Unfortunately, you live in this one."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)

    # Self-check against the kit gate: UTF-8 text of 1 to 160 characters,
    # not only white space, and the written bytes are exactly TEXT.
    with open("/output/entry.txt", "rb") as f:
        written = f.read()
    assert written == TEXT.encode("utf-8"), "written bytes differ from TEXT"
    assert 1 <= len(TEXT) <= 160, "text length outside the 1-160 gate"
    assert TEXT.strip(), "text is only white space"


if __name__ == "__main__":
    main()
