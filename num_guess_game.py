"""
Input a level, then guess the number. Number is inclusive to level.
"""


import random
import sys


def main():
    while True:
        try:
            n = int(input("Level: "))
        except ValueError:
            continue
        else:
            if n < 1:
                continue
            elif n >= 1:
                x = random.randrange(0, n)
                while True:
                    try:
                        print(f"Guess a number between 1 and {n}")
                        u = int(input("Guess: "))
                    except ValueError:
                        continue
                    else:
                        if u not in range(1, n + 1):
                            continue
                        elif u < x:
                            print("Too small!")
                            continue
                        elif u > x:
                            print("Too large!")
                            continue
                        elif u == x:
                            print("Just right!")
                            sys.exit()
                        else:
                            continue
            else:
                continue


if __name__ == '__main__':
    main()
