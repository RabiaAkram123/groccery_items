# 🛒 Grocery Item Finder – Python Project

A simple yet practical Python script that searches for a specific grocery item within a list and retrieves its full details.

---

## 📘 Description

This project demonstrates basic Python programming concepts like:
- Lists of lists
- Looping with `enumerate()`
- Conditional checking
- Clean data extraction and output formatting

Each grocery item is stored as a list: `[item_name, price, quantity]`.

---

## 🔍 How It Works

- The script loops through the grocery list using `enumerate()` to keep track of item positions.
- It compares each item name with the target item.
- If a match is found, it prints the item’s name, price, quantity, and its index in the list.

---

## 📦 Sample Data

```python
grocery_items = [
    ["banana", 100, "drgen"],
    ["apple", 90, "1 kg"],
    ["soap", 50, "1 pack"],
    ["cream", 350, "1 pack"],
    ["mango", 70, "1 kg"],
    ["mobile", 1500, "1 piece"]
]
