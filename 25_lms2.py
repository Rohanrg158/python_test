'''
Author: Rohan
Date: 25-10-2024
Write a Python program to convert temperature values back and forth between Celsius and Fahrenheit.
The user should be able to input a temperature in Celsius or Fahrenheit, and the program should convert it to the other unit using the formula:
c/5=(f-32)/9
'''

temp=int(input("Enter the temperature: "))
scale=input("Is this in (C)elsius or (F)ahrenheit?")
if scale=="C":
    print("The temp in Fahrenheit is:",(9/5*temp)+32)
else:
    print("The temp in Celsius is:",(5/9*(temp-32)))
    