# Super User Creating Function for creating Staff
def Su_Creat_user():
    # Validation for Input
    while True:
        First_name = input("Enter First Name : ")
        if First_name == '':
            print("Mandatory Field ")
            continue
        else:
            break
    # Validation for Input
    while True:
        Last_name = input("Enter Last Name : ")
        if Last_name == '':
            print("Mandatory Field ")
            continue
        else:
            break
    # Validation for Input
    while True:
        Username = input("Enter Username : ")
        if Username == '':
            print("Mandatory Field ")
            continue
        else:
            break
    # Validation for Input
    while True:
        Password = input("Enter Password : ")
        if Password == '':
            print("Mandatory Field ")
            continue
        else:
            break
    # Adding Details to admin_staff_details.txt File
    admin_staff = open("admin_staff_details", 'a')
    admin_staff.write(First_name + ' ' + Last_name + ' ' + Username + ' ' + Password+'\n')
    admin_staff.close()
    print("Added Successfully:")
    print("You are already a member of PEDRO Bank administration Staff")
