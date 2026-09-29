# *********************************************************
# Authors:      David Schaper and Adolfo Garcia
# File:         main.py
# Date:         9/29/2026
# Description:  Takes a simple list of ingredients and
#               converts it into a bigger batch.
# Source:       CIS 133Y Assignment – Recipe Converter
# Inputs:       name and batch_size
# Output:       Date, Name, and List of ingredients
# *********************************************************
from datetime import date


def main():
    name = get_name()
    batch_size = get_batch_size()
    print_the_date()
    print_name(name)
    print_recipe(batch_size)


def get_name():
    name = input("Type your name: ").strip().title()
    return name


def get_batch_size():
    batch_size = float(input("Type the number of batches you want: "))
    return batch_size


def print_name(name):
    print("Name: " + name + "'s converted recipe")


def print_the_date():
    print("Date:", date.today().strftime("%B %d, %Y"))


def print_recipe(batch_size):
    flour = 1
    sugar = 0.5
    butter = 0.5
    eggs = 1
    vanilla = 0.5
    powder = 0.5
    salt = 1

    flour *= batch_size
    sugar *= batch_size
    butter *= batch_size
    eggs *= batch_size
    vanilla *= batch_size
    powder *= batch_size
    salt *= batch_size

    print(f"{flour:.2f} cup(s) all-purpose flour".title().replace("(S)", "(s)"))
    print(f"{sugar:.2f} cup(s) sugar".title().replace("(S)", "(s)"))
    print(f"{butter:.2f} cup(s) butter (softend)".title().replace("(S)", "(s)"))
    print("{}    egg(s)".format(round(eggs)).title().replace("(S)", "(s)"))
    print(f"{vanilla:.2f} teaspoon(s) vanilla extract".title().replace("(S)", "(s)"))
    print(f"{powder:.2f} teaspoon(s) baking powder".title().replace("(S)", "(s)"))
    print("{}    pinch(es) of salt".format(round(salt)).title().replace("(Es)", "(es)"))
    print("\n")


if __name__ == "__main__":
    main()
