# Staff_Fun.py
import datetime
import sys
import os       # For file operations in Edit_Customer
import shutil   # For safer file replacement in Edit_Customer

# Define constants for filenames
ADMIN_STAFF_DETAILS_FILE = "admin_staff_details.txt" # Assuming .txt extension
CUSTOMER_DETAILS_FILE = "customer_details.txt"
ACCOUNTS_FILE = "accounts.txt" # Assuming .txt extension


# Staff Details Function (Improved Error Handling)
def Staff_details():
    """Reads staff usernames and passwords from the details file."""
    usernames = []
    passwords = []
    try:
        with open(ADMIN_STAFF_DETAILS_FILE, 'r') as file1:
            for line_num, line in enumerate(file1, 1):
                line = line.strip()
                if not line: # Skip empty lines
                    continue
                parts = line.split(' ')
                # Expecting at least 4 parts: FName LName User Pass
                if len(parts) >= 4:
                    usernames.append(parts[2])
                    passwords.append(parts[3])
                else:
                    print(f"Warning: Skipping malformed line #{line_num} in {ADMIN_STAFF_DETAILS_FILE}: {line}")
    except FileNotFoundError:
        print(f"Error: Staff details file '{ADMIN_STAFF_DETAILS_FILE}' not found.")
        # Depending on requirements, may need to create it or exit
    except Exception as e:
        print(f"An unexpected error occurred reading {ADMIN_STAFF_DETAILS_FILE}: {e}")

    return usernames, passwords


# Staff menu function (minor changes for consistency if needed)
def Staff_menu():
    """Displays the staff menu and handles user selection."""
    while True: # Use True for clearer infinite loop
        print("\n--- Staff Menu ---")
        print("1 . Add Customer")
        print("2 . Edit Customer")
        print("3 . Customer Transaction Report")
        print("4 . Logout")
        print("------------------")

        input_entry = input("Select one: ")
        if input_entry == '1':
            Add_Customer()
        elif input_entry == '2':
            Edit_Customer()
        elif input_entry == '3':
            Staff_Report()
        elif input_entry == '4':
            print("Logging out...")
            break # Exit the staff menu loop
        else:
            print("Invalid entry. Please select a number from 1 to 4.")


# Helper function for mandatory input
def get_mandatory_input(prompt):
    """Gets non-empty input from the user."""
    while True:
        value = input(prompt).strip()
        if value:
            return value
        else:
            print("Input cannot be empty. Please try again.")

# Helper function to validate account type
def get_valid_account_type(prompt):
    """Gets a valid account type (Savings or Current, case-insensitive). Returns '1' or '2'."""
    while True:
        acc_type_input = input(prompt).strip().lower()
        if acc_type_input == 'savings':
            return '1'
        elif acc_type_input == 'current':
            return '2'
        else:
            print("Invalid account type. Please enter 'Savings' or 'Current'.")


