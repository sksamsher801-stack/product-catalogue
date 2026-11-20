from datetime import datetime
from controller import ProductController  # Import the command handler.
from model import ProductRepository  # Import the JSON-backed data store.

def logging_middleware(command, controller_function):  # Log a command before the controller runs.
    current_time = datetime.now().strftime("%H:%M:%S")
    print(f"[LOG] {current_time} {command}")  # Display the request log.
    return controller_function(command)  # Pass the command to the controller.

def main():
    repository = ProductRepository()  # Create the product data store.
    controller = ProductController(repository)  # Connect the controller to the data store.
    print("Product Catalogue")
    print("Commands: list_products, add_product, exit")
    while True:
        command = input("Enter command: ").strip().lower()
        if command == "":
            print("Command cannot be empty.")
            continue
        result = logging_middleware(command,controller.handle_command)  # Log the request, then handle it.
        print(result)
        if command == "exit":
            break

if __name__ == "__main__":  # Run the app only when this file is started directly.
    main()
