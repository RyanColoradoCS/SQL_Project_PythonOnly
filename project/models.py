# Initialize globals
user_id = 0
account_id = 0
email_id = 0
product_id = 0
transaction_id = 0
email_id_counter = 0
receipt_id = 0

# Base User Class
class User:
    """Base class for users on the website"""
    
    def __init__(self, username, name, password, email):
        global user_id  # Declare the global user_id
        user_id += 1
        self.user_id = user_id
        self.username = username
        self.name = name
        self.password = self._hash_password(password)
        self.email = email
        self.admin_status = False
        self.logged_in = False

    '''
    Note:
    double underscore (__) in Python for method or variable names signifies a form 
    of name mangling that changes the way the attribute is accessed to make it less 
    accessible from outside the class
    '''
    def _hash_password(self, password):
        # Hash the password for security purposes
        # Using a placeholder hash here
        return f"hashed_{password}"

    def login(self, password):
        if self._hash_password(password) == self.password:
            self.logged_in = True
            print(f"User {self.username} is now logged in.")
        else:
            print(f"Incorrect password for user {self.username}.")
    
    def logout(self):
        self.logged_in = False
        print(f"User {self.username} is now logged out.")

# Admin Class
class Admin(User):
    """Admin account for the website"""
    def __init__(self, username, name, password, email):
        super().__init__(username, name, password, email)
        self.admin_status = True

    # this will have admin rights and functions added later
    
# Customer Class
class Customer(User):
    """Customer account for the website"""

    def __init__(self, username, name, password, email, physical_address):
        super().__init__(username, name, password, email)
        self.physical_address = physical_address
        self.bank_account = None
        self.transactions = [] # user can have multiple transactions

    def set_bank_account(self, new_bank_account):
        """Assign or update the customer's bank account."""
        if self.bank_account is None:
            print(f"Assigned new bank account {new_bank_account.account_number} to {self.name}.")
        else:
            print(f"Updated bank account to {new_bank_account.account_number} for {self.name}.")
        self.bank_account = new_bank_account
        
    def remove_bank_account(self):
        """Remove the bank account from the customer."""
        if self.bank_account is None:
            raise Exception("This customer has no bank account to remove.")
        else:
            removed_account = self.bank_account  # Store for message
            self.bank_account = None  # Clear the bank account
            print(f"Removed bank account {removed_account.account_number} for {self.name}.")

    def add_transaction(self, transaction):
        """Add a transaction to the customer"""
        if transaction not in self.transactions:
            print(f"Added transaction {transaction.transaction_id} for {self.name}.")
            self.transactions.append(transaction)
        else:
            print(f"Unable to add transaction id: {transaction.transaction_id} because it already exists for {self.name}.")

    def print_transactions(self):
        print(f"Printing all transactions for {self.name}:")
        for transaction in self.transactions:
            print(f"Transaction ID: {transaction.transaction_id}, "
                f"Type: {transaction.transaction_type}, "
                f"Product: {transaction.product.name}")

        
class BankAccount:
    def __init__(self, user, bank_name, account_number):
        if user is None:
            raise ValueError("User cannot be None")
        
        global account_id  # Declare the global account_id
        account_id += 1

        self.user = user
        self.bank_name = bank_name
        self.account_number = account_number

class TransactionEmail:
    """Email class to manage email sending."""
    
    def __init__(self, user, transaction, email_content):

        if user is None:
            raise ValueError("User cannot be None")
        if transaction is None:
            raise ValueError("Transaction cannot be None")

        global email_id
        email_id += 1
        self.email_id = email_id  # Assign to the instance
        
        self.user = user  # Store the User object
        self.transaction = transaction # Store the Transaction object
        self.email_content = email_content

    def send_email(self):
        # Use the user object to send the email
        print(f"Sending email to {self.user.email} about transaction {self.transaction.transaction_id}")
        print(f"Content: {self.email_content}")

class Product:
    def __init__(self, name, manufacturer, product_type, price, shipping_cost, labor_overhead):
        
        global product_id
        product_id += 1
        self.product_id = product_id
        
        self.name = name
        self.manufacturer = manufacturer
        self.product_type = product_type
        self.price = price
        self.shipping_cost = shipping_cost
        self.labor_overhead = labor_overhead
        
    def __str__(self):
        return f"Product {self.product_id}: {self.name} ({self.product_type}) by {self.manufacturer}"

class Transaction:
    def __init__(self, user, product, transaction_type):
        
        if product is None:
            raise ValueError("Product cannot be None.")
        if user is None:
            raise ValueError("User cannot be None.")

        global transaction_id
        transaction_id += 1
        self.transaction_id = transaction_id  # Assign to the instance

        self.user = user
        self.product = product
        self.transaction_type = transaction_type
        # Add this transaction instance to the user's transactions list
        self.user.add_transaction(self)

    def process_transaction(self):
        print(f"Processing transaction id {self.transaction_id} type {self.transaction_type} "
            f"for {self.product.name} for user {self.user.name}")

class Receipt:
    def __init__(self, transaction, user):
        
        if transaction is None:
            raise ValueError("Transaction cannot be None.")
        if user is None:
            raise ValueError("User cannot be None.")
        if transaction.user != user:
            raise ValueError("Transaction user does not match the provided user.")
        
        global receipt_id
        receipt_id += 1
        self.receipt_id = receipt_id
        
        self.transaction = transaction
        self.user = user
        
    def generate_receipt(self):
        print(f"Receipt #{self.receipt_id} for transaction {self.transaction.transaction_id}")

        