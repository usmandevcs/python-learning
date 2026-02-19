# conditional expressions in python 
# why we use conditional expressions 
'''in python programming hum conditional expression/statement
ko us waqt use karty hain jab humy instructions ko 
aik certain condition py execute karwana ho'''
# types  
'''python ma mainly 2 types ki conditins hoti hain
1st is if/else and 2nd is elif'''
# syntax
'''if (condition1): # if condition1 is True 
print ("yes") 
elif(condition2): # if condition2 is True  
print("no") 
else:       # otherwise 
print("maybe")'''     


# code example 

a = int(input("Enter your age:"))

if(a>=18):
     print("congratulations!","you are allowed")
else:
     print("you are not allowed")



# code example 

a = int(input("Enter your age:"))
if(a>=18):
     print("you are allowed!")

elif(a<=0):
     print("you are entering an invalid age!")

else:
     print("you are not allowed!")

# its also called if else elif ladder