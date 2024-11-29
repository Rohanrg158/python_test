def mobile_number(number):

    number_length=len(number)
    if number_length==10:
        if number[0]=="7":
            print("Valid mobile number")
        elif number[0]=="8":
            print("Valid mobile number")
        elif number[0]=="9":
            print("Valid mobile number")
        else:
            print("Invalid mobile number")
    else:
        print("Invalid mobile number")
num= input("Enter mobile number: ")
mobile_number(num)
