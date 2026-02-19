# 6. Write a program to calculate the factorial of a given number using for loop. 

# what is factorial? 
'''factorial ka mtlb ha jitny number given hain wo sab jab apas 
ma multiply hongy to factrial ayega.e.g; factorial of 5 
1 x 2 x 3 x 4 x 5 = ans '''
n = int(input("Enter the number: "))
ans = 1
for i in range(1,n+1):
    ans = ans*i
print(f"factorial of {n} is {ans}")
    