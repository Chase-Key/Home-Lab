# Beginning of Coffee Shop Simulation... Enjoy!
#
# Time Module
from datetime import datetime, timedelta
from datetime import date
now = datetime.now()
today = date.today()
import sys


def hour_rounder(t):
    return t.replace(second=0, microsecond=0, minute=0, hour=t.hour)
# Print(now) #<--Command to see time\date

# Imports\Functions\Variables for Coffee Simulation\Game\Art


def banner(sign):  # Banner for all menus
    print("\n|----------------------------------------|")
    print("|         *Azure's Coffee Company*       |")
    print("|                *" + str(sign) + "*              ")
    print("|----------------------------------------|")
# Art Module
from art import tprint
#tprint()  #<-- Command to print designs
import random
latte_count = 0
expresso_count = 0
reg_count = 0
whipped_count = 0
caramel_count = 0

while True:
    banner("Welcome!")
    print(" a) Enter Store ")
    print(" b) Leave ")
    print(" c) admin\n")
    print("|Please enter your option below|")
    welcome = input("   [Azure'sCoffeeCompany]: ")
# Coffee Shop
    if str.lower(welcome) == "a":
        while True:
            banner("Main Menu")
            print(" 1. Drink Menu ")
            print(" 2. Extras Menu ")
            print(" 3. Checkout \n")
            try:
                choice = int(input("[Azure'sCoffeeCo]\nSelect(1-3): "))
            except ValueError:
                continue
            else:
                if choice == 1:
                    while True:
                        banner("Drink menu")
                        print(" l - Latte'  - $6.49")
                        print(" e - Expresso  - $5.49")
                        print(" r - Regular  - $4.95\n")
                        menu_choice = input("[Azure'sCoffeeCo]\n(l,e,r): ")
                        if str.lower(menu_choice) == 'l':
                            print("Latte it is!")
                            banner("Latte")
                            while True:
                                amount = int(input("Enter number of Latte's (limit: 10 per customer): "))
                                if amount <= 10:
                                    latte_count += amount
                                    break
                                else:
                                    print(" Oops, wrong input")
                                    continue
                        elif str.lower(menu_choice) == 'e':
                            print("Expresso stat!")
                            banner("Expresso")
                            while True:
                                amount = int(input("Enter number of Expresso's (limit: 10 per customer): "))
                                if amount <= 10:
                                    expresso_count += amount
                                    break
                                else:
                                    print(" Oops, wrong input")
                                    continue
                        elif str.lower(menu_choice) == 'r':
                            print("Regular to even out your awesomeness.")
                            banner("Regular")
                            while True:
                                amount = int(input("Enter number of Regular's (limit: 10 per customer): "))
                                if amount <= 10:
                                    expresso_count += amount
                                    break
                                else:
                                    print(" Oops, wrong input")
                                    continue
                        else:
                            continue

                elif choice == 2:
                    while True:
                        banner("Extra's Menu")
                        print(" w - Whipped Cream = $0.49")
                        print(" c - Caramel = $0.69\n")
                        sides_choice = input("[Azure'sCoffeeCo]\nSelect(w or c): ")
                        if str.lower(sides_choice) == 'w':
                            while True:
                                banner("Whipped Cream")
                                amount = int(input("Enter number of drinks with whipped cream (limit: 10 per customer): "))
                                if amount <= 10:
                                    whipped_count += amount
                                    break
                                else:
                                    print(" Oops, wrong input")
                                    continue
                        elif str.lower(sides_choice) == 'c':
                            while True:
                                banner("Caramel")
                                amount = int(input("Enter number of drinks with caramel (limit: 10 per customer): "))
                                if amount <= 10:
                                    caramel_count += amount
                                    break
                                else:
                                    print(" Oops, wrong input")
                                    continue
                        else:
                            print(" Oops, wrong input")
                            continue

                elif choice == 3:
                    print("\nThank you for coming in today!")
                    sub = (latte_count * 6.49) + (expresso_count * 5.49) + (reg_count * 4.95) + (whipped_count * 0.49) + (caramel_count * 0.69)
                    sides_count = whipped_count + caramel_count
                    drink_count = latte_count + expresso_count + reg_count
                    tax = sub * 0.0875
                    total = sub + tax
                    print("\n|----------------------------------------|")
                    print("|         *Azure's Coffee Company*       |")
                    print("|----------------------------------------|")
                    print("|-----------------RECEIPT----------------|")
                    print('|  Drinks: {0}'.format(drink_count))
                    print('|  Extras: {0}'.format(sides_count))
                    print("|----------------------------------------|")
                    print('|  Subtotal: ${:0.2f}'.format(sub))
                    print('|  Tax: ${:0.2f}'.format(tax))
                    print("|----------------------------------------|")
                    print('|  Total: ${:0.2f}'.format(total))
                    print("|----------------RECEIPT-----------------|")
                    print("|  " + str(now))
                    print("|----------------------------------------|")
                    print("|         *Azure's Coffee Company*       |")
                    print("|            *Have a nice day!*          |")
                    print("|----------------------------------------|")
                    sys.exit()
                else:
                    print(" Oops, wrong input")
                    continue
# Exit
    elif str.lower(welcome) == "b":
        banner("Goodbye!")
        sys.exit()
# Admin Area
    elif str.lower(welcome) == "c":
        banner("Admin Area")
        loop = True
        while loop:
            print(" Please enter the correct username.\n Press Q to quit.")
            user_name = input("\nUsername: ")
            if str.capitalize(user_name) == "Q":
                sys.exit()
            elif str(user_name) == "Azure'sDad":
                print("\n Username Accepted!")
                break
            else:
                print("\n Wrong input!")

        while loop:
            print(" Please enter the correct password.\n Press Q to quit.")
            password = input("\nPassword: ")
            if str.capitalize(password) == 'Q':
                print("\n Come back soon!")
                sys.exit()
            elif str(password) == "3/1/2022":
                print("\n Password Accepted!")
                break
            else:
                print("Wrong password. Try again.")

        print("\n|----------------------------------------|")
        print("|         *Azure's Coffee Company*       |")
        tprint("|               *               |")
        print("|              *Secret Area*             |")
        print("|----------------------------------------|")
        print("   a) Play game ")
        print("   b) Leave ")
        admin_log = input("\n[Azure'sCoffeeCompany]: ")
        while True:
            if str.lower(admin_log) == "a":
                # Computer guessing Game
                def computer_guess(x):
                    low = 1
                    high = x
                    feedback = ''
                    while feedback != 'c':
                        if low != high:
                            guess = random.randint(low, high)
                        else:
                            guess = low  # could also be high cause low = high
                        feedback = input("\nThink of a number between 1 and 100...\nThe computer's guess is: (" + str(guess) + ")\nIs " + str(guess) + " too high? (H) Is " + str(guess) + " too low? (L) Is " + str(guess) + " correct? (C)?\n[Azure'sCoffeeCompany]: \n\n")
                        if str.lower(feedback) == 'h':
                            high = guess - 1
                        elif str.lower(feedback) == 'l':
                            low = guess - 1
                    print("\n\n           Yay! The computer guessed your number correctly!")
                computer_guess(100) #Can set (guess) to a higher value
            elif str.lower(admin_log) == "b":
                quit()
            else:
                print(" Oops, wrong input")
                continue
    else:
        print(" Oops, wrong input.")
        continue

# End of Coffee Simulation


