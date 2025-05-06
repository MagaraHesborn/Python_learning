#conditional statements
# if, elif, else
#They allow a program to make decisions
 
age = int(input("Enter your agae: "))

if age < 18:
    print("You are a minor.")
elif age == 18:
    print("You are just an adult.")
else:
    print("You are an adult.")

#lopps
#for, while
#They allow a program to repeat a block of code multiple times

#while loop
#Repeat a block of code while a condition is true

number = 1
while number < 6:
    print(number)
    number += 1

#for loop
#Repeat a block of code for a specific number of times

for i in range(5):
    print("i")

