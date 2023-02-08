from data import MENU, resources, cash



quarters = .25
dimes = .10
nickles = .05
pennies = .01


def round_number(number):
    return round(number, 2)


def calculating_money():
    quarters_entered = int(input("How many quarters? "))
    quarters_entered *= quarters

    dimes_entered = int(input("How many dimes? "))
    dimes_entered *= dimes

    nickles_entered = int(input("How many nickles? "))
    nickles_entered *= nickles

    pennies_entered = int(input("How many pennies? "))
    pennies_entered *= pennies

    amount_entered = quarters_entered + dimes_entered + nickles_entered + pennies_entered

    return amount_entered


def cost_of_product(coffee):
    cost = MENU[coffee]["cost"]
    return cost


def machine_report():
    for item in resources:
        if item == 'coffee':
            print(f"{item.capitalize()}: {resources[item]}g")
        else:
            print(f"{item.capitalize()}: {resources[item]}ml")

    for money in cash:
        print(f"{money.capitalize()}: ${cash[money]}")


def change_calc(order_param, total_coins_param):
    cost = cost_of_product(order_param)
    total_coins_param = round_number(total_coins_param)


    if total_coins_param >= cost:
        cash["money"] += cost
        change = round_number(total_coins_param - cost)
        print(f"Total money received is ${total_coins_param}")
        print(f"Here is ${change} in change.")
        print(f"Here is your {order_param}. Enjoy!")
        resources_used(coffee_param=order_param)
    else:
        print(f"Sorry ${total_coins_param} is not enough money. Money refunded.")
        

def resources_used(coffee_param):
    for coffee in MENU:
        if coffee == coffee_param:
            for resource in resources:
                if resources[resource] >= MENU[coffee_param]['ingredients'][resource]:
                    resource_left = resources[resource] - MENU[coffee_param]['ingredients'][resource]
                    resources[resource] = resource_left
            return resources[resource]
        

def resources_check(coffee_param):
    keep_ordering = False
    for coffee in MENU:
        if coffee == coffee_param:
            for resource in resources:
                if resources[resource] < MENU[coffee_param]['ingredients'][resource]:
                    print(f"Sorry there is not enough {resource} left.")
                    return end_program(keep_ordering_param=keep_ordering)
                    # return


def end_program(keep_ordering_param):
    keep_ordering_param = False
    return keep_ordering_param


def coffee_machine():
    order_coffee = True
    while order_coffee:
        order = input("What would you like? (espresso/latte/cappuccino): ").lower()
        if order == 'report':
            machine_report()
        elif order == 'off':
            print("Coffee machine has been turned off. Have a good day!")
            order_coffee = False
        else:
            if resources_check(coffee_param=order) == False:
                return
            print("Please insert coins.")
            total_coins = calculating_money()
            change_calc(order_param=order, total_coins_param=total_coins)



coffee_machine()