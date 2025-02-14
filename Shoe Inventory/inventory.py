class Shoe:
    def __init__(self, country, code, product, cost, quantity):
        """
        Create a Shoe object with basic details.

        Parameters:
        - country: The country where the shoe is made.
        - code: A unique identifier for the shoe.
        - product: The name of the shoe product.
        - cost: The price of the shoe.
        - quantity: How many of this shoe are in stock.
        """
        self.country = country
        self.code = code
        self.product = product
        self.cost = float(cost)
        self.quantity = int(quantity)

    def get_cost(self):
        """Return the price of the shoe."""
        return self.cost

    def get_quantity(self):
        """Return the number of this shoe in stock."""
        return self.quantity

    def __str__(self):
        """Return a string that shows details about the shoe."""
        return f"Country: {self.country}, Code: {self.code}, \
Product: {self.product}, Cost: {self.cost}, Quantity: {self.quantity}"


# List to keep track of all the shoes in the program.
shoe_list = []


def read_shoes_data():
    """Read shoe data from a file and add to the shoe list."""
    try:
        with open("inventory.txt", "r") as file:
            '''Use next to skip the first line,
            which has the headers of the columns.'''
            next(file)
            for line in file:
                data = line.strip().split(",")
                # Make sure we have all required data.
                if len(data) == 5:
                    country, code, product, cost, quantity = data
                    shoe_list.append(Shoe(country, code, product, cost, quantity))
    except FileNotFoundError:
        print("Error: 'inventory.txt' file not found.")
    except Exception as e:
        print(f"Error: {e}")


def capture_shoes():
    """Get new shoe details from the user and add it to the list."""
    shoe = Shoe(
        input("Enter country: "),
        input("Enter code: "),
        input("Enter product: "),
        input("Enter cost: "),
        input("Enter quantity: ")
    )
    shoe_list.append(shoe)
    print("Shoe added successfully.")


def view_all():
    """Show all the shoes in the shoe list."""
    if shoe_list:
        for shoe in shoe_list:
            # Returning the shoes in a user-friendly manner.
            print("\n_________________________________________")
            print(f"Country: {shoe.country}\n")
            print(f"Code: {shoe.code}\n")
            print(f"Product: {shoe.product}\n")
            print(f"Cost: {shoe.cost}\n")
            print(f"Quantity: {shoe.quantity}")
            print("_________________________________________\n")
    else:
        print("No shoes in inventory.")


def re_stock():
    """Find the shoe with the lowest stock and allow the user to add more."""
    if not shoe_list:
        print("No shoes available.")
        return

    # Find the shoe with the lowest quantity.
    lowest_qty_shoe = shoe_list[0]
    for shoe in shoe_list[1:]:
        if shoe.get_quantity() < lowest_qty_shoe.get_quantity():
            lowest_qty_shoe = shoe

    print(f"Lowest quantity shoe:\n{lowest_qty_shoe}")

    try:
        additional_qty = int(input("Enter additional quantity: "))
        # Update the quantity.
        lowest_qty_shoe.quantity += additional_qty
        print(f"Updated quantity: {lowest_qty_shoe.quantity}")
        # Save changes to the file.
        update_inventory_file()
    except ValueError:
        print("Invalid quantity.")


def search_shoe():
    """Look for a shoe by its code and display its details."""
    code = input("Enter the shoe code: ")
    for shoe in shoe_list:
        if shoe.code == code:
            # Returning shoe in a user-friendly manner.
            print("\n_________________________________________")
            print(f"Country: {shoe.country}\n")
            print(f"Code: {shoe.code}\n")
            print(f"Product: {shoe.product}\n")
            print(f"Cost: {shoe.cost}\n")
            print(f"Quantity: {shoe.quantity}")
            print("_________________________________________\n")
            return
    print("Shoe not found.")


def value_per_item():
    """Calculate and display the total value of each shoe in stock."""
    for shoe in shoe_list:
        value = shoe.get_cost() * shoe.get_quantity()
        print(f"{shoe.product}: Value = {value}")


def highest_qty():
    """Find and show the shoe with the most stock."""
    if not shoe_list:
        print("No shoes available.")
        return

    '''Start with the first shoe as the highest quantity,
    then check each shoe in the list.'''
    highest_qty_shoe = shoe_list[0]
    for shoe in shoe_list[1:]:
        if shoe.get_quantity() > highest_qty_shoe.get_quantity():
            highest_qty_shoe = shoe

    print(f"Shoe with the highest quantity (For Sale):\n{highest_qty_shoe}")


def update_inventory_file():
    """Write the current shoe data back to the file."""
    try:
        with open("inventory.txt", "w") as file:
            '''Save the shoe details to the file,
            starting with the column names.'''
            file.write("Country,Code,Product,Cost,Quantity\n")
            for shoe in shoe_list:
                file.write(f"{shoe.country},{shoe.code},{shoe.product},\
{shoe.cost},{shoe.quantity}\n")
    except Exception as e:
        print(f"Error updating file: {e}")


def menu():
    """Display the main menu and let the user choose an option from (1-8)."""
    while True:
        print("\n--- Main Menu ---")
        print("1. Read shoe data")
        print("2. Capture new shoe")
        print("3. View all shoes")
        print("4. Restock a shoe")
        print("5. Search for a shoe")
        print("6. Calculate value per item")
        print("7. Find shoe with highest quantity (For Sale)")
        print("8. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            read_shoes_data()
            print("Shoe data has been successfully read.")
        elif choice == '2':
            capture_shoes()
            print("New shoe has been captured successfully.")
        elif choice == '3':
            view_all()
        elif choice == '4':
            re_stock()
            print("Stock updated successfully.")
        elif choice == '5':
            search_shoe()
        elif choice == '6':
            value_per_item()
        elif choice == '7':
            highest_qty()
        elif choice == '8':
            print("Exiting the Main Menu, Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


# Start the program
menu()
