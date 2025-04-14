# SuperUser_Fun.py
import os

# Define constants for filenames
ADMIN_STAFF_DETAILS_FILE = "admin_staff_details.txt" # Assuming .txt extension

# Helper function for mandatory input (could be moved to a common utility module)
def get_mandatory_input(prompt):
    """Gets non-empty input from the user."""
    while True:
        value = input(prompt).strip()
        if value:
            return value
        else:
            print("Input cannot be empty. Please try again.")

# Function to check if username already exists
def check_username_exists(username):
    """Checks if a staff username already exists in the details file."""
    try:
        # Check if file exists first
        if not os.path.exists(ADMIN_STAFF_DETAILS_FILE):
            return False # Cannot exist if file doesn't exist

        with open(ADMIN_STAFF_DETAILS_FILE, 'r') as file:
            for line in file:
                line = line.strip()
                if not line: continue
                parts = line.split(' ')
                # Assuming format: FName LName User Pass
                if len(parts) >= 3 and parts[2] == username:
                    return True # Username found
    except IOError as e:
        print(f"Warning: Could not read staff details file to check username: {e}")
        # Decide behavior: maybe prevent creation if check fails?
        # Returning False allows creation, but with a warning.
        return False
    except Exception as e:
         print(f"An unexpected error occurred checking username: {e}")
         return False # Safer to assume not found if error occurs? Or block creation?

    return False # Username not found

# Super User Creating Function for creating Staff (Improved Validation)
def Su_Creat_user():
    """Creates a new staff user, ensuring username doesn't already exist."""
    print("\n--- Create New Staff User ---")

    first_name = get_mandatory_input("Enter First Name : ")
    last_name = get_mandatory_input("Enter Last Name : ")

    # Get and validate Username (check for existence)
    while True:
        username = get_mandatory_input("Enter Username : ")
        if ' ' in username: # Basic check - usernames usually don't have spaces
             print("Username cannot contain spaces. Please try again.")
             continue
        if check_username_exists(username):
            print(f"Error: Username '{username}' already exists. Please choose a different one.")
        else:
            # Add a secondary check in case of read error during check_username_exists
            # This provides a bit more safety if the file was unreadable earlier.
            if check_username_exists(username): # Re-check just before proceeding
                 print(f"Error: Username '{username}' check conflict. Please try again.")
                 continue
            break # Username is valid and doesn't exist

    password = get_mandatory_input("Enter Password : ")

    # Adding Details to admin_staff_details.txt File
    new_staff_line = f"{first_name} {last_name} {username} {password}\n"

    try:
        # Use 'a' to append the new user
        with open(ADMIN_STAFF_DETAILS_FILE, 'a') as admin_staff_file:
            admin_staff_file.write(new_staff_line)
        print("\nStaff User Added Successfully:")
        print(f"   Username: {username}")
        print(f"   Name: {first_name} {last_name}")
        print("The new user can now log in using the staff credentials.")
    except IOError as e:
        print(f"Error: Could not write to staff details file '{ADMIN_STAFF_DETAILS_FILE}': {e}")
    except Exception as e:
        print(f"An unexpected error occurred saving staff details: {e}")