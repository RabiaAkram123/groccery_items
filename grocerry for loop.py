grocery_items = [
    ["banana", 100, "drgen"],  # [item, price, quantity]
    ["apple", 90, "1 kg"],
    ["soap", 50, "1 pack"],
    ["cream", 350, "1 pack"],
    ["mango", 70, "1 kg"],
    ["mobile", 1500, "1 piece"]
]

target = "cream"

for index, item in enumerate(grocery_items):  # Use enumerate to get index and item
    if item[0] == target:  # Check if the current item name matches the target
        name = item[0]  # Get the item name
        price = item[1]  # Get the price
        quantity = item[2]  # Get the quantity
        print(f"Found {name} at index {index}, price {price}, with quantity {quantity}")  # Print details
        break  # Exit the loop if found
