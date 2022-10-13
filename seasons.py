from datetime import date
#from num2words import num2words
import re
import sys
import inflect

p = inflect.engine()


def main():
    birthday = input("DOB: ")
    try:
        year, month, day = convert_date(birthday)
        #print(year, month, day)
    except:
        sys.exit("Invalid date")
    else:
        birth_date = date(int(year), int(month), int(day))
        days_old = abs(birth_date - date.today())
        minutes_old = int(days_old.days) * 24 * 60
        word_minutes = p.number_to_words(minutes_old, andword="")
        print(word_minutes.capitalize() + " minutes")

    #birthday = date(int(year), int(month), int(day))
    #days_old = abs(birthday - date.today())
    #minutes_old = int(days_old.days) * 24 * 60
    #word_minutes = num2words(minutes_old)
    #word_minutes = word_minutes.capitalize().replace(" and", "")
    #print(f"{word_minutes} minutes")


def convert_date(birthday):
    if re.search(r"^([0-2][0-9][0-9][0-9])-([0-1][0-9])-([0-3][0-9])$", birthday):
        year, month, day = birthday.split("-")
        #print(year, month, day)
        return year, month, day


if __name__ == "__main__":
    main()
