#Python Variables
    #Variables are containers for storing data values.
    # Python has no command for declaring Variables.
    # A variable is created the moment we first assign a value to it.
    #Casting -- if we want to specify the data type of a variable, this can be done with casting.


a=str(3)  # a will be string with value '3'
b=int(3)  # b will be integer 3
c=float(3) # c will be float type with value 3.0
print(a,b,c)   
print(type(a)) 
print(type(b))
print(type(c))      
   # Variable Names -----
    # A variable can have a short name(like x and y) or  a more descriptive name (like age, carname, total_volume)
    # A variable name must start with a letter or underscore
    #A variable name cannot start with a number
    #A variable name can only contain alpha-numeric characters(A-z, 0-9, and _)
    #Variable names are case-sensitive(age Age and AGE are three differenet variables)
    # Python Variables--- 
    #Assign Multiple values
i,j,k="Orange","Banana","Cherry"
print(i)
print(j)
print(k)
#One values to Multiple Variables
l=m=n="Orange"
print(l)
print(m)
print(n)
   # Unpack a collection
   #  if we have a collection of values in a list, tuple etc.
   #  Python allows you to extract the values into variables. This is called unpacking.
fruits=["apple","banana","cherry"]
x1,y1,z1=fruits
print(x1)
print(y1)
print(z1)
     # Output Variables:
     # The python print() function is often used to output variables.
x="Python is awesome"
print(x)
   # In the print() function, we can output multiple variables, seperated using comma:
   #example:
a1="Python"
a2="is"
a3="Awesome"
print(a1,a2,a3)
   #We can also use the + operator to output multiple variables
a4="Python "
a5="is "
a6="Awesome"
print(a4+a5+a6)
  # Notice the space after "Python " and "is ", without them the result would be "PythonisAwesome".
  #For numbers the + character works as a mathematical operator.
a7=5
a8=22
print(a7+a8)
  # The best way to multiple variables in the print() function is to seperate them with commas, which even
  # support different data types:
x=5
y="John"
print(x,y)
# Global Variables:
# Variables that are created outside of a function(as in all of the above examples) are known as 
# Global Variables.
# They can be used by everyone, both inside the function and outside the function
# Example:
b1="awesome"

def myfunc():
    print("Python is "+b1)
myfunc()
# If we create a variable with the same name inside a function, this variable will be local, and can only
# be used inside the function.
# The global variable with the same name will remain as it was, global and with the original value.
a11="awesome"

def myfunc():
    a11="fantastic"
    print("Python is "+a11)

myfunc()

print("Python is "+a11)

#The Global Keyword :
 