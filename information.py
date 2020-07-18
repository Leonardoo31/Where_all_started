# . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
#modules
#.......
import math


#data types :
#1- strings = contains a letter , word or a phrase, we can define it using : '' , "" , """ """ , f" "
family_name = "sandu"
creator_name = "leonard"
full_name = family_name + " " + creator_name
#2- integers = contains a numerical value
number = 10
#3- float = contains a decimal point number
decimal_num = 1.12901
#4- boolean = contains a true\false value (only works with the first letter to be a capital)
is_on = True
#5- complex numbers = they are formated using an imaginar number
complex_num = 1 + 2j
#7- iterables = values who works is usually used in while loops, they can be ranges , strings and lists
print(type(range(0)))


#print function
#..............
print("Application started")
print("Running" + "." * 5)
print("MADE BY: " + creator_name)


#input from user
#...............
name = input("your name is : ")
num1 = int(input(f"pick an number {name} : ")) #we transfrom the standard input value(string) into an integer


#methods
#.......
print(name.upper()) #all letters big
print(name.lower()) #all letters small
print(name.title()) #only first letter of every word big
print(name.strip()) #clears the spaces after the string ("   leo")  #we have also rstrip and lstrip
print(name.find("leonard")) #searches for something and gives back a -1 / 0 value
print(name.replace("leo", "leonard")) #replaces the 1nd value with the second
print("leo" in name) #returns an boolean value if fiinds "leo" in name
print("leo" not in name)#the opossite
print(type(num1)) #print in terminal the type of something


#index positions in strings
name[0] #getting the first character (at index 0)
name[0:-1] #getting the characters from index 2 to the last index (-1) (if you put "-" it counts the position from the end to start)
name[:] #sellect all the string from index 0 to -1


#conditional statements
if "leo" in name:
    print("hey master")
elif "sandu" in name:
    print("hey master's fammily member")
else:
    print("hey " + name)

#short circuit evaluation
name = "master " + name if "leo" in name else "customer " + name
#chaining comparasion operators
if 100 <= num1 < 1000:
    print("why you choose big numbers ? ")


#loops
#1. for loop
for number in range(1, num1, 1):
    print("hello", number)
    if  number < 50:
        print("too much numbers sir")
        break

#2. while loops
number = 100
while number > 0 :
    print(number)
    number //= 2

#nested lopps
for x in range(2):
    for y in range(2):
        print(f"({x}, {y})")

#infinite loop
while True:
    break


#functions (functions can (perform a task) but they return "none", (return a value))
#1- perform a task and the value is only in  the terminal
def calculus(num1, num2):
    print(num1 + num2)
    print(num1 * num2)
calculus(200, 10)

#return a value and store it in a variable
def multiplication(x, y):
    return x * y
result = multiplication(x = 10, y = 55)
print(result)
#print(multiplication(x = 10, y = 55)) #also we can do it like this
