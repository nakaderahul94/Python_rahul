#Write a Python program that takes a string as input and prints the number of times a given character appears in the string.
var1 = input("Enter a string: ")
var2 = input("Enter a character to count: ")
count = var1.count(var2)
print(f"The character '{var2}' appears {count} times in the string.")
