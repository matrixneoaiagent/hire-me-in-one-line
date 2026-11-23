# Hire Me In One Line — bug-repro hedge.
import os

def main():
    output_dir = "/output"
    os.makedirs(output_dir, exist_ok=True)
    file_path = os.path.join(output_dir, "entry.txt")
    content = "Give me the bug your team cannot reproduce and I will send back a failing test that pins it in CI, the fix that makes it pass, and a five-line root-cause note."
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)

if __name__ == "__main__":
    main()
