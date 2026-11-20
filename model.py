import json  # Read and write JSON data.
import math  # Check whether prices are valid finite numbers.
import os  # Check whether the product file exists.

def validate_product_name(name):  # Validate a product name.
    if not isinstance(name, str):
        raise ValueError("Product name must be text.")
    name = name.strip()
    if name == "":
        raise ValueError("Product name cannot be empty.")
    try:
        float(name)  # Check whether the name contains only a number.
    except ValueError:
        return name
    else:
        raise ValueError("Product name cannot contain only a number.")

def validate_product_price(price):  # Validate and convert a product price.
    if isinstance(price, bool):
        raise ValueError("Price must be a number greater than zero.")
    try:
        price = float(price)  # Convert numeric text into a number.
    except (TypeError, ValueError):
        raise ValueError("Price must be a valid number.")
    if not math.isfinite(price):  # Reject NaN and infinity values.
        raise ValueError("Price must be a normal, finite number.")
    if price <= 0:
        raise ValueError("Price must be greater than zero.")
    return price

class Product:
    def __init__(self, product_id, name, price):
        if isinstance(product_id, bool) or not isinstance(product_id, int):
            raise ValueError("Product ID must be a whole number.")
        if product_id <= 0:
            raise ValueError("Product ID must be greater than zero.")
        self.product_id = product_id
        self.name = validate_product_name(name)
        self.price = validate_product_price(price)
    
    def to_dict(self):  # Prepare this product for JSON storage.
        return {
            "id": self.product_id,
            "name": self.name,
            "price": self.price,
        }

class ProductRepository:
    def __init__(self, file_name="products.json"):  # Set up the JSON storage file.
        self.file_name = file_name
        if not os.path.exists(self.file_name):  # Create starter data if the file is missing.
            sample_products = [
                Product(1, "Keyboard", 1299.00),
                Product(2, "Mouse", 499.00),
            ]
            self.save_products(sample_products)  # Save starter products to the JSON file.

    def get_all_products(self):  # Read and validate products from the file.
        try:
            with open(self.file_name, "r", encoding="utf-8") as file:  # Open the product file for reading.
                product_data = json.load(file)  # Load JSON data into Python objects.
        except json.JSONDecodeError as error:
            raise ValueError("products.json does not contain valid JSON.") from error

        if not isinstance(product_data, list):
            raise ValueError("Product data must be a list.")
        products = []
        for item in product_data:
            if not isinstance(item, dict):
                raise ValueError("Each product must be a JSON object.")
            if "id" not in item or "name" not in item or "price" not in item:
                raise ValueError("Every product needs id, name, and price.")
            product = Product(
                item["id"],
                item["name"],
                item["price"],
            )
            products.append(product)
        return products

    def save_products(self, products):  # Save products to the JSON file.
        if not isinstance(products, list):
            raise ValueError("Products must be provided as a list.")
        product_data = []
        for product in products:
            if not isinstance(product, Product):
                raise ValueError("Every item must be a Product.")
            product_data.append(product.to_dict())
        with open(self.file_name, "w", encoding="utf-8") as file:  # Open the file for writing.
            json.dump(product_data, file, indent=2)  # Write the product data as readable JSON.

    def add_product(self, name, price):  # Add a validated product and save it.
        name = validate_product_name(name)
        price = validate_product_price(price)
        products = self.get_all_products()  # Load existing products.
        new_id = 1
        for product in products:
            if product.product_id >= new_id:
                new_id = product.product_id + 1
        new_product = Product(new_id, name, price)
        products.append(new_product)
        self.save_products(products)  # Save the updated product list.
        return new_product  # Return the product that was added.