# Add customer function (Improved Validation, Error Handling)
def Add_Customer():
    """Adds a new customer to the system."""
    print("\n--- Add New Customer ---")
    customer_id = '1' # Default for first customer
    next_account_suffix = 1 # Default for first account

    # Get the next Customer ID and Account Number suffix
    try:
        last_line = None
        # Check if file exists and read last line efficiently if it does
        if os.path.exists(CUSTOMER_DETAILS_FILE):
             with open(CUSTOMER_DETAILS_FILE, 'rb') as f: # Read bytes for seeking
                try: # handle empty file
                    f.seek(-2, os.SEEK_END)
                    while f.read(1) != b'\n':
                        f.seek(-2, os.SEEK_CUR)
                    last_line = f.readline().decode().strip()
                except OSError: # Probably empty file
                    f.seek(0)
                    last_line = f.readline().decode().strip()

        if last_line:
            parts = last_line.split(' ')
            if len(parts) >= 5:
                try:
                    last_customer_id = int(parts[0])
                    customer_id = str(last_customer_id + 1)

                    # Extract last account number part
                    last_account_no = parts[4]
                    if last_account_no.startswith('05628') and len(last_account_no) > 5:
                         last_suffix_str = last_account_no[5:] # Get the part after '05628'
                         if last_suffix_str.isdigit():
                              next_account_suffix = int(last_suffix_str) + 1
                         else:
                             print(f"Warning: Could not parse suffix from last account number: {last_account_no}")
                             # Fallback or specific error needed? Using default '1' for now.
                    else:
                         print(f"Warning: Last account number format unexpected: {last_account_no}")
                         # Fallback or specific error needed? Using default '1' for now.

                except ValueError:
                    print(f"Warning: Could not parse numeric data from last line: {last_line}")
                    # Decide on fallback: keep default '1' or raise error?
                except IndexError:
                     print(f"Warning: Malformed last line in customer details: {last_line}")

    except FileNotFoundError:
        print(f"Info: '{CUSTOMER_DETAILS_FILE}' not found. Creating new file.")
    except Exception as e:
        print(f"An error occurred reading last customer details: {e}")
        print("Proceeding with default ID 1 and Account Suffix 1.")
        # Reset to defaults just in case
        customer_id = '1'
        next_account_suffix = 1

    print(f"Next Customer ID: {customer_id}")

    # Generate Account Number (padding suffix to 5 digits)
    account_no = f"05628{next_account_suffix:05d}" # e.g., 0562800001, 0562800002

    print(f"Generated Account Number: {account_no}")

    # Validation for Inputs using helper
    name = get_mandatory_input("Enter Name : ")
    # Add basic space check for name (as split(' ') is used)
    if ' ' in name:
        print("Warning: Name contains spaces. Consider using a different delimiter or format for storage if this is common.")

    # Basic date validation could be added here (e.g., using try-strptime)
    date_of_birth = get_mandatory_input("Enter Date of Birth (YYYY-MM-DD) : ")
    account_type_code = get_valid_account_type("Enter Account type (Savings / Current) : ")
    user_password = get_mandatory_input("Enter Password: ")

    # --- Optional: Check if generated account number already exists ---
    account_exists = False
    try:
         if os.path.exists(CUSTOMER_DETAILS_FILE):
              with open(CUSTOMER_DETAILS_FILE, 'r') as f:
                   for line in f:
                        parts = line.strip().split(' ')
                        if len(parts) >= 5 and parts[4] == account_no:
                             account_exists = True
                             break
    except Exception as e:
         print(f"Warning: Could not verify if account {account_no} exists due to error: {e}")

    if account_exists:
         print(f"Error: Generated Account Number {account_no} already exists! Cannot add customer. Please check the data file or logic.")
         return
    # --- End Optional Check ---

    # Save to customer_details.txt
    new_customer_line = f"{customer_id} {name} {date_of_birth} {account_type_code} {account_no} {user_password}\n"

    try:
        with open(CUSTOMER_DETAILS_FILE, 'a') as customer_details_file:
            customer_details_file.write(new_customer_line)
        print("\nCustomer Added Successfully:")
        print(f"   Account Number : {account_no}")
        print(f"   Password : {user_password}")
    except IOError as e:
        print(f"Error: Could not write to customer details file '{CUSTOMER_DETAILS_FILE}': {e}")
    except Exception as e:
        print(f"An unexpected error occurred saving customer details: {e}")


