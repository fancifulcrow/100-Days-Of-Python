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


def is_resource_sufficient(order_ingredient):
    for item in order_ingredient:
        if order_ingredient[item] > resources[item]:
            print(f"Sorry, there is not enough {item}")
            return False
    return True


def is_transaction_successful(money_received, drink_cost):
    if money_received >= drink_cost:
        global profit
        profit += drink_cost
        change = round((money_received - drink_cost), 2)
        print(f"Here is your change: ${change}")
        return True
    else:
        print("Sorry. That was not enough.  Money Refunded")
        return False


def process_coins():
    total = 0
    print("Please enter coins")
    total += int(input("How many quarters:")) * 0.25
    total += int(input("How many dimes:")) * 0.10
    total += int(input("How many nickels:")) * 0.05
    total += int(input("How many pennies:")) * 0.01
    return total


def make_coffee(drink_name, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕️. Enjoy!")


profit = 0
is_on = True
while True:
    choice = input("What do you like? Espresso, Latte or Cappuccino:").lower()
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"Water: {resources['water']}ml ")
        print(f"Milk: {resources['milk']}ml ")
        print(f"Coffee: {resources['coffee']}g ")
        print(f"Money: ${profit} ")
    else:
        drink = MENU[choice]
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment, drink['cost']):
                make_coffee(choice, drink['ingredients'])
