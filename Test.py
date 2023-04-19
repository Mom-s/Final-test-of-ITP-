phoneDirectory={}
M1=0
while True:
    if M1==0:
        print("\nWELCOME TO THE GRANN'S PHONE DIRECTORY MENU\n")
    else:
        print("\nMenu")
    M1=M1+1
    while True:

        print("\nMenu\n")
        print("\n1. Add a record")
        print("\n2. Search a record")
        print("\n3. Change a record")
        print("\n4. Delete a record")
        print("\n5. Quit")
        

        choice = input("\nEnter your choice: ")
        

        if choice == '1':
            name = input("\nEnter name: ")

            if name.replace(" ", "").isalpha(): # check if input contains only alphabets and spaces
                phone_number = input("Enter your 10-digit phone number: ")

                if len(phone_number) == 10 and phone_number.isdigit():
                    phoneDirectory[name] = phone_number
                    print("\nRecord added")
                else:
                    print("\nInvalid phone number. Please enter a 10-digit phone number.")
            else:
                print("\nInvalid name. Please enter a valid name.")

        elif choice == '2':
            name = input("\nEnter name to search: ")

            if name in phoneDirectory:
                print(name + ": " + phoneDirectory[name])
            else:
                print("\nName not found")

        elif choice == '3':
            name = input("\nEnter name: ")

            if name in phoneDirectory:
                phone_number = input("Enter new 10-digit phone number: ")

                if len(phone_number) == 10 and phone_number.isdigit():
                    phoneDirectory[name] = phone_number
                    print("\nRecord updated")
                else:
                    print("\nInvalid phone number. Please enter a 10-digit phone number.")
            else:
                print("\nName not found")

        elif choice == '4':
            name = input("\nEnter name: ")

            if name in phoneDirectory:
                del phoneDirectory[name]
                print("\nRecord deleted")
            else:
                print("\nName not found")

        elif choice == '5':
            print("\nGoodbye!")
            break

        else:
            print("\nInvalid choice. Please enter a valid choice.")