# This is the final project for day5
#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))


password =""
for char in range(1, nr_letters + 1):
  string = random.choice(letters)
  password = password + string


for sym in range(1, nr_symbols + 1):
  sign = random.choice(symbols)
  password = password + sign

for num in range(1, nr_numbers + 1):
  num = random.choice(numbers)
  password = password + num


for final_password in range(0, len(password) + 1):
 final_password = random.choice(password)
 random_password = password + final_password

print(f"{random_password}")
