n=int(input("Enter the number of rows: "))

# Increasing triangle
for i in range(1,n+1):
    for j in range(i):
        print('*', end=" ")
    print()

# Decreasing triangle
for k in range(n+1,0,-1):
    for l in range(k):
        print('*', end=" ")
    print()

# Hill pattern
for i in range(1, n + 1):
    for j in range(n - i):
        print(" ", end="")
    for k in range(1, 2 * i):
        print("*", end="")
    print()

# Reverse hill pattern
for i in range(n,0,-1):
    for j in range(n-i):
        print(" ", end="")
    for k in range(2*i-1):
        print("*", end="")
    print()
