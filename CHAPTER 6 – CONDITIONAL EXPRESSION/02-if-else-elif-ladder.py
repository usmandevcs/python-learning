# now elif conditions example
'''is statement ko aik aur condition add karny 
k liye use kiya jata ha (if) jo statement ha wo aik
bar hi use hoti ha program ma us k bad (elif)
use hoti ha '''

# code example 

a = int(input("Enter your age:"))
if(a>=18):
     print("you are allowed!")

elif(a<=0):
     print("you are entering an invalid age!")

else:
     print("you are not allowed!")

# its also called if else elif ladder