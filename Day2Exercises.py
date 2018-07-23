# -*- coding: utf-8 -*-
"""
Created on Sat Jul 21 11:14:46 2018

@author: Me
"""



rentals = {'1a':'200', '1b':'100', '2c':'120'}

def show_rentals():
    for a, r in rentals.items():
        print (a, ":", r)

def add_rental(rentals, apt:rent):
    rentals.update({apt : rent})

def delete_rental(rentals, apt):
    del rentals[apt]
    return rentals

def show_menu():
    print(1."View all Rentals")
    print(2."Add")
    print(3. "Delete")
    print(4."Exit")
    

while True:
    show menu()
    selection = int(input("Pick: ")
    if selection == 1:
        show rental()
    elif selection == 2:
        apt = input ("What appt?")
        rental = int (input("What rent?))
        add_rental(rentals, apt : rent)
    elif selection == 3:
        apt = input ("What apt you want removed?")
        rentals = delete_rental(rentals, apt)
    elif selection == 4:
        exit()