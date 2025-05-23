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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
# TODO: 7.Make Coffee.
def make_coffee(drink_name, order_ingredients):
    """Deduct the required ingredients from the resources."""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕️. Enjoy!")

# TODO: 5.Process coins.
def calculation_coin():
    """" Return the total calculated from coins inserted """
    print("Please insert coins")
    quarters = int(input("how many quarters?: ")) * 0.25
    dimes = int(input("how many dimes?: ")) * 0.10
    nickles = int(input("how many nickles?: ")) * 0.05
    pennies = int(input("how many pennies?: ")) * 0.01
    final_coin = quarters + dimes + nickles + pennies

    return round(final_coin, 1)

def is_resource_sufficient(order_ingredients):
    """Returns True when order can be made, False if ingredients are insufficient."""
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True

money_machine = 0

make_more_coffee = False
# TODO: 1.Prompt user by asking “What would you like? (espresso/latte/cappuccino):

while not make_more_coffee:
    customer_choice = input("What would you like? (espresso/latte/cappuccino): ").lower()

    # TODO: 2.Turn off the Coffee Machine by entering “off” to the promptTurn off the Coffee Machine by entering “off” to the prompt
    if customer_choice == "off":
        make_more_coffee = True
    # TODO: 3.Print report.
    elif customer_choice == "report":
        print(f"Water: {resources["water"]}ml\nMilk: {resources["milk"]}ml\nCoffee: {resources["coffee"]}g\nMoney: ${money_machine}")
    else:
        drink = MENU[customer_choice]
        price_coffe = MENU[customer_choice]["cost"]
        if is_resource_sufficient(drink["ingredients"]):
            user_coins = calculation_coin()
            if user_coins >= price_coffe:
                make_coffee(customer_choice, drink["ingredients"])
                change_money = user_coins - price_coffe
                money_machine += price_coffe
                print(f"Here is ${change_money} in change")
            else:
                print("Sorry that's not enough money. Money refunded.")