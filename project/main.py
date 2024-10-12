from models import User, Admin, Customer, BankAccount

if __name__ == "__main__":
   print("In main function")
   # This will now walk through a customer logging in and buying an item
   
   # The customer creates an account:
   new_user = User("John Customer", "John Customer", "password123", "john@gmail.com")
   
   # The customer logs in:
   # Incorrect password
   new_user.login("password124")
   
   # Correct password
   new_user.login("password123")
   
   # Logout
   new_user.logout()
   
else:
   print("Not in main function")