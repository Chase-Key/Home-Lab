"""    ----> # Count lines of code in any .py file. <----
Take only 1 command line argument from user (filename.py).
If that filename.py doesn't end in ".py", then sys.exit().
If that filename.py doesn't exist, using file open will raise error.
Open that file and count how many lines of code there are, then close.
    - exclude any lines starting with "#".
    - Assume any line that contains  only whitespace is considered blank.
"""

import sys
import string

"""
def main():
    while True:
        for arg in sys.argv:
            if len(sys.argv) <= 1:
                sys.exit("Too few commands")
            elif len(sys.argv) > 2:
                sys.exit("Too many commands")
            else:
                filename = ' '.join(sys.argv[1:])
                if filename.endswith(".py"[-3:]):
                    with open(filename, "r") as file:
                        count = 0
                        for line in file.read().split("\n"):
                            if (not line.strip().startswith("#")) and (not line.strip() == ''):
                                count += 1
                else:
                    sys.exit("file not .py")

                print(count)
                sys.exit()


if __name__ == '__main__':
    main()
"""


def main():
    check_argv(sys.argv)


def check_argv(arg):
    for arg in sys.argv:
        if len(sys.argv) <= 1:
            sys.exit("Too few commands")
        elif len(sys.argv) > 2:
            sys.exit("Too many commands")
        else:
            return convert_filename(sys.argv[1:])


def convert_filename(argument):
    filename = ' '.join(sys.argv[1:])
    if filename.endswith(".py"[-3:]):
        return count_lines(filename)
    else:
        sys.exit("file not .py")


def count_lines(filename):
    with open(filename, "r") as file:
        count = 0
        for line in file.read().split("\n"):
            if (not line.strip().startswith("#")) and (not line.strip() == ''):
                count += 1
    print(count)
    sys.exit()


if __name__ == '__main__':
    main()
