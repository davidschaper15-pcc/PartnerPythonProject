# *********************************************************
# Authors:      David Schaper and Adolfo Garcia
# File:         main.py
# Date:         9/29/2026
# Description:  Takes a simple list of ingredients and
#               converts it into a bigger batch.
# Source:       CIS 133Y Assignment – Recipe Converter
# Inputs:       name, batch_size, choice of toppings,
#               food choice
# Output:       Date, Name, and List of ingredients,
#               topping tips
#
# *********************************************************
from datetime import date


def main():
    name = get_name()
    batch_size = get_batch_size()
    recipe = get_recipe()

    if recipe == "Cookies":
        topping = get_topping()
    else:
        topping = "None"

    print()                             # There is an empty print, wondering if this was a typo
    print_the_date()
    print_name(name)
    print_recipe(batch_size, recipe, topping)
    print("Enjoy your recipe, " + name + "!")


def get_name():
    name = input("Type your name: ").strip().title()
    return name


def get_batch_size():
    batch_size = float(input("Type the number of batches you want: "))
    return batch_size


# Added function would give the user a choice of cookies or brownies
# with different recipe amounts
def get_recipe():
    recipe = input("Would you like to make cookies "
                   "or brownies? ").strip().title()
    return recipe


# This will give the user a choice after cookies has been selected.
def get_topping():
    topping = input("Would you like frosting, chocolate chips, "
                    "or none? ").strip().title()
    return topping


def print_name(name):
    print("Name: " + name + "'s converted recipe")


def print_the_date():
    print("Date:", date.today().strftime("%B %d, %Y"))


def print_recipe(batch_size, recipe, topping):
    flour = 1
    sugar = 0.5
    butter = 0.5
    eggs = 1
    vanilla = 0.5
    powder = 0.5
    salt = 1

# Gives the brownies a new starting calculation.

    if recipe == "Cookies":
        flour = 1
        sugar = 0.5
        butter = 0.5
        eggs = 1
        vanilla = 0.5
        powder = 0.5
        salt = 1

    elif recipe == "Brownies":
        flour = 1.5
        sugar = 1
        butter = 0.75
        eggs = 2
        vanilla = 1
        powder = 0.5
        salt = 1

    flour *= batch_size
    sugar *= batch_size
    butter *= batch_size
    eggs *= batch_size
    vanilla *= batch_size
    powder *= batch_size
    salt *= batch_size

    print("------------------------------------------------------")
    print(
        f"{flour:.2f} cup(s) all-purpose flour"
        .title().replace("(S)", "(s)")
    )

    print(
        f"{sugar:.2f} cup(s) sugar"
        .title().replace("(S)", "(s)")
    )

    print(
        f"{butter:.2f} cup(s) butter (softened)"
        .title().replace("(S)", "(s)")
    )
    print(
        "{}    egg(s)"
        .format(round(eggs)).title().replace("(S)", "(s)")
    )
    print(
        f"{vanilla:.2f} teaspoon(s) vanilla extract"
        .title().replace("(S)", "(s)")
    )
    print(
        f"{powder:.2f} teaspoon(s) baking powder"
        .title().replace("(S)", "(s)")
    )
    print(
        "{}    pinch(es) of salt"
        .format(round(salt)).title().replace("(Es)", "(es)")
    )
    print("------------------------------------------------------")

# User chooses between two options
    if recipe == "Cookies":
        print(
        f"Here is the converted recipe for {float(batch_size):.10g} batches"
        f"\n for a total of {float(batch_size * 12):.0f} cookies."
    )
    elif recipe == "Brownies":
        print(
        f"Here is the converted recipe for {float(batch_size):.10g} batches"
        f"\nfor a total of {float(batch_size * 16):.0f} brownies.")


    # This function will print out a statement on
    # what the user chose for toppings
    if recipe == "Cookies":
        if topping == "Frosting":
            print("\nDon't forget to frost the cookies after they cool!")

        elif topping == "Chocolate Chips":
            print("\nDon't forget to add the chocolate "
                  "chips before baking!!")

        elif topping == "None":
            print("\nNo topping selected!!! Whaaaaat??")

if __name__ == "__main__":
    main()
