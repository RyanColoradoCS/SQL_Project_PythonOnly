from models import User, Admin, Customer, BankAccount, Product, Transaction

if __name__ == "__main__":
   print("In main function")
   # This will now walk through a customer logging in and buying an item
   
   # create some products
   product = Product("Laptop", "TechCorp", "Electronics", 1200, 50, 100)
   
   # The customer creates an account:
   # Create a customer account
   new_user = Customer(
      username="johncustomer", 
      name="John Customer", 
      password="password123", 
      email="john@gmail.com", 
      physical_address="123 Main St"
   )

   print(f"Customer created: {new_user.name}, Email: {new_user.email}, Address: {new_user.physical_address}")

   # The customer logs in:
   # Incorrect password
   new_user.login("password124")
   
   # Correct password
   new_user.login("password123")
   

   # Create a test transaction
   transaction1 = Transaction(new_user, product, "Purchase")
   transaction1.process_transaction()

   # Try to add the same transaction again
   transaction2 = Transaction(new_user, product, "Purchase")
   transaction2.process_transaction()
   
   # print all user transactions
   new_user.print_transactions()
   
   # Logout
   new_user.logout()
   
else:
   print("Not in main function")