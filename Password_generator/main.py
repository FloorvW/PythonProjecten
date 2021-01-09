import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

total_length = nr_letters + nr_numbers + nr_symbols
password = []
password_str = ""

for amount_of_letters in range(0, int(nr_letters)):
    x = random.randint(0, len(letters) - 1)
    password.append(letters[x])

for amount_of_symbols in range(0, int(nr_symbols)):
    y = random.randint(0, len(symbols) - 1)
    password.append(symbols[y])

for amount_of_numbers in range(0, int(nr_numbers)):
    z = random.randint(0, len(numbers) - 1)
    password.append(numbers[z])

for i in range(0, total_length):
    g = random.randint(0, len(password) - 1)
    password_str = password_str + password[g]
    password.remove(password[g])

print("\n" + password_str)