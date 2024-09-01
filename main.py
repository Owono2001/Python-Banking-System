import Customer_fun
import Staff_Fun
import SuperUser_Fun
from SuperUser_Fun import *
from Customer_fun import *
from Staff_Fun import *


def login(username, password):  # Checking for Login User
    if (username == "admin" and password == "admin1234"):  # Check that admin or not
        print("super user logged in")

        SU_Select()  # Call the Menu Selection Function
    # elif(username == )
    else:
        staff_username, staff_password = Staff_Fun.Staff_details()  # Call the Staff Details Function to get Username and Password of Staff
        customer_account_no, customer_password = Customer_fun.Customer_login_details()  # Call the Customer Details Function For Username and Password
        stored_username = ''  # Variable for Store the Staff Username
        stored_password = ''  # Variable for Store the Staff Password
        Customer_stored_username = ''  # Variable for Store the Customer Username
        Customer_stored_password = ''  # Variable for Store the Customer Username
        Staff_Flage = False  # Flage for Check staff or Customer
        Customer_Flage = False
        #   Checking Entered Username and Password in Staff Details
        for x in range(len(staff_username)):
            if (username == staff_username[x] and password == staff_password[x]):
                # print("user exist")
                stored_username = staff_username[x]
                stored_password = staff_password[x]
                Staff_Flage = True  # Set if Present
                break

        #   Checking Entered Username and Password in Customer Details
        for y in range(len(customer_account_no)):
            if (username == customer_account_no[y] and password == customer_password[y]):
                Customer_stored_username = customer_account_no[y]
                Customer_stored_password = customer_password[y]
                Customer_Flage = True  # Set if Pressent
                break
        # Check the staff and customer flage for login
        if stored_username and Staff_Flage:
            print("Loged in as " + str(stored_username))
            Staff_Fun.Staff_menu()  # calling Staff Menu Fun
        elif Customer_stored_username and Customer_Flage:
            print("Loged in as " + str(Customer_stored_username))
            Customer_fun.Customer_menu(Customer_stored_username)  # calling Customer Menu Fun and pass Account No
        else:
            print("User does not exist !")
            # pass
        # print(f'Hi, {username}')
        # print(f'Hi, {password}')


def SU_Select():
    while (1):
        print("1 . Create User\n"
              "2 . Login")
        entery = input("Select one : ")  # Menu Input Selection
        if  entery == '1' :
            SuperUser_Fun.Su_Creat_user()

        elif  entery == '2':
            break
        else:
            print("invalid entry")
if __name__ == '__main__':
    print("WELCOME TO PEDRO LOCAL BANK")
    print("\tLOGIN")
    while (1):
        username = input("Enter Username : ")
        password = input("Enter Password : ")  # password = getpass('Password :')
        # noinspection PyPep8
        login(username, password)  # Calling Login Function and Pass entered Username and Password
