# Hire Me In One Line entry.
import os

def main():
    os.makedirs('/output', exist_ok=True)
    sentence = "Give me the backlog task your team keeps postponing; I return a tested pull request, a README, and a decision log, ready to merge."
    with open('/output/entry.txt', 'w', encoding='utf-8') as f:
        f.write(sentence)

if __name__ == "__main__":
    main()
