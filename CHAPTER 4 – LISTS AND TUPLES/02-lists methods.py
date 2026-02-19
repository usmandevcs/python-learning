''' strings k function/methods ki tarah lists k methods bhi hote hain
lekin thory different hote hain.jesa we know strings are immutable
to us k methods sirf string k copy return karte hain means 
new string return karte hain lekin lists k methods original list 
ko change karte hain.'''
# for example:
friends = ['ali', 'ahmed', 'apple',23,45.6,True]
print(friends)
#list methods
#1.append() method
friends.append('banana') #it add banana at the end of list
print(friends)
#2.insert() method
friends.insert(1,'orange') #it add orange at index 1
print(friends)
#3.remove() method
friends.remove('apple') #it remove apple from list
print(friends)
#4.pop() method
friends.pop() #it remove last item from list
print(friends)
friends.pop(2) #it remove item at index 2
print(friends)
#5.clear() method
friends.clear() #it remove all items from list 
print(friends)
#6.sort() method
friends.sort() #it sort the list in ascending order
print(friends)
#7.reverse() method
friends.reverse() #it reverse the list
print(friends)
#8.count() method
print(friends.count('ali')) #it count the number of times ali is in list
#9.extend() method
friends.extend(['kiwi','grape']) #it add multiple items to the end of list
print(friends)