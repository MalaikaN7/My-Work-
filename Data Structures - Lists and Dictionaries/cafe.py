# List of menu items in the cafe.
menu = ["coffee", "tea", "scones", "doughnuts"]

# Dictionary to store the stock quantities for each menu item.
stock = {
    "coffee": 45,
    "tea": 30,
    "scones": 72,
    "doughnuts": 84
}

# Dictionary to store the prices for each menu item.
price = {
    "coffee": 22,
    "tea": 17,
    "scones": 7,
    "doughnuts": 14
}

# Start theh count of the variable total stock at 0.
total_stock = 0

# Loop through each item in the menu.
for item in menu:
    # Calculate the total value for each item (stock quantity * price).
    item_value = stock[item] * price[item]
    # Add the item's total value to the total stock value.
    total_stock += item_value

# Print the total worth of the stock in the cafe.
print(f"Total stock worth in the cafe is: R{total_stock}")
