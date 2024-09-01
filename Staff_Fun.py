import datetime
import sys


# Staff Details Function


def Staff_details():
    file1 = open("admin_staff_details", 'r')
    # List for Username and Password
    username = []
    password = []
    while True:
        line = file1.readline()
        if not line:
            break
        # print(line.strip().split(' ')[2])
        username.append(line.strip().split(' ')[2])
        password.append(line.strip().split(' ')[3])
    file1.close()
    # Return the username and password
    return username, password


# Staff menu function
def Staff_menu():
    while (1):
        print("\tMenu\n"
              "1 . Add Customer\n"
              "2 . Edit Customer\n"
              "3 . Report\n"
              "4 . Login")
        # Menu Selection
        input_entry = input("Select one: ")
        if input_entry == '1':
            Add_Customer()

        elif input_entry == '2':
            Edit_Customer()

        elif input_entry == '3':
            Staff_Report()

        elif input_entry == '4':
            break
        else:
            print("invalid entry")


# Add customer function
def Add_Customer():
    Customer_ID = ''  # Variable for customer id
    # Getting Customer Id from customer_detials.txt
    try:
        with open('customer_details.txt', 'r') as f:
            lines = f.read().splitlines()
            last_line = lines[-1]
            # print (last_line)
            Customer_ID = str(int(last_line.strip().split(' ')[0]) + 1)
            print("Customer ID : " + Customer_ID)
    except:
        Customer_ID = '1'

    # Validation for Inputs
    while True:
        Name = input("Enter Name : ")
        if Name == '':
            print("Mandatory Field ")
            continue
        else:
            break
    # Validation for Inputs
    while True:
        Date_of_birth = input("Enter Date of Birth : ")
        if Date_of_birth == '':
            print("Mandatory Field ")
            continue
        else:
            break
    # Validation for Inputs
    while True:
        Account_type = input("Enter Account type (Savings / Current) : ")
        if Account_type == '':
            print("Mandatory Field ")
            continue
        else:
            break
    # Validation for Inputs
    while True:
        User_Password = input("Enter Password: ")
        if User_Password == '':
            print("Mandatory Field ")
            continue
        else:
            break
    # 0562800001
    Account_No = ''  # variable for Generating account no
    # Account No Generating Function
    try:
        with open('customer_details.txt', 'r') as f:
            lines = f.read().splitlines()
            last_line = lines[-1]
            # print (last_line)
            Account_No = '05628' + str(
                int(last_line.strip().split(' ')[4][4:len(last_line.strip().split(' ')[4]):]) + 1)
    except:
        Account_No = '0562800001'
    # Save to customer_details.txt
    customer_details = open("customer_details.txt", 'a')
    customer_details.write(
        Customer_ID + ' ' + Name + ' ' + Date_of_birth + ' ' + Account_type + ' ' + Account_No + ' ' + User_Password + '\n')
    customer_details.close()
    print("Added Successfully:")
    print("Your Account Number : " + str(Account_No))
    print("Your Password : " + str(User_Password))


# Edit Customer Function
def Edit_Customer():
    customer_details = open("customer_details.txt", 'r')
    Customer_list = []  # List for Customer Details
    # Add Customer Details to List
    while True:
        line = customer_details.readline()
        if not line:
            break
        Customer_list.append(line.strip().split(' '))
        print(Customer_list)
        index = 1
        if Customer_list != []:
            # Print the Customer Details in Comment line
            print("SLNO".ljust(15) + "Customer ID".ljust(15) + "Name".ljust(15) + "Date of Birth".ljust(15) + "Account Type".ljust(15) + "Account No".ljust(15) + "Password")
            for data in Customer_list:
                print(str(index).ljust(15) + str(data[0]).ljust(15) + str(data[1]).ljust(15) + str(data[2]).ljust(15) + str(data[3]).ljust(15) + str(data[4]).ljust(15) + str(data[5]))
                index = index + 1
            # For Selecting the Customer For Editing
            entered_input = input("Enter th SLNO want to Edit (q for Back): ")
            if entered_input == 'q':
                return None
            edit_Customer = Customer_list[int(entered_input) - 1]
            edit_Customer_str = ''
            for x in edit_Customer:
                edit_Customer_str = edit_Customer_str + x + ' '
            # Getting the other Detials
            print("Current Date of Birth : " + edit_Customer[2])
            Enterd_DOB = input("Enter New Date of Birth (YYYY-MM-DD): ")
            print("Current Account Type : " + edit_Customer[3])
            Enterd_Account_Type = input("Enter New Account Type (Savings / Current): ")
            print("Current Password : " + edit_Customer[5])
            Enterd_Password = input("Enter New Password : ")
            updated_customer_details = edit_Customer[0] + ' ' + edit_Customer[1] + ' ' + Enterd_DOB + ' ' + Enterd_Account_Type + ' ' + edit_Customer[4] + ' ' + Enterd_Password
            print(updated_customer_details)
            # Saving to the Corresponding Customer Details Line in text files
            try:
                with open('customer_details.txt', 'r') as file:
                    data = file.read()
                    print(data)
                    # Replace the target string
                data = data.replace(edit_Customer_str.strip(), updated_customer_details)
                with open('customer_details.txt', 'w') as file:
                    file.write(data)
            except Exception as error:
                print(error)
        else:
            print("No Customer Added !")
            file.close()



# Customer Report Generating Function For Staff
def Staff_Report():
    account_no = input("Enter Account No : ")
    # Validation For Input
    while True:
        try:
            start_date = datetime.datetime.strptime(input("Enter Start Date (YYYY-MM-DD) : "), '%Y-%m-%d')
        except Exception as error:
            print(error)
            print("Does not match format 'YYYY-MM-DD'")
            continue
        break
    # Validation For Input
    while True:
        try:
            end_date = datetime.datetime.strptime(input("Enter End Date (YYYY-MM-DD) : "), '%Y-%m-%d')
        except Exception as error:
            print(error)
            print("Does not match format 'YYYY-MM-DD'")
            continue
        break

    accounts = open("accounts", 'r')
    # List for Report Generating
    Report = []
    # Adding Report to the list
    while True:
        line = accounts.readline()
        if not line:
            break
        if (line.strip().split(' ')[0] == account_no):
            # Checking the Start date and End date
            if start_date <= datetime.datetime.strptime(line.strip().split(' ')[1], '%Y-%m-%d') <= end_date:
                Report.append(line.strip().split(' '))
    print(Report)
    index = 1
    # Showing the generated Report
    print("Account No :" + account_no)
    print("SLNO".ljust(15) + "Date".ljust(15) + "Deposits".ljust(15) + "Withdrawals".ljust(15))
    for data in Report:
        print(str(index).ljust(15) + str(data[1]).ljust(15) + str(data[2]).ljust(15) + str(data[3]).ljust(15))
        index = index + 1
