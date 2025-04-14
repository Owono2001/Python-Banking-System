# main.py
import Customer_fun
import Staff_Fun
import SuperUser_Fun
# Removed redundant specific imports as module is imported
# from SuperUser_Fun import * # Generally avoid wildcard imports
# from Customer_fun import *
# from Staff_Fun import *

# Consider defining credentials as constants for clarity
SUPERUSER_USERNAME = "admin"
SUPERUSER_PASSWORD = "admin1234"

def login(username, password):  # Checking for Login User
    """Handles login for SuperUser, Staff, and Customer."""
    if username == SUPERUSER_USERNAME and password == SUPERUSER_PASSWORD:
        print("\nSuper User logged in successfully.")
        SU_Select()  # Call the SuperUser Menu Selection Function

    else:
        # Retrieve staff details (handles errors internally now)
        staff_usernames, staff_passwords = Staff_Fun.Staff_details()

        # Retrieve customer details (handles errors internally now)
        customer_account_nos, customer_passwords = Customer_fun.Customer_login_details()

        # Check if login matches any staff member
        staff_found = False
        for i in range(len(staff_usernames)):
            if username == staff_usernames[i] and password == staff_passwords[i]:
                print(f"\nLogged in as Staff: {username}")
                Staff_Fun.Staff_menu()  # calling Staff Menu Fun
                staff_found = True
                break # Exit loop once found

        # If not found as staff, check if login matches any customer
        if not staff_found:
            customer_found = False
            for i in range(len(customer_account_nos)):
                # Ensure comparison is correct (username input vs account number)
                if username == customer_account_nos[i] and password == customer_passwords[i]:
                    print(f"\nLogged in as Customer: {username}")
                    # Pass the confirmed account number (username in this case)
                    Customer_fun.Customer_menu(username) # calling Customer Menu Fun
                    customer_found = True
                    break # Exit loop once found

            # If not found as staff or customer
            if not customer_found:
                print("\nLogin Failed: Invalid username or password.")


def SU_Select():
    """Menu for SuperUser after successful login."""
    while True:
        print("\n--- SuperUser Menu ---")
        print("1 . Create Staff User")
        print("2 . Logout")
        print("----------------------")
        entry = input("Select one : ").strip()
        if entry == '1':
            SuperUser_Fun.Su_Creat_user()
        elif entry == '2':
            print("Logging out SuperUser...")
            break # Exit SuperUser menu
        else:
            print("Invalid entry. Please select 1 or 2.")

# Main execution block
if __name__ == '__main__':
    print("\n--- WELCOME TO PEDRO LOCAL BANK ---")
    while True: # Main login loop
        print("\n--- LOGIN ---")
        username = input("Enter Username : ").strip()
        # Consider using getpass for password input for better security
        # import getpass
        # password = getpass.getpass("Enter Password : ")
        password = input("Enter Password : ").strip() # Using input for simplicity here

        if not username or not password:
             print("Username and password cannot be empty.")
             continue # Ask for login again

        login(username, password)
        # After a successful login (and subsequent logout from that role's menu),
        # the loop will continue, prompting for login again.
        # Add a check or option here if you want to exit the entire application.
        # For example:
        # exit_choice = input("Do you want to exit the application? (yes/no): ").lower()
        # if exit_choice == 'yes':
        #     print("Exiting application. Goodbye!")
        #     break