# Edit Customer Function (Improved Validation, Error Handling, Temp File Update)
def Edit_Customer():
    """Edits details for an existing customer."""
    print("\n--- Edit Customer ---")
    customer_list = []
    try:
        with open(CUSTOMER_DETAILS_FILE, 'r') as customer_details_file:
            for line_num, line in enumerate(customer_details_file, 1):
                line = line.strip()
                if not line: continue
                parts = line.strip().split(' ')
                if len(parts) == 6: # Expect ID Name DOB Type AccNo Pass
                    customer_list.append(parts)
                else:
                     print(f"Warning: Skipping malformed line #{line_num} in {CUSTOMER_DETAILS_FILE} during edit display: {line}")

    except FileNotFoundError:
        print(f"Error: Customer details file '{CUSTOMER_DETAILS_FILE}' not found. Cannot edit.")
        return
    except Exception as e:
        print(f"An error occurred reading customer details for editing: {e}")
        return

    if not customer_list:
        print("No customers found in the file to edit.")
        return

    # Print the Customer Details
    print("\nAvailable Customers:")
    print("-" * 80)
    print("SLNO".ljust(5) + "Customer ID".ljust(15) + "Name".ljust(20) + "DOB".ljust(15) + "Type".ljust(10) + "Account No".ljust(15))
    print("-" * 80)
    for index, data in enumerate(customer_list):
        # Display type name instead of code
        acc_type_display = "Savings" if data[3] == '1' else "Current" if data[3] == '2' else "Unknown"
        print(f"{str(index + 1).ljust(5)}{data[0].ljust(15)}{data[1].ljust(20)}{data[2].ljust(15)}{acc_type_display.ljust(10)}{data[4].ljust(15)}") # Don't display password
    print("-" * 80)

    # Select Customer For Editing
    while True:
        entered_input = input(f"Enter the SLNO (1-{len(customer_list)}) to Edit (or 'q' to Quit): ").strip()
        if entered_input.lower() == 'q':
            return # Exit editing

        try:
            edit_index = int(entered_input) - 1
            if 0 <= edit_index < len(customer_list):
                edit_customer_data = customer_list[edit_index]
                break # Valid selection
            else:
                print(f"Invalid SLNO. Please enter a number between 1 and {len(customer_list)}.")
        except ValueError:
            print("Invalid input. Please enter a number or 'q'.")

    # Store original line for replacement logic
    original_customer_line = ' '.join(edit_customer_data)

    # Get updated details
    print("\nEnter new details (leave blank to keep current value):")

    print(f"Current Date of Birth : {edit_customer_data[2]}")
    entered_dob = input("Enter New Date of Birth (YYYY-MM-DD): ").strip()
    # Add format validation if desired: try datetime.datetime.strptime(entered_dob, '%Y-%m-%d')

    current_type_display = "Savings" if edit_customer_data[3] == '1' else "Current" if edit_customer_data[3] == '2' else "Unknown"
    print(f"Current Account Type : {current_type_display} ({edit_customer_data[3]})")
    # Use helper for validation, but allow empty input
    new_account_type_code = ''
    while True:
         acc_type_input = input("Enter New Account Type (Savings / Current): ").strip().lower()
         if not acc_type_input: # Allow keeping current
              new_account_type_code = edit_customer_data[3]
              break
         elif acc_type_input == 'savings':
              new_account_type_code = '1'
              break
         elif acc_type_input == 'current':
              new_account_type_code = '2'
              break
         else:
              print("Invalid account type. Enter 'Savings', 'Current', or leave blank.")


    print(f"Current Password : {edit_customer_data[5]} (Hidden)") # Don't show actual password ideally
    entered_password = input("Enter New Password : ").strip()


    # Prepare the updated data list, using original values if input was empty
    updated_customer_data = edit_customer_data[:] # Make a copy
    if entered_dob:
        updated_customer_data[2] = entered_dob
    # Account type code is already set correctly above
    updated_customer_data[3] = new_account_type_code
    if entered_password:
        updated_customer_data[5] = entered_password

    updated_customer_line = ' '.join(updated_customer_data)

    # If nothing changed, inform user and exit
    if original_customer_line == updated_customer_line:
         print("\nNo changes were made.")
         return

    print("\n--- Review Changes ---")
    print("Original:", original_customer_line)
    print("Updated :", updated_customer_line)
    confirm = input("Save these changes? (yes/no): ").strip().lower()

    if confirm != 'yes':
        print("Changes discarded.")
        return

    # --- Save using temporary file method ---
    temp_file_path = CUSTOMER_DETAILS_FILE + ".tmp"
    write_error = False
    try:
        with open(CUSTOMER_DETAILS_FILE, 'r') as infile, open(temp_file_path, 'w') as outfile:
            for line in infile:
                stripped_line = line.strip()
                # Compare based on account number (safer if other fields could change)
                # Assuming account number (index 4) is unique and doesn't change here
                line_parts = stripped_line.split(' ')
                if len(line_parts) >= 5 and line_parts[4] == edit_customer_data[4]: # Match based on account number
                     print(f"Replacing line for account {edit_customer_data[4]}")
                     outfile.write(updated_customer_line + '\n')
                else:
                     outfile.write(line) # Write other lines unchanged

        # Replace original file with temp file
        shutil.move(temp_file_path, CUSTOMER_DETAILS_FILE)
        print("Customer details updated successfully!")

    except FileNotFoundError: # Should not happen if initial read worked, but good practice
         print(f"Error: Original file '{CUSTOMER_DETAILS_FILE}' disappeared during update.")
         write_error = True
    except (IOError, OSError, shutil.Error) as error:
        print(f"An error occurred while updating the customer file: {error}")
        write_error = True
    finally:
        # Clean up temp file if error occurred and it still exists
        if write_error and os.path.exists(temp_file_path):
            try:
                os.remove(temp_file_path)
                print(f"Removed temporary file: {temp_file_path}")
            except OSError as e:
                print(f"Error cleaning up temporary file {temp_file_path}: {e}")
    # --- End temporary file save ---


