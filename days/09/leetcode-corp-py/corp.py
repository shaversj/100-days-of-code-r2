# A restaurant ordering system accepts food orders one item at a time. Each item entered is for a specific person sitting at a particular table.
# The kitchen is not concerned with which person ordered which item. They just need to know what menu items have been ordered for each table.
# Write a program that will read a list of individual orders and "pivot" that set into a display of food items for each table in the diner. The total number of each item per table will be displayed on a column for that food item.
# For example, the orders:
# Sarah,7,Green Salad
# Sarah,7,Cappuccino
# Michael,2,Club Sandwich
# Marcus,5,Sparkling Water
#
# Would be displayed for the kitchen as:
#     Table,Cappuccino,Club Sandwich,Green Salad,Sparkling Water
# 2,0,1,0,0
# 5,0,0,0,1
# 7,1,0,1,0
#
# Note that the menu items are listed in alphabetical order across the overall list.
# Input:
# A comma-delimited list of names, table numbers, and menu items.
# Output:
# A comma-delimited list of table numbers and item counts with a header row as the first line. The first column name is "Table".

FOOD_TABLE = {"Cappuccino": 0, "Club Sandwich": 1, "Green Salad": 2, "Sparkling Water": 3}

def load_orders():
    orders = []
    with open("input.txt") as f:
        for line in f:
            l = line.strip().split(",")
            orders.append(l)

    return orders


def pivot_orders_to_food_items(list_of_orders):
    order_table = {}

    # populate dictionary
    for order in list_of_orders:
        if int(order[1]) not in order_table:
            order_table[int(order[1])] = [0, 0, 0, 0]

        order_table[int(order[1])][FOOD_TABLE.get(order[2])] += 1

    return order_table


def format_food_items(food_items):

    header = ["Table", "Cappuccino", "Club Sandwich", "Green Salad", "Sparkling Water"]

    for entry in header:
        print(entry, end=",")

    print()

    for k, v in food_items.items():
        print(f"  {k},       {v[0]},         {v[1]},           {v[2]},         {v[3]}")


format_food_items(pivot_orders_to_food_items(load_orders()))
