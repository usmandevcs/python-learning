# problem 8

n = int(input("Enter the value of n: "))

for i in range(n):
    if i == 0 or i == n-1:
        # First and last row: full stars
        print("* " * n)
    else:
        # Middle rows: star at beginning and end, spaces in between
        print("*" + " " * (2*(n-2)+1) + "*")

