name = input("Enter your name: ")
print(f"Your name is {name}.")

#By default input returns a string.
#To work with numbers use int or float to convert the string to a number.

age = input("Enter your age: ")
age = int(age)
print(f"You will be {age + 1} next year")

height = float(input("Enter your height in cm: "))
print(*f"Your height is {height} cm.")
