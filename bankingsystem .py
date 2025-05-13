import random
import datetime
import json
import os

accounts_file = "accounts.json"

admin_username = "admin"
admin_password = "admin123

def load_accounts():
    """Load accounts from a JSON file."""
    if os.path.exists(accounts_file):
        with open(accounts_file, "r") as file:
            return json.load(file)
    return {}
def save_accounts():
    """Save accounts data to a JSON file."""
    with open(accounts_file, "w") as file:
        json.dump(accounts, file, indent=4)

accounts = load_accounts()

def admin_login():
    """Admin login function."""
    print("\n===== Admin Login =====")
    username = input("Enter admin username: ").strip()
    password = input("Enter admin password: ").strip()
    
    if username == admin_username and password == admin_password:
        print("\nLogin successful!")
        return True
    else:
        print("\nInvalid credentials. Access denied.")
        return False
# TESTING 
def generate_account_number():
    """Generate a unique 8-digit account number"""
    while True:
       
        account_number = str(random.randint(10000000, 99999999))

        if account_number not in accounts:
            return account_number

def create_account():
    """Function to create a new bank account"""
    print("\n===== Create New Account =====")
    
    while True:
        name = input("Enter account holder name: ").strip()
        if name:
            break
        print("Name cannot be empty. Please try again.")
    
   while True:
        adress = input("Enter account holder adress: ").strip()
        if adress:
            break
        print("Adress cannot be empty. Please try again.")
       
    while True:
        try:
            initial_balance = float(input("Enter initial deposit amount: $"))
            if initial_balance < 0:
                print("Initial balance cannot be negative. Please try again.")
            else:
                break
        except ValueError:
            print("Please enter a valid amount.")
    
    account_number = generate_account_number()
    
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    accounts[account_number] = {
        "holder_name": name,
        "balance": initial_balance,
        "transactions": []
    }
    
    if initial_balance > 0:
        accounts[account_number]["transactions"].append({
            "type": "deposit",
            "amount": initial_balance,
            "timestamp": timestamp,
            "description": "Initial deposit"
        })
    
    print(f"\nAccount created successfully!")
    print(f"Account Number: {account_number}")
    print(f"Account Holder: {name}")
    print(f"Initial Balance: ${initial_balance:.2f}")
    
    save_accounts()  
    return account_number

def deposit_money():
    """Function to deposit money into an account"""
    print("\n===== Deposit Money =====")
    
    account_number = input("Enter account number: ").strip()
    
    if account_number not in accounts:
        print("Account not found. Please check the account number.")
        return
    
    while True:
        try:
            amount = float(input("Enter deposit amount: $"))
            if amount <= 0:
                print("Deposit amount must be positive. Please try again.")
            else:
                break
        except ValueError:
            print("Please enter a valid amount.")
    
    accounts[account_number]["balance"] += amount
    
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    accounts[account_number]["transactions"].append({
        "type": "deposit",
        "amount": amount,
        "timestamp": timestamp,
        "description": "Regular deposit"
    })
    print(f"\nDeposit successful!")
    print(f"Deposited: ${amount:.2f}")
    print(f"New Balance: ${accounts[account_number]['balance']:.2f}")
    
    save_accounts()  
    
def withdraw_money():
    """Function to withdraw money from an account"""
    print("\n===== Withdraw Money =====")
    
    account_number = input("Enter account number: ").strip()
    
    if account_number not in accounts:
        print("Account not found. Please check the account number.")
        return
    
    while True:
        try:
            amount = float(input("Enter withdrawal amount: $"))
            if amount <= 0:
                print("Withdrawal amount must be positive. Please try again.")
            elif amount > accounts[account_number]["balance"]:
                print(f"Insufficient funds. Your current balance is ${accounts[account_number]['balance']:.2f}")
            else:
                break
        except ValueError:
            print("Please enter a valid amount.")
    
    accounts[account_number]["balance"] -= amount
    
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    accounts[account_number]["transactions"].append({
        "type": "withdrawal",
        "amount": amount,
        "timestamp": timestamp,
        "description": "Regular withdrawal"
    })
    
    print(f"\nWithdrawal successful!")
    print(f"Withdrawn: ${amount:.2f}")
    print(f"New Balance: ${accounts[account_number]['balance']:.2f}")

    save_accounts()  

