def factorial(n):
    f=1
    for i in range(1,n+1):
        f=f*i
    print("Factorial is: ",f)
number=int(input("Enter a number: "))
factorial(number)