# Mini MVC Product Catalogue

A beginner-friendly console application built with pure Python. It uses the MVC pattern and saves product data in a JSON file.

## Requirements

- Python 3
- No external packages are required

## Project files

- `model.py` contains the `Product` class and `ProductRepository`.
- `view.py` formats product lists and messages for display.
- `controller.py` handles commands and validates product input.
- `app.py` starts the program and logs each command.
- `products.json` stores product data. The program creates this file the first time it runs.

## How to run

Open a terminal in this folder and run:

    python app.py

## Commands

### List products

Enter:

    list_products

The program displays all products in a table.

### Add a product

Enter:

    add_product

The program asks for a product name and price.

- The product name cannot be empty.
- The price must be a number greater than zero.
- The new product is saved in `products.json`.

### Exit

Enter:

    exit

## Request lifecycle

    User enters a command
            |
            v
    Logging middleware logs the command
            |
            v
    Controller handles the command
       |                 |
       v                 v
    Model reads      View formats
    or saves data    the result
       |                 |
       +--------+--------+
                |
                v
        App displays the result

## Example

    Product Catalogue
    Commands: list_products, add_product, exit
    Enter command: add_product
    [LOG] 12:05:31 add_product
    Product name: Headphones
    Product price: 899
    Product added: Headphones (ID: 3, Price: 899.00)

## Submission checklist

- Include `model.py`, `view.py`, `controller.py`, `app.py`, and `README.md`.
- Include `products.json` after running the program.
- Include a screenshot showing the program running and a product being added.