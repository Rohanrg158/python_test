def addition(num1,num2):
    if num1==0:
        return num2
    elif num2==0:
        return num1
    else:
        return addition(num1+1,num2-1)
number1=int(input("Enter a number: "))
number2=int(input("Enter another number: "))