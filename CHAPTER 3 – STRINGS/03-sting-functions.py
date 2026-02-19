""" 1st function is len() function which is
used to find the length of string
including spaces and special characters"""
a = "UsmanAnwar63"

print(len(a))

"""2nd functon is sting.endswith() function
which is used to check that string ends with a specific substring
means k jo humny string add ki ha us ky jo last
words hain wo usi py hi end ho rahi ha ya nhi
it returns boolean value True or False"""

a = "UsmanAnwar63"
print(a.endswith("63")) #output: True
print(a.endswith("usman")) #output: False
 
"""same as endswith() function
 3rd function is string.startswith() function"""

a = "UsmanAnwar63"
print(a.startswith("Usman")) #output: True
print(a.startswith("Anwar")) #output: False
    
"""4th function is string.count() function
which is used to count the number of occurrences of a substring in a string"""

a = "UsmanAnwar63"
print(a.count("a")) #output: 3
print(a.count("U")) #output: 1          
print(a.count("z")) #output: 0
print(a.count("63")) #output: 1

"""5th function is string.capitalize() function
 which is used to convert the first character of a string to uppercase"""
a = "usmananwar63"  
print(a.capitalize()) #output: Usmananwar63
a = "usman anwar63"
print(a.capitalize()) #output: Usman anwar63
a = "usman Anwar63" 
print(a.capitalize()) #output: Usman anwar63

"""6th function is string.find() function
which is used to find the index of the first occurrence of a substring in a string
 if substring is not found it returns -1"""
a = "UsmanAnwar63"
print(a.find("Anwar")) #output: 5
print(a.find("z")) #output: -1
print(a.find("a")) #output: 2

"""7th function is string.replace() function
which is used to replace a substring with another substring in a string"""
a = "UsmanAnwar63"
print(a.replace("Anwar", "Khan")) #output: UsmanKhan63  
print(a.replace("a", "o")) #output: UsmonAnwor63
print(a.replace("z", "o")) #output: UsmanAnwar63
print(a.replace("63", "64")) #output: UsmanAnwar64
print(a.replace("63", "")) #output: UsmanAnwar
print(a.replace("", "-")) #output: -U-s-m-a-n-A-n-w-a-r-6-3-
print(a.replace(" ", "-")) #output: UsmanAnwar63

"""8th function is string.lower() function
which is used to convert all characters of a string to lowercase"""
a = "USMANANWAR63"
print(a.lower()) #output: usmananwar63
a = "UsmanAnwar63"
print(a.lower()) #output: usmananwar63
a = "usmananwar63"
print(a.lower()) #output: usmananwar63  
a = "Usman Anwar63"
print(a.lower()) #output: usman anwar63
a = "Usman Anwar 63"
print(a.lower()) #output: usman anwar 63

"""9th function is string.upper() function
which is used to convert all characters of a string to uppercase"""
a = "usmananwar63"
print(a.upper()) #output: USMANANWAR63
a = "UsmanAnwar63"
print(a.upper()) #output: USMANANWAR63
a = "USMANANWAR63"
print(a.upper()) #output: USMANANWAR63
a = "Usman Anwar63"
print(a.upper()) #output: USMAN ANWAR63
a = "Usman Anwar 63"
print(a.upper()) #output: USMAN ANWAR 63

"""10th function is string.title() function
which is used to convert the first character of each word to uppercase"""
a = "usmananwar63"
print(a.title()) #output: Usmananwar63
a = "UsmanAnwar63"
print(a.title()) #output: Usmananwar63
a = "USMANANWAR63"
print(a.title()) #output: Usmananwar63
a = "Usman Anwar63"
print(a.title()) #output: Usman Anwar63
a = "Usman Anwar 63"
print(a.title()) #output: Usman Anwar 63

"""11th function is string.strip() function
which is used to remove leading and trailing whitespace characters from a string"""
a = "   Usman Anwar 63   "
print(a.strip()) #output: Usman Anwar 63
a = "   Usman Anwar 63"
print(a.strip()) #output: Usman An  
a = "Usman Anwar 63   "
print(a.strip()) #output: Usman An

"""11th function is string.split() function
which is used to split a string into a list of substrings based on a specified delimiter"""
a = "Usman Anwar 63"
print(a.split()) #output: ['Usman', 'Anwar', '63']
a = "Usman,Anwar,63"
print(a.split(",")) #output: ['Usman', 'Anwar', '63']