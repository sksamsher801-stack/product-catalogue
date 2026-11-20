from model import validate_product_name, validate_product_price  # Reuse the model validation rules.
from view import format_added_product, format_message, format_products  # Reuse the view formatting functions.

class ProductController:
    def __init__(self, repository):
        self.repository = repository
    def handle_command(self, command):  # Route each user command to the right action.
        if not isinstance(command, str):
            return format_message("Command must be text.")
        command = command.strip().lower()  # Clean the command before checking it.
        if command == "":
            return format_message("Command cannot be empty.")
        if command == "list_products":
            try:
                products = self.repository.get_all_products()  # Ask the model to load saved products.
                return format_products(products)  # Ask the view to format the product list.
            except (OSError, ValueError) as error:
                return format_message(f"Could not load products: {error}")
        elif command == "add_product":
            return self.add_product()
        elif command == "exit":
            return format_message("Goodbye!")
        else:
            return format_message("Unknown command. Type list_products, add_product, or exit.")

    def add_product(self):  # Get, validate, and save a new product.
        while True:
            name_input = input("Product name: ")  # Ask the user for a product name.
            try:
                name = validate_product_name(name_input)  # Reject empty or numeric-only names.
                break
            except ValueError as error:
                print(error)
        while True:
            price_input = input("Product price: ")  # Ask the user for a product price.
            try:
                price = validate_product_price(price_input)  # Check and convert the price.
                break
            except ValueError as error:
                print(error)
        try:
            product = self.repository.add_product(name, price)  # Save the new product through the model.
            return format_added_product(product)
        except (OSError, ValueError) as error:
            return format_message(f"Could not save product: {error}")