# Customer Report Generating Function For Staff (Improved Validation)
def Staff_Report():
    """Generates a transaction report for a customer account within a date range."""
    print("\n--- Generate Customer Transaction Report ---")

    account_no = input("Enter Customer Account No : ").strip()
    if not account_no:
        print("Account number cannot be empty.")
        return

    # Validation For Start Date Input
    start_date = None
    while start_date is None:
        try:
            start_date_str = input("Enter Start Date (YYYY-MM-DD) : ").strip()
            start_date = datetime.datetime.strptime(start_date_str, '%Y-%m-%d')
        except ValueError:
            print("Invalid date format. Please use YYYY-MM-DD.")
        except Exception as e: # Catch other unexpected errors
             print(f"An error occurred processing the start date: {e}")
             return # Exit if unexpected error

    # Validation For End Date Input
    end_date = None
    while end_date is None:
        try:
            end_date_str = input("Enter End Date (YYYY-MM-DD) : ").strip()
            end_date = datetime.datetime.strptime(end_date_str, '%Y-%m-%d')
            if end_date < start_date:
                print("End date cannot be before start date.")
                end_date = None # Force re-entry
        except ValueError:
            print("Invalid date format. Please use YYYY-MM-DD.")
        except Exception as e:
             print(f"An error occurred processing the end date: {e}")
             return # Exit if unexpected error


    report_lines = []
    try:
        with open(ACCOUNTS_FILE, 'r') as accounts:
            for line_num, line in enumerate(accounts, 1):
                line = line.strip()
                if not line: continue
                parts = line.split(' ')

                # Expecting AccNo Date Deposit Withdraw
                if len(parts) == 4 and parts[0] == account_no:
                    try:
                        transaction_date = datetime.datetime.strptime(parts[1], '%Y-%m-%d')
                        # Check if transaction date is within the requested range (inclusive)
                        if start_date <= transaction_date <= end_date:
                            # Basic validation of amounts before adding
                            int(parts[2]) # Check if deposit is integer
                            int(parts[3]) # Check if withdrawal is integer
                            report_lines.append(parts)
                    except ValueError:
                         print(f"Warning: Skipping line #{line_num} in {ACCOUNTS_FILE} due to invalid date or amount format: {line}")
                    except IndexError:
                         print(f"Warning: Skipping malformed line #{line_num} in {ACCOUNTS_FILE}: {line}")
                elif parts[0] == account_no: # Handle lines for the account but with wrong format
                     print(f"Warning: Skipping malformed line #{line_num} for account {account_no} in {ACCOUNTS_FILE}: {line}")


    except FileNotFoundError:
        print(f"Error: Accounts file '{ACCOUNTS_FILE}' not found.")
        return
    except Exception as e:
        print(f"An error occurred reading the accounts file: {e}")
        return

    # Showing the generated Report
    print("\n--- Transaction Report ---")
    print(f"Account No : {account_no}")
    print(f"Period     : {start_date.strftime('%Y-%m-%d')} to {end_date.strftime('%Y-%m-%d')}")
    print("-" * 60)
    print("SLNO".ljust(10) + "Date".ljust(15) + "Deposits".ljust(15) + "Withdrawals".ljust(15))
    print("-" * 60)

    if not report_lines:
        print("No transactions found for this account in the specified period.")
    else:
        for index, data in enumerate(report_lines):
            print(f"{str(index + 1).ljust(10)}{str(data[1]).ljust(15)}{str(data[2]).ljust(15)}{str(data[3]).ljust(15)}")
    print("-" * 60)