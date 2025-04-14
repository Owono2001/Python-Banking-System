import datetime
import sys
import os # Needed for rename/remove
import shutil # More robust file moving/copying
CUSTOMER_DETAILS_FILE = "customer_details.txt"
ACCOUNTS_FILE = "accounts.txt" # Use .txt for consistency if desired

# For Getting Customer Login Details from the text file
def Customer_login_details():
    account_no = []  # List for saving Account NO
    password = []  # List for saving Password
    try:
        # Use 'with' for automatic file closing
        with open(CUSTOMER_DETAILS_FILE, 'r') as file1:
            for line in file1: # Iterate directly over the file object
                line = line.strip()
                if not line: # Skip empty lines
                    continue
                parts = line.split(' ')
                # Add checks for expected number of parts
                if len(parts) >= 6:
                    account_no.append(parts[4])
                    password.append(parts[5])
                else:
                    print(f"Warning: Skipping malformed line in {CUSTOMER_DETAILS_FILE}: {line}")
    except FileNotFoundError:
        print(f"Error: Customer details file '{CUSTOMER_DETAILS_FILE}' not found.")
        # Depending on requirements, you might want to exit or create the file
        # sys.exit(1)
    except Exception as e: # Catch other potential errors during processing
         print(f"An unexpected error occurred reading {CUSTOMER_DETAILS_FILE}: {e}")
         # Consider logging the full error for debugging

    return account_no, password


# Customer Menu Function
def Customer_menu(accound_no):
    while 1:
        print("\tMenu\n"
              "1 . Change Password\n"
              "2 . Deposits\n"
              "3 . Withdrawals\n"
              "4 . Balance\n"
              "5 . Report\n"
              "6 . Login")

        input_entry = input("Select one : ")
        if input_entry == '1':
            Change_password(accound_no)  # 1 For Calling Change Password Function

        elif input_entry == '2':
            Deposit(accound_no)  # 2 for Calling Deposit Function

        elif input_entry == '3':
            Withdrawals(accound_no)  # 3 for Withdrawal Function

        elif input_entry == '4':
            print("Balance : " + str(Balance(accound_no)))  # 4 for Balance Function and Printing

        elif input_entry == '5':
            Report(accound_no)  # Report Function

        elif input_entry == '6':
            break  # 6 for For LOGIN
        else:
            print("invalid entry")


# Change Password Function


def Change_password(account_no): # Corrected spelling: account_no
    print(f"Attempting to change password for account: {account_no}") # Debugging info
    Current_password = input("Enter Current Password : ")
    New_password = input("New Password : ")
    Confirm_New_password = input("Confirm New Password : ")

    if New_password != Confirm_New_password:
        print("Error: New passwords do not match.")
        return
    if not New_password: # Basic check for empty password
         print("Error: New password cannot be empty.")
         return

    # Find the current details and password for the user
    customer_line_to_edit = None
    original_password = None
    customer_found = False
    try:
        with open(CUSTOMER_DETAILS_FILE, 'r') as infile:
            for line in infile:
                parts = line.strip().split(' ')
                if len(parts) >= 6 and parts[4] == account_no:
                    customer_line_to_edit = line.strip() # Store the original line
                    original_password = parts[5]
                    customer_found = True
                    break # Found the user, no need to read further
    except FileNotFoundError:
        print(f"Error: Customer details file '{CUSTOMER_DETAILS_FILE}' not found.")
        return
    except Exception as e:
        print(f"An error occurred reading customer details: {e}")
        return

    if not customer_found:
        print(f"Error: Account {account_no} not found.")
        return

    # Check if the entered current password matches the stored one
    if Current_password != original_password:
        print("Error: Current password incorrect.")
        return

    # Prepare the updated line
    parts = customer_line_to_edit.split(' ')
    parts[5] = New_password # Update the password part
    updated_line = ' '.join(parts)

    # Update the file using a temporary file
    temp_file_path = CUSTOMER_DETAILS_FILE + ".tmp"
    try:
        with open(CUSTOMER_DETAILS_FILE, 'r') as infile, open(temp_file_path, 'w') as outfile:
            for line in infile:
                stripped_line = line.strip()
                if stripped_line == customer_line_to_edit:
                    outfile.write(updated_line + '\n') # Write the modified line
                    print("Password line identified and updated in temp file.") # Debug
                else:
                    outfile.write(line) # Write other lines unchanged

        # Replace the original file with the temporary file
        # This is safer than os.rename on some systems/situations
        shutil.move(temp_file_path, CUSTOMER_DETAILS_FILE)
        print("Password Successfully changed!")

    except Exception as error:
        print(f"An error occurred while updating the password file: {error}")
        # Attempt to clean up the temp file if it exists
        if os.path.exists(temp_file_path):
            try:
                os.remove(temp_file_path)
            except OSError as e:
                print(f"Error cleaning up temporary file {temp_file_path}: {e}")


# Deposit Function
def Deposit(account_no): # Corrected spelling: account_no
    Date = datetime.date.today()
    deposit_amount_str = input("Enter Amount : ") # Get amount as string first
    try:
        deposit_amount = int(deposit_amount_str) # Try converting to integer
        if deposit_amount <= 0:
            print("Error: Deposit amount must be positive.")
            return # Exit function if invalid amount

        withdrawals = '0'
        # Use 'with' for automatic closing
        with open(ACCOUNTS_FILE, 'a') as accounts:
            accounts.write(f"{account_no} {Date} {deposit_amount} {withdrawals}\n") # Use f-string for clarity
        print("Deposit Successful.")

    except ValueError:
        print("Error: Invalid amount entered. Please enter numbers only.")
    except FileNotFoundError:
        print(f"Error: Accounts file '{ACCOUNTS_FILE}' not found.")
    except Exception as e:
        print(f"An unexpected error occurred during deposit: {e}")


