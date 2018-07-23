# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import random


balance = 500000
balance_history = []
BUY = True
SELL = False
trades_pairs_to_make = 100

def get_bitcoin_price():
    return random.randint(0,20000)

def trade (side, price, current_balance):
    x = 5
    if side:
        current_balance = current_balance - price
    else:
        current_balance = current_balance + price
    return current_balance


for n in range(0,trades_pairs_to_make):
    price = get_bitcoin_price()
    balance = trade(BUY, price, balance)
    balance_history.append(balance)
    price = get_bitcoin_price()
    balance = trade(SELL, price, balance)
    balance_history.append(balance)
    

print ('Trades made', trades_pairs_to_make *2)
print(balance_history)


        
        



