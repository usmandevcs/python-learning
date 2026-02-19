# Overview
'''A function is a group of statements performing a specific  
task. When a program gets bigger in size and its complexity grows, 
it gets difficult for a program to keep on track that which piece 
of code is doing what!.
A function can be reused by the programmer in a given program 
any number of EXAMPLE AND SYNTAX OF A FUNCTION is ka mtlb ha k
jab humy kai dafa aik hi kam ko code ma karna ha to us ko bar 
bar likhny se better ha k hum functions ka use kary jis se code
sahi aur well defined treeqy se likh saky gy function bnany k 
liye humy us ko name dena hoga jesa k example ma diya gya ha 
name kisko de gy aik piece of logic means jo logic code humny 
bnaya ha usy hum aik name dy gy.name deny se pehly #def use 
kary gy'''
# Function definition 
    # def aur agy sari body ka mtlb function definition ha.
'''The part containing the exact set of instructions which are
executed during the function call.'''

# The syntax 
'''def func1():
    # print("hello")
This function can be called any number of times, anywhere 
in the program.'''
# Example of finding average with a function
def avg():     #this is function definition
    a = int(input("Enter your number:"))
    b = int(input("Enter your number:"))
    c = int(input("Enter your number:"))
    average = (a + b + c)/3
    print(round(average, 2))
"""
round() function value ko round karny mtlb jab value floating 
number ma jaye aur kafi bari ho to usy chota karny k liye 
round function use kiya jata ha aur (average, 2) ka mtlb ha 
kitny figures ma value chahiye.
"""
# Function call 
'''1. ab function ban chuka ha avg k name se agr humy is ko 
run karna ha to humy isy call karna hoga jese k neechy
kiya gya ha apko jitni dafa code run karwana ha utni dafa
function ko call kardy jese mene 2 bar kiya ha'''
'''2. Whenever we want to call a function, we put the name of the
function followed by parentheses as follows: '''
# avg() This is called function call. 
avg()
# benefits
'''ye ha function likhny ka aur us ko call karny ka treeqa
is se code elegant aur clean ho jata ha '''