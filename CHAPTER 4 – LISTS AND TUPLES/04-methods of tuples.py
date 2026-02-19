#methods of tuples
# 1st method of tuple is tuple.count() e.g;
a = (1,2,3,3,4,5)
print(a.count(3)) #it will count the number of times 3 is in tuple
# 2nd method of tuple is tuple.index() e.g; 
print(a.index(4)) #it will return the index of first occurence of 4
# if the item is not found it will raise a ValueError
# print(a.index(6)) #it will raise ValueError because 6 is not in tuple
#3rd method of tuple is tuple.len() e.g;
print(len(a)) #it will return the length of tuple
#4th method of tuple is tuple.sorted() e.g;
print(sorted(a)) #it will return a sorted list of tuple items
#5th method of tuple is tuple.min() e.g;
print(min(a)) #it will return the minimum item of tuple
#6th method of tuple is tuple.max() e.g;
print(max(a)) #it will return the maximum item of tuple
#7th method of tuple is tuple.sum() e.g;
print(sum(a)) #it will return the sum of all items in tuple
#8th method of tuple is concatenation e.g;
b = (6,7,8)
c = a + b #it will concatenate two tuples
print(c)

