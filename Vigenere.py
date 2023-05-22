# Name: Sophia Marie T. Reyes
# Year & Section: BSCpE 1-5
# Laboratory Program: CMPE-103-LAB-EXERCISE-No.-1
# PROBLEM 3 – THE VIGENERE CIPHER
# Date: April 20, 2023
  

# this function provides a value for each character
# from the inputted text to generate an encrypted message

def encryption(message, key):
    encrypt_text = []
    for i in range(len(message)):
        value = (ord(message[i]) + ord(key[i])) % 26
        value += ord("A")
        encrypt_text.append(chr(value))
    return ("".join(encrypt_text))


# this function formats the key based on the 
# length of the inputted text

def key_format(message, key):
    key = list(key)
    if len(message) == len(key):
        return(key)
    else:
        for i in range(len(message) - len(key)):
            key.append(key[i % len(key)])
        return("".join(key))
    

# the user type the message and key
# the output printed is based on the condition met

is_lower = True
while True:
    message = input("\nEnter Message (all uppercase): ")
    keyword = input("\nEnter Keyword (all uppercase): ")
    if message.isupper() and keyword.isupper():
        is_lower == False
        key = key_format(message, keyword)
        encrypt_text = encryption(message, key)
        print("\033[1m", "\nEncrypted message:", encrypt_text)
        break
    else:
        print("Invalid input, please try again.")