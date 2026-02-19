#this is problem 1 of chap 4 jis ma hum user
# say 7 fruit names input karwayengay aur unko list ma store karwayengay
# aur phir us list ko print karwayengay
fruits = []
f1 = input("Enter fruit 1: ")
fruits.append(f1)
f2 = input("Enter fruit 2: ")
fruits.append(f2)
f3 = input("Enter fruit 3: ")
fruits.append(f3)
f4 = input("Enter fruit 4: ")
fruits.append(f4)
f5 = input("Enter fruit 5: ")
fruits.append(f5)
f6 = input("Enter fruit 6: ")
fruits.append(f6)
f7 = input("Enter fruit 7: ")
fruits.append(f7)
print(fruits)
fruits.sort()
print("Sorted fruit list is: ", fruits)