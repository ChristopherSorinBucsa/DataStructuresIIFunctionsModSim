"""
Name: Christopher Bucsa
"""
import math
"""
Problem 1
"""
print("\n",40*"-","\n","Problem 1:\n",40*"-")
# Your code goes here:

# Create function:
def equation(x):
    y = (1) / (1 + math.e**-x)
    return y

# Use for loop, inside - call function:
for x in range(-5,6):
    y = equation(x)
    print(f"({x}, {y: .2f})")     
"""
Problem 2
"""
print("\n",40*"-","\n","Problem 2:\n",40*"-")
# Your code goes here:
 
# Create the function:
def equation2(x,y):
    r = math.sqrt(x**2 + y**2)
    return r 

# Use for-loop, can also use list [-5,0,5] instead of range and use those values instead
for e in range(-5,6):
    x = e
    y = e
    if e == -5 or e == 0 or e == 5:
        r = equation2(x,y) 
        print(f"({e},{e}) = {r:.2f}")
"""
Problem 3
"""
print("\n",40*"-","\n","Problem 3:\n",40*"-")
# Your code goes here:
    
# Function Implementation: 
def extractor(name):
    elements = name.split() # Split the name into 2 parts
    first_name = elements[0] # Retrieve first name and store in variable
    last_name = elements[1] # Retrieve last name and store in variable
    initials = first_name[0].upper() + last_name[0].upper() # Retrieve first letter of first/last names and capitalize
    return initials 
    
# Testing Function and Printing Result:
my_name = "Christopher Bucsa" 
initials = extractor(my_name)
print(initials)  
"""
Problem 4
"""
print("\n",40*"-","\n","Problem 4:\n",40*"-")
# Your code goes here:

# Function implementation 
def occurence(sequence):
    dictionary = {} 
    # Iterate through sequence
    for e in sequence: 
        if e in dictionary: # if element is already in dictionary, we can add to its total count
            dictionary[e] = dictionary[e] + 1
        else: # otherwise, we can create new key in dictionary and initialize its value at 1
            dictionary[e] = 1
    return dictionary 

# Testing and Printing Results
text = "Mississippi"
num_list = [72, 70, 75, 70, 72, 72, 71]

print(occurence(text))
print(occurence(num_list))

"""
Problem 5
"""
print("\n",40*"-","\n","Problem 5:\n",40*"-")
# Your code goes here:

def list_stats(list):
    largest_value= max(list)
    smallest_value = min(list)
    total = sum(list) 
    average = int((total) / (len(list)))
    return print("Max value in list:", largest_value, "\nLowest value in list:", smallest_value,
                  "\nSum of elements in list:", total, "\nMean of elements:", average)

list1 = [2,-1, 10, 5]
list2 = [10,8,6,4,2,0,-2,-4,-6,-8,-10]
list3 = [4]
list4 = [1,1,2,3,5,8,13]

list_stats(list1) 
print("\n")
list_stats(list2) 
print("\n")
list_stats(list3) 
print("\n")
list_stats(list4) 
"""
Problem 6
"""
print("\n",40*"-","\n","Problem 6:\n",40*"-")
# Your code goes here:
    
def summation(n,p):
     total2 = 0
     for e in range(1,n+1):
         total2 = total2 + (1) / (e**p)
     return total2 
 
n = 200
p1 = 1/2
p2 = 1
p3 = 2 
p4 = 3

print(summation(n,p1))
print(summation(n,p2))
print(summation(n,p3))
print(summation(n,p4))

print("\n The results of the sums for the different exponents(p) make sense." 
      " Since our equation is taking 1 over an increasingly higher number (due to the increasing value of p expoent)," 
      "it is expected that the sum will get progressively smaller, as shown in the output above.")