def check_balance():
    """Function to check the balance of an account"""
    print("\n===== Check Balance =====")
    
    account_number = input("Enter account number: ").strip()
    
    if account_number not in accounts:
        print("Account not found. Please check the account number.")
        return
    
    print(f"\nAccount Number: {account_number}")
    print(f"Account Holder: {accounts[account_number]['holder_name']}")
    print(f"Current Balance: ${accounts[account_number]['balance']:.2f}")

def view_transaction_history():
    """Function to view transaction history of an account"""
    print("\n===== Transaction History =====")
    
    account_number = input("Enter account number: ").strip()
    
    if account_number not in accounts:
        print("Account not found. Please check the account number.")
        return
    
    transactions = accounts[account_number]["transactions"]
    
    if not transactions:
        print("\nNo transactions recorded for this account.")
        return
    
    print(f"\nAccount Number: {account_number}")
    print(f"Account Holder: {accounts[account_number]['holder_name']}")
    print(f"Current Balance: ${accounts[account_number]['balance']:.2f}")

    print("\nTransaction History:")
    print("-" * 80)
    print("| Type       | Amount      | Date & Time           | Description        |")
    print("-" * 80)
    
    for transaction in transactions:
        transaction_type = transaction["type"].capitalize()
        amount = f"${transaction['amount']:.2f}"
        timestamp = transaction["timestamp"]
        description = transaction["description"]
        
        print(f"| {transaction_type:<10} | {amount:<11} | {timestamp:<21} | {description:<18} |")
    
    print("-" * 80)

def transfer_money():
    """Bonus function to transfer money between accounts"""
    print("\n===== Transfer Money =====")
    
    from_account = input("Enter source account number: ").strip()
    
    if from_account not in accounts:
        print("Source account not found. Please check the account number.")
        return
    
    to_account = input("Enter destination account number: ").strip()
    
    if to_account not in accounts:
        print("Destination account not found. Please check the account number.")
        return
    
    if from_account == to_account:
        print("Source and destination accounts cannot be the same.")
        return
    
    while True:
        try:
            amount = float(input("Enter transfer amount: $"))
            if amount <= 0:
                print("Transfer amount must be positive. Please try again.")
            elif amount > accounts[from_account]["balance"]:
                print(f"Insufficient funds. Your current balance is ${accounts[from_account]['balance']:.2f}")
            else:
                break
        except ValueError:
            print("Please enter a valid amount.")
    
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    accounts[from_account]["balance"] -= amount
    accounts[from_account]["transactions"].append({
        "type": "transfer out",
        "amount": amount,
        "timestamp": timestamp,
        "description": f"Transfer to {to_account}"
    })
    
    accounts[to_account]["balance"] += amount
    accounts[to_account]["transactions"].append({
        "type": "transfer in",
        "amount": amount,
        "timestamp": timestamp,
        "description": f"Transfer from {from_account}"
    })
    
    print(f"\nTransfer successful!")
    print(f"Transferred: ${amount:.2f} from {from_account} to {to_account}")
    print(f"New Balance (source account): ${accounts[from_account]['balance']:.2f}")
      
    save_accounts()
    
def display_menu():
    """Function to display the menu"""
    print("\n" + "=" * 40)
    print("   BANK OF LANKA BANKING APPLICATION")
    print("=" * 40)
    print("1. Create Account")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Check Balance")
    print("5. Transaction History")
    print("6. Transfer Money (Bonus)")
    print("7. Exit")
    print("=" * 40)

def main():
    """Main function to run the banking application"""
    print("Welcome to the Bank Of Lanka!")
    
    attempts = 3
    while attempts > 0:
        if admin_login():
            break
        attempts -= 1
        print(f"Attempts remaining: {attempts}")
    else:
        print("Too many failed attempts. Exiting.")
        return
    while True:
        display_menu()
        
        choice = input("Enter your choice (1-7): ").strip()
        
        if choice == "1":
            create_account()
        elif choice == "2":
            deposit_money()
        elif choice == "3":
            withdraw_money()
        elif choice == "4":
            check_balance()
        elif choice == "5":
            view_transaction_history()
        elif choice == "6":
            transfer_money()
        elif choice == "7":
            print("\nThank you for using the Bank Of Lanka. Goodbye!")
            break
        else:
            print("\nInvalid choice. Please try again.")
        
        input("\nPress Enter to continue...")

main()
