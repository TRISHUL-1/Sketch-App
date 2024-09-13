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
profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def printResource():
    """ To print the current resources left in the machine """
    print(f"water : {resources['water']}ml")
    print(f"milk : {resources['milk']}ml")
    print(f"coffee : {resources['coffee']}gm")
    print(f"Money : ${profit}")

def checkResource(drink,drinkIngredients):
    """ Checks wheather the machine has enough resources and returns True/False """
    
    if drink == "latte" or drink == "cappuccino":
        if  resources["water"] < drinkIngredients["water"]:
            print("Sorry there is not enough water.")
            return False
        elif resources["milk"] < drinkIngredients["milk"] :
            print("Sorry there is not enough milk.")
            return False
        elif resources["coffee"] < drinkIngredients["coffee"] :
            print("Sorry there is not enough coffee.")
            return False
        
    else:
        if  resources["water"] < drinkIngredients["water"]:
            print("Sorry there is not enough water.")
            return False
        elif resources["coffee"] < drinkIngredients["coffee"] :
            print("Sorry there is not enough coffee.")
            return False
    
    return True

def calculateCoins():
    """ Returns the amount of money inserted by the User """
    # quarters = $0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01
    print("Please insert coins")
    total = int(input("How many quarters : "))  * 0.25 
    total += int(input("How many quarters : "))  * 0.10
    total += int(input("How many quarters : "))  * 0.05
    total += int(input("How many quarters : "))  * 0.01
    return total

def transactionSucces(payment, drinkCost) :
    """ Returns true if transaction was successfull otherwise false """

    if payment < drinkCost : 
        print("Sorry that's not enough money. Money refunded.")
        return False
    else :
        change = round(payment - drinkCost, 2)
        print(f"Here is your Change : ${change}")
        global profit
        profit += drinkCost
        return True


def makeCoffee(choice, drinkIngredients):
    """ Deduct resources based on the drink ordered """
    for item in drinkIngredients:
        resources[item] -= drinkIngredients[item]
    print(f"Here is you {choice} ☕")



while True:
    userChoice = input("What would you like (espresso/latte/cappuccino) : ")

    if userChoice.lower() == "off":
        break
    elif userChoice.lower() == "report":
        printResource()
        continue
    else:
        drink = MENU[userChoice]
        resourceOk = checkResource(drink,drink["ingredients"])
        if resourceOk:
            payment = calculateCoins()
            if transactionSucces(payment, drink["cost"]):
                makeCoffee(userChoice ,drink["ingredients"])