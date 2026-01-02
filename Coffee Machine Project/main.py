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

coffee=input("What would you like? (espresso/latte/cappuccino):").lower()


#price
def price():
    print("Please insert coins")
    quaters=int(input("How many quaters?:"))
    dimes=int(input("How many dimes?:"))
    nickels=int(input("How many nickles?:"))
    pennies=int(input("How many pennies?:"))
    quaters=quaters*0.25
    dimes=dimes*0.1
    nickels=nickels*0.05
    pennies*=0.01
    price_dollars=quaters+dimes+nickels+pennies

    if coffee == "espresso":
        cost=1.5
        if price_dollars <=cost:
            print(f"Here is your change{price_dollars-cost}")
        else:
            print("Sorry that's not enough money. Money refunded.")




def coffee_item():
    if coffee == "espresso":
        price()






