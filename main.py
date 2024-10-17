# Password Generator Project
import random  # Import the random module to use for generating random values

# Define the lists of possible characters for the password
letters = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
    'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
    'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

password = ""  # Initialize an empty string to store the generated password

# Print a welcome message for the user
print("Welcome to the PyPassword Generator!")

# Ask the user for the number of letters, symbols, and numbers they want in the password
nr_letters = int(input("How many letters would you like in your password? \n"))
nr_symbols = int(input(f"How many symbols would you like? \n"))
nr_numbers = int(input(f"How many numbers would you like? \n"))

# Add random letters to the password
for i in range(1, nr_letters + 1):
    letter_index = random.randint(0, len(letters) - 1)  # Generate a random index for letters list
    password += letters[letter_index]  # Add the randomly selected letter to the password

# Add random symbols to the password
for i in range(1, nr_symbols + 1):
    symbol_index = random.randint(0, len(symbols) - 1)  # Generate a random index for symbols list
    password += symbols[symbol_index]  # Add the randomly selected symbol to the password

# Add random numbers to the password
for i in range(1, nr_numbers + 1):
    number_index = random.randint(0, len(numbers) - 1)  # Generate a random index for numbers list
    password += numbers[number_index]  # Add the randomly selected number to the password

# Convert the password string to a list to allow shuffling
password_array = []
for i in password:
    password_array.append(i)

# Shuffle the characters in the password list to randomize the order
random.shuffle(password_array)

# Print the final randomized password
print(f"Here is your randomized password: {''.join(password_array)}")
