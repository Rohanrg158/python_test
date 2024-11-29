def triangle():
    a = int(input("Enter the first side length: "))
    b = int(input("Enter the second side length: "))
    c = int(input("Enter the third side length: "))
    pythagorean_theorem=(a**2+b**2)
    if pythagorean_theorem==c**2:
        print("It is a right angle triangle")
    else:
        print("It is not a right angle triangle")
triangle()