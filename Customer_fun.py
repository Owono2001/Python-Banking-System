import datetime
import sys


# For Getting Customer Login Details from the text file
def Customer_login_details():
    file1 = open("customer_details.txt", 'r')  # Open the customer_details.txt file
    account_no = []  # List for saving Account NO
    password = []  # List for saving Password
    try:
        while True:
            line = file1.readline()  # Read Line by Line From the Text File
            if not line:  # End the loop if line has no data
                break
            #  Add Values to the List
            account_no.append(line.strip().split(' ')[4])
            password.append(line.strip().split(' ')[5])
        file1.close()
    except:
        pass
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


def Change_password(accound_no):
    print(accound_no)
    Current_password = input("Enter Current Password : ")  # Getting current Passwprd
    New_password = input("New Password : ")  # Getting New Password
    Confirm_New_password = input("Confirm New Password : ")  # Conmfroming the entered password
    Customer_details = []  # List for Customer Detials
    customer_details = open("customer_details.txt", 'r')  # opening Customer Detials text file
    while True:
        line = customer_details.readline()
        if line.strip().split(' ')[4] == accound_no:
            # Customer_detials.append(line.strip().split(' '))
            Customer_details = (line.strip().split(' '))
            edit_line = line
            break
        if not line:
            break
    # Checking Current password and conforming the entered password
    if Current_password == Customer_details[5] and New_password == Confirm_New_password:
        Edit_Customer_details = ''
        for x in Customer_details:
            Edit_Customer_details = Edit_Customer_details + x + ' '
        file = "customer_details.txt"
        # Variable for Update Customer details
        updated_customer_details = Customer_details[0] + ' ' + Customer_details[1] + ' ' + Customer_details[
            2] + ' ' + Customer_details[3] + ' ' + Customer_details[4] + ' ' + New_password
        # Updating to Customer Details text file
        try:
            with open('customer_details.txt', 'rt') as file:
                data = file.read()
                print(data)
                # Replace the target string
            data = data.replace(Edit_Customer_details.strip(), updated_customer_details)
            with open('customer_details.txt', 'wt') as file:
                file.write(data)
        except Exception as error:
            print(error)
        else:
            print("Password Succesfully changed !")
            file.close()


# Deposit Function
def Deposit(accound_no):
    Date = datetime.date.today()
    deposit = input("Enter Amount : ")  # Getting Deposit Amount
    withdrawals = '0'
    accounts = open("accounts", 'a')  # Opening accounts.txt
    accounts.write(accound_no + ' ' + str(Date) + ' ' + deposit + ' ' + withdrawals + '\n')  # Saving to accounts.txt
    accounts.close()


# Withdrawals Function
def Withdrawals(accound_no):
    Date = datetime.date.today()
    deposit = '0'
    withdrawals = input("Enter Amount : ")
    Total_balance = Balance(accound_no)
    customer_details = open("customer_details.txt", 'r')
    while True:
        line = customer_details.readline()
        if not line:
            break
        if line.strip().split(' ')[4] == accound_no:
            # Customer_details.append(line.strip().split(' '))
            Customer_details = (line.strip().split(' '))
            break
    print(Customer_details)
    # Checking Saving Or Current Account
    if Customer_details[3] == '1':  # 1-Savings / 2-Current    RM100 and RM500
        # Checking the Minimum balance
        if (Total_balance - int(withdrawals)) >= 100:
            accounts = open("accounts", 'a')
            accounts.write(
                accound_no + ' ' + str(Date) + ' ' + deposit + ' ' + withdrawals + '\n')  # Saving to accounts.txt
            accounts.close()
            print("Transaction Successful")
        else:
            print("Transaction Error : Minimum balance !")
    elif Customer_details[3] == '2':  # 1-Savings / 2-Current    RM100 and RM500
        # Checking the Minimum balance
        if (Total_balance - int(withdrawals)) >= 500:
            accounts = open("accounts", 'a')
            accounts.write(
                accound_no + ' ' + str(Date) + ' ' + deposit + ' ' + withdrawals + '\n')  # Saving to accounts.txt
            accounts.close()
            print("Transaction Successful")
        else:
            print("Transaction Error : Minimum balance !")
    else:
        pass


# Balance Checking Function
def Balance(accound_no):
    Total_Balance = 0  # Variable for store total balance
    accounts = open("accounts", 'r')
    while True:
        line = accounts.readline()
        if not line:
            break
        if line.strip().split(' ')[0] == accound_no:
            Total_Balance = Total_Balance + int(line.strip().split(' ')[2])
            Total_Balance = Total_Balance - int(line.strip().split(' ')[3])
    return Total_Balance  # Returning the Calculated balance


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
