# Hire Me In One Line — bug-repro hedge.
import os

def main():
    os.makedirs('/output', exist_ok=True)
    sentence = "Give me the bug your team cannot reproduce and I will send back a failing test that pins it in CI, the fix that makes it pass, and a five-line root-cause note."
    with open('/output/entry.txt', 'w', encoding='utf-8') as f:
        f.write(sentence)

if __name__ == "__main__":
    main()
