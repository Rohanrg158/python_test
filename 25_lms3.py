num=int(input("Enter a number: "))
sum_of_digits=0
while num>0:
    remainder=num%10
    sum_of_digits=sum_of_digits+remainder
    num=num//10
print("Sum of digits of the given number:",sum_of_digits)
