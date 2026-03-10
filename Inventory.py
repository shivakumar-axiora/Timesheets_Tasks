# Data Structures
product_ids = []          # List
categories = set()        # Set
inventory = {}            # Nested Dictionary


def add_product():
    pid = input("Enter Product ID: ").strip()

    # Edge Case: Duplicate ID
    if pid in inventory:
        print("Error: Product ID already exists.")
        return

    name = input("Enter Product Name: ").strip()
    category = input("Enter Product Category: ").strip()

    # Edge Case: Empty fields
    if not name or not category:
        print("Error: Name and Category cannot be empty.")
        return

    try:
        quantity = int(input("Enter Quantity: "))
        price = float(input("Enter Price: "))

        # Edge Case: Negative values
        if quantity < 0 or price < 0:
            print("Error: Quantity and Price must be positive.")
            return

    except ValueError:
        print("Error: Quantity must be integer and Price must be number.")
        return

    # Tuple (immutable product info)
    product_info = (name, category)

    # Store data
    product_ids.append(pid)
    categories.add(category)

    # Nested Dictionary
    inventory[pid] = {
        "info": product_info,
        "stock": {
            "quantity": quantity,
            "price": price
        }
    }

    print("Product added successfully.")


def view_inventory():
    if not inventory:
        print("Inventory is empty.")
        return

    for pid, details in inventory.items():

        name, category = details["info"]
        quantity = details["stock"]["quantity"]
        price = details["stock"]["price"]

        print("\nID:", pid)
        print("Name:", name)
        print("Category:", category)
        print("Quantity:", quantity)
        print("Price:", price)


def update_stock():
    pid = input("Enter Product ID to update: ")

    if pid not in inventory:
        print("Product not found.")
        return

    try:
        new_qty = int(input("Enter new quantity: "))

        if new_qty < 0:
            print("Quantity cannot be negative.")
            return

    except ValueError:
        print("Invalid quantity.")
        return

    # Nested dictionary manipulation
    inventory[pid]["stock"]["quantity"] = new_qty

    print("Stock updated successfully.")


def delete_product():
    pid = input("Enter Product ID to delete: ")

    if pid not in inventory:
        print("Product does not exist.")
        return

    # Remove from dictionary
    del inventory[pid]

    # Remove from list
    if pid in product_ids:
        product_ids.remove(pid)

    print("Product deleted.")


def search_product():
    pid = input("Enter Product ID: ")

    if pid not in inventory:
        print("Product not found.")
        return

    details = inventory[pid]

    name, category = details["info"]
    quantity = details["stock"]["quantity"]
    price = details["stock"]["price"]

    print("\nProduct Found")
    print("Name:", name)
    print("Category:", category)
    print("Quantity:", quantity)
    print("Price:", price)


def show_categories():
    if not categories:
        print("No categories available.")
    else:
        print("Categories:", categories)


def menu():
    while True:
        print("\n----- Inventory System -----")
        print("1 Add Product")
        print("2 View Inventory")
        print("3 Update Stock")
        print("4 Delete Product")
        print("5 Search Product")
        print("6 Show Categories")
        print("7 Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_product()
        elif choice == "2":
            view_inventory()
        elif choice == "3":
            update_stock()
        elif choice == "4":
            delete_product()
        elif choice == "5":
            search_product()
        elif choice == "6":
            show_categories()
        elif choice == "7":
            print("Exiting...")
            break
        else:
            print("Invalid choice.")

menu()