# Withdrawals Function
def Withdrawals(account_no): # Corrected spelling: account_no
    Date = datetime.date.today()
    deposit = '0'
    withdrawal_amount_str = input("Enter Amount : ")

    try:
        withdrawal_amount = int(withdrawal_amount_str)
        if withdrawal_amount <= 0:
            print("Error: Withdrawal amount must be positive.")
            return

        # Get current balance *before* checking minimums
        current_balance = Balance(account_no)
        if current_balance is None: # Handle case where balance check failed
             print("Error: Could not retrieve current balance.")
             return

        # Find customer details to check account type
        customer_details_list = None
        try:
            with open(CUSTOMER_DETAILS_FILE, 'r') as customer_details_file:
                for line in customer_details_file:
                    parts = line.strip().split(' ')
                    if len(parts) >= 5 and parts[4] == account_no:
                        customer_details_list = parts
                        break
        except FileNotFoundError:
            print(f"Error: Customer details file '{CUSTOMER_DETAILS_FILE}' not found.")
            return
        except Exception as e:
             print(f"An error occurred reading customer details: {e}")
             return

        if customer_details_list is None:
            print(f"Error: Customer account {account_no} not found.")
            return

        # print(customer_details_list) # Keep for debugging if needed

        account_type = customer_details_list[3] # 1-Savings / 2-Current
        min_balance = 0
        if account_type == '1': # Savings
            min_balance = 100
        elif account_type == '2': # Current
            min_balance = 500
        else:
            print(f"Warning: Unknown account type '{account_type}' for account {account_no}.")
            # Decide how to handle unknown types - maybe default to a high min balance or disallow?
            # For now, let's assume it's an error state or needs a default.
            min_balance = float('inf') # Effectively disallows withdrawal if type is wrong

        # Check if withdrawal respects minimum balance
        if (current_balance - withdrawal_amount) >= min_balance:
            try:
                with open(ACCOUNTS_FILE, 'a') as accounts:
                    accounts.write(f"{account_no} {Date} {deposit} {withdrawal_amount}\n")
                print("Transaction Successful")
            except FileNotFoundError:
                 print(f"Error: Accounts file '{ACCOUNTS_FILE}' not found during write.")
            except Exception as e:
                 print(f"An unexpected error occurred writing withdrawal: {e}")
        else:
            print(f"Transaction Error: Withdrawal would bring balance below minimum RM{min_balance}. Current Balance: RM{current_balance}")

    except ValueError:
        print("Error: Invalid amount entered. Please enter numbers only.")
    except Exception as e: # Catch unexpected errors during the process
        print(f"An unexpected error occurred during withdrawal: {e}")


# Balance Checking Function
def Balance(account_no): # Corrected spelling: account_no
    Total_Balance = 0
    try:
        with open(ACCOUNTS_FILE, 'r') as accounts:
            for line in accounts:
                line = line.strip()
                if not line:
                    continue
                parts = line.split(' ')
                # Basic validation of line format
                if len(parts) == 4 and parts[0] == account_no:
                    try:
                        deposit = int(parts[2])
                        withdrawal = int(parts[3])
                        Total_Balance += deposit
                        Total_Balance -= withdrawal
                    except ValueError:
                        print(f"Warning: Skipping line with non-numeric amount in {ACCOUNTS_FILE}: {line}")
                        continue # Skip this line if amounts aren't numbers
                elif len(parts) != 4 and parts[0] == account_no:
                     print(f"Warning: Skipping malformed line for account {account_no} in {ACCOUNTS_FILE}: {line}")
        return Total_Balance
    except FileNotFoundError:
        print(f"Error: Accounts file '{ACCOUNTS_FILE}' not found.")
        return None # Indicate error by returning None
    except Exception as e:
        print(f"An unexpected error occurred calculating balance: {e}")
        return None # Indicate error by returning None


# Report generating function
def Report(account_no):
    # Validation For Start Date Input
    while True:
        try:
            start_date = datetime.datetime.strptime(input("Enter Start Date (YYYY-MM-DD) : "), '%Y-%m-%d')
        except Exception as error:
            print(error)
            print("Does not match format 'YYYY-MM-DD'")
            continue
        break

    # Validation For End Date Input
    while True:
        try:
            end_date = datetime.datetime.strptime(input("Enter End Date (YYYY-MM-DD) : "), '%Y-%m-%d')
        except Exception as error:
            print(error)
            print("Does not match format 'YYYY-MM-DD'")
            continue
        break

    accounts = open("accounts", 'r')
    report = []
    # Checking the Entry in between the start date and end date
    while True:
        line = accounts.readline()
        if not line:
            break
        if line.strip().split(' ')[0] == account_no:
            if start_date <= datetime.datetime.strptime(line.strip().split(' ')[1], '%Y-%m-%d') <= end_date:
                report.append(line.strip().split(' '))
    print(report)
    index = 1
    print("Account No :" + account_no)
    # Showing generated Report
    print("SLNO".ljust(15) + "Date".ljust(15) + "Deposits".ljust(15) + "Withdrawals".ljust(15))
    for data in report:
        print(str(index).ljust(15) + str(data[1]).ljust(15) + str(data[2]).ljust(15) + str(data[3]).ljust(15))
        index = index + 1
