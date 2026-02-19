# 7. Write a program to print the following star pattern. 
'''
  * 
 *** 
***** 
for n = 3 '''
n = int(input("Enter the number of rows: "))

for i in range(1, n+1):
    # spaces for alignment
    print(' ' * (n - i) + '*' * (2*i - 1))
            # or 
    # print(' ' * (n - i)
    # print('*' * (2*i - 1))

