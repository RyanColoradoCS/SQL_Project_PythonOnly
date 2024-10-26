from models import User, Admin, Customer, BankAccount, Product, Transaction
from json_functions import *


if __name__ == "__main__":
   
    print("In main function...")

    # Step 1: Create some products
    product = Product("Laptop", "TechCorp", "Electronics", 1200, 50, 100)
    product2 = Product("Desktop", "TechCorp", "Electronics", 1200, 50, 100)

    # Convert product to dict and save to JSON
    product_data = product.to_dict()
    save_to_json(product_data, 'product_data.json')

    # Step 2: The customer creates an account
    new_user = Customer(
        username="johncustomer", 
        name="John Customer", 
        password="password123", 
        email="john@gmail.com", 
        physical_address="123 Main St"
    )
    print(f"Customer created: {new_user.name}, Email: {new_user.email}, Address: {new_user.physical_address}")

    # Convert user to dict and save to JSON
    user_data = new_user.to_dict()
    save_to_json(user_data, 'user_data.json')

    # Step 3: The customer logs in
    new_user.login("password124")  # Incorrect password
    new_user.login("password123")  # Correct password

    # Step 4: Create transaction(s) and store them in a list
    
    # List to hold all transactions in current session
    transactions = []

   # Buy a product (laptop)
    transaction1 = Transaction(new_user, product, "Purchase")
    transaction1.process_transaction()
    transactions.append(transaction1.to_dict())

   # Buy the product again
    transaction2 = Transaction(new_user, product, "Purchase")
    transaction2.process_transaction()
    transactions.append(transaction2.to_dict())

   # Buy the desktop
    transaction3 = Transaction(new_user, product2, "Purchase")
    transaction3.process_transaction()
    transactions.append(transaction3.to_dict())

    # Save all transactions to a JSON file
    save_to_json(transactions, 'transactions_data.json')

    # Step 5: Print all user transactions
    new_user.print_transactions()

    # Save all user data to JSON (including transactions)
    save_to_json(new_user.to_dict(), 'customer_data_with_transactions.json')

    # Step 6: The customer logs out
    new_user.logout()

    # Load data back from JSON files as needed
    loaded_user_data = load_from_json('user_data.json')
    if loaded_user_data:
        print(f"Loaded User Data: {loaded_user_data}")

    loaded_product_data = load_from_json('product_data.json')
    if loaded_product_data:
        print(f"Loaded Product Data: {loaded_product_data}")

    loaded_transaction_data = load_from_json('transaction_data.json')
    if loaded_transaction_data:
        print(f"Loaded Transaction Data: {loaded_transaction_data}")

else:
    print("Not in main function")
