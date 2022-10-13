import re
import sys


def main():
    print(parse(input("HTML: ").strip()))


def parse(s):
    if s := re.search(r'"(https?://)?(www\.)?youtube\.com/embed/([A-Za-z0-9]+)?(")?', s, re.ASCII):
        return f"https://youtu.be/{s.group(3)}"
    else:
        return None



if __name__ == "__main__":
    main()
