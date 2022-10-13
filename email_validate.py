from validator_collection import validators, checkers, errors

import sys


def main():
    print(validate(input("Email: ")))


def validate(email):
    try:
        email_address = validators.email(email)
    except errors.EmptyValueError:
        return "Invalid"
    except errors.InvalidEmailError:
        return "Invalid"
    else:
        return "Valid"


if __name__ == '__main__':
    main()
