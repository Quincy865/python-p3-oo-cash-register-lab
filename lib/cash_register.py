#!/usr/bin/env python3

import sys

class CashRegister:
    def __init__(self, discount=0):
        """
        Initializes a new CashRegister instance.
        Args:
            discount (int): Discount percentage to be applied (default is 0).
        """
        self.total = 0.0  # Total price of all items
        self.discount = discount  # Discount percentage
        self.items = []  # List to track items added to the register
        self.last_transaction = 0.0  # Keeps track of the most recent transaction

    def add_item(self, title, price, quantity=1):
        """
        Adds an item to the register.
        Args:
            title (str): The name of the item.
            price (float): Price per unit of the item.
            quantity (int): Number of units being added (default: 1).
        """
        self.total += price * quantity
        self.items.extend([title] * quantity)  # Track each item added
        self.last_transaction = price * quantity  # Record the value of the last transaction

    def apply_discount(self):
        """
        Applies the discount to the total and prints the result.
        If no discount is available, it prints an error message.
        """
        if self.discount > 0:
            discount_amount = (self.discount / 100) * self.total
            self.total -= discount_amount
            print(f"After the discount, the total comes to ${int(self.total)}.")
        else:
            print("There is no discount to apply.")

    def void_last_transaction(self):
        """
        Voids the last transaction by subtracting its value from the total.
        Resets the last transaction amount to 0.
        """
        self.total -= self.last_transaction
        self.last_transaction = 0.0
