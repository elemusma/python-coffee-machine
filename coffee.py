from data import MENU, resources, cash


# amount_paid = 0
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
    # print(f"{cash['money'].capitalize()}: {resources[item]}ml")
    for money in cash:
        print(f"{money.capitalize()}: ${cash[money]}")


def change_calc(order_param, total_coins_param):
    cost = cost_of_product(order_param)
    total_coins_param = round_number(total_coins_param)
    cash["money"] += cost
    
    if total_coins_param >= cost:
        change = round_number(total_coins_param - cost)
        print(f"Total money received is ${total_coins_param}")
        print(f"Here is ${change} in change.")
        print(f"Here is your {order_param}. Enjoy!")
    else:
        print(f"Sorry ${total_coins_param} is not enough money. Money refunded.")


def resources_used(coffee_param):
    for coffee in MENU:
        print(coffee)
        for resource in resources:
            # if coffee != 'espresso':
            print(f"{resource} left: {resources[resource]}")
            print(f"{coffee_param} used: {MENU[coffee_param]['ingredients'][resource]}")
            # print(resource)
            # print(coffee)
    # water = MENU[coffee]["ingredients"]["water"]
    # print(water)
    # return cost


def coffee_machine(order_param):
    if order_param == 'report':
        change_calc(order_param,0)
    else:
        print("Please insert coins.")
        total_coins = calculating_money()
        change_calc(order_param=order_param, total_coins_param=total_coins)


# print(cash['money'])
print(resources_used("latte"))
# espresso = list(MENU.keys())[0]
# print(MENU["espresso"]["cost"])
# print(resources["money"])
# print(cost_of_product("espresso"))
# machine_report()

# keep_ordering = True
# while keep_ordering:
#     order = input("What would you like? (espresso/latte/cappuccino): ").lower()
#     if order == 'off':
#         print("Coffee machine has been turned off. Have a good day!")
#         keep_ordering = False
#     elif order == 'report':
#         machine_report()
#     else:
#         coffee_machine(order_param=order)