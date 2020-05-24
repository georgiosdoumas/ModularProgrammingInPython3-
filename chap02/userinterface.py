#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

"""
import datastorage

def prompt_for_action():
    while True:
        print()
        print("What would you like to do? Type the letter for the coresponding action:")
        print()
        print(" A = add an item to the inventory.")
        print(" R = remove an item from the inventory.")
        print(" C = generate a report of the current inventory levels.")
        print(" O = generate a report of the inventory items to re-order.")
        print(" Q = quit.")
        print()
        action = input("> ").strip().upper()
        if action == "A": return "ADD"
        elif action == "R": return "REMOVE"
        elif action == "C": return "INVENTORY_REPORT"
        elif action == "O": return "REORDER_REPORT"
        elif action == "Q": return "QUIT"
        else:
            print(action, "Unknown action!")
            
def prompt_for_product():
    while True:
        print("\n Select a product-number from the following table:\n")
        np = 1
        for prod_code, description, desired_number in datastorage.products():
            print(" {}. {} - {}".format(np, prod_code, description))
            np = np + 1
        s = input("> ").strip()
        if s == "": return None
        try:
            np = int(s)
        except ValueError:
            np = -1    # to flag a bad user input 
        if np < 1 or np > len(datastorage.products()): # user either typed Enter or gave a non-existence product code
            print("Invalid option: {}".format(s))
            continue
        product_code = datastorage.products()[np-1][0]
        return product_code
    
def prompt_for_location():
    while True:
        print("\n Select a location number from the following table:\n")
        nl = 1
        for loc_code, description in datastorage.locations():
            print(" {}. {} - {}".format(nl, loc_code, description))
            nl = nl + 1
        s = input("> ").strip()
        if s == "": return None
        try:
            nl = int(s)
        except ValueError:
            nl = -1  # to flag a bad user input 
        if nl < 1 or nl > len(datastorage.locations()):
            print("Invalid option: {}".format(s))
            continue
        location_code = datastorage.locations()[nl-1][0]
        return location_code

def show_report(report):
    print('------------')
    for line in report:
        print(line)
    print('------------')
    
def show_error(err_msg):
    print("\n", err_msg, "\n")
