# Name: Sophia Marie T. Reyes
# Year & Section: BSCpE 1-5
# Laboratory Program: CMPE-103-LAB-EXERCISE-No.-1
# PROBLEM 2 – DECRYPTION
# Date: April 1, 2023

plain_text = input("Type your string input: ")

# dictionary for converting special characters into vowels
converter = {
    "*": "a",
    "&": "e",
    "#": "i",
    "+": "o",
    "!": "u",
}

# checking each character and printing an output

output = ""
for ch in plain_text:
    output += converter.get(ch, ch)
print("\033[95m", f"\nResult: {output}")
