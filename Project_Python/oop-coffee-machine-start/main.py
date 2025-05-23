from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
from item import MenuItem

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

#TODO 1: create object
my_menu = Menu()
make_drink = CoffeeMaker()
profit = MoneyMachine()
items = MenuItem()

is_on = True

while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        make_drink.report()
        profit.report()
    else:
        items.name = choice
        items.cost = MENU[choice]["cost"]
        drink = items.name
        cost = items.cost
        ingredient = my_menu.find_drink(drink)
        if make_drink.is_resource_sufficient(ingredient):
            if profit.make_payment(cost):
                make_drink.make_coffee(ingredient)




