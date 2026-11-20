def format_products(products):  # Format product data for display.
    if not products:
        return "No products found."  # Show a message when the list is empty.
    lines = []
    lines.append("ID   Name                 Price")
    lines.append("-----------------------------------")
    for product in products:
        line = (
            f"{product.product_id:<4} "
            f"{product.name:<20} "
            f"{product.price:.2f}"
        )
        lines.append(line)
    return "\n".join(lines)  # Combine the table rows into one string.

def format_added_product(product):  # Format the new-product message.
    return (
        f"Product added: {product.name} "
        f"(ID: {product.product_id}, Price: {product.price:.2f})"
    )

def format_message(message):
    return message
