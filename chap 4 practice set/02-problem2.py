'''this is 2nd problem of chap 4 jis ma hum 
6 students ke numbers input karwayengay
aur unko list ma store karwayengay aur phir
us list ko sort karwayengay aur print karwayengay'''
students = []
n1 = int(input("Enter number of student 1: "))
students.append(n1)
n2 = int(input("Enter number of student 2: "))
students.append(n2)
n3 = int(input("Enter number of student 3: "))
students.append(n3)
n4 = int(input("Enter number of student 4: "))
students.append(n4)
n5 = int(input("Enter number of student 5: "))
students.append(n5)
n6 = int(input("Enter number of student 6: "))
students.append(n6)
print(students)
students.sort()
print("Sorted student numbers are: ", students)