# Initialize globals
user_id = 0
account_id = 0
email_id = 0
product_id = 0
transaction_id = 0

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

# Customer Class
class Customer(User):
    """Customer account for the website"""

    def __init__(self, username, name, password, email, physical_address):
        super().__init__(username, name, password, email)
        self.physical_address = physical_address
        self.bank_account = None
        self.transactions = []

    def set_bank_account(self, bank_account):
        """Assign the bank account to the customer. Ensure only one account is allowed."""
        if self.bank_account is None:
            self.bank_account = bank_account
        else:
            raise Exception("This customer already has a bank account.")
    
    # This has not been updated yet
    def set_bank_account(self, new_bank_account):
        """Update bank account for the customer."""
        print(f"New account: {new_bank_account}")
        

    def add_transaction(self, transaction):
        """Add a transaction to the customer"""
        self.transactions.append(transaction)


class BankAccount:
    def __init__(self, user, bank_name, account_number):
        if user is None:
            raise ValueError("User cannot be None")
        
        global account_id  # Declare the global account_id
        account_id += 1
        self.account_id = account_id
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

        global email_id_counter
        self.email_id = email_id_counter
        email_id_counter += 1
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

class Transaction:
    def __init__(self, user, product, transaction_type):
        global transaction_id
        transaction_id = transaction_id
        self.user = user
        self.product = product
        self.transaction_type = transaction_type
        user.add_transaction(self)

    def process_transaction(self):
        print(f"Processing {self.transaction_type} for {self.product.name} for user {self.user.name}")

class Receipt:
    def __init__(self, receipt_id, transaction):
        self.receipt_id = receipt_id
        self.transaction = transaction

    def generate_receipt(self):
        print(f"Receipt #{self.receipt_id} for transaction {self.transaction.transaction_id}")

        