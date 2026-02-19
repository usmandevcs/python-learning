# Problem 3 
'''
Write a program to generate multiplication tables from 2 to 20 
and write it to the different files. Place these files in a 
folder for a 13  year old. 
'''
def generate_multiplication_tables(n):
    for i in range(2, 21):
        with open(f"tables/table_{i}.txt", "w") as f:
            for j in range(1, n + 1):
                f.write(f"{i} x {j} = {i * j}\n")
generate_multiplication_tables(10)

