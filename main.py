# 100 Days of Code Practice Project
# Caesar Cipher 

from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# Cipher logic
# Encodes or Decodes input from the user by shifting through the alphabet list
def caesar(start_text, shift_amount, cipher_direction):
  message = ""
  for letter in text:
    if letter in alphabet:
      position = alphabet.index(letter)
      if direction == "encode":
        new_position = position + shift
        message += alphabet[new_position]
      elif direction == "decode":
        new_position = position - shift
        message += alphabet[new_position]
    else:
      message += letter
    
  print(f"Here's the {cipher_direction}d result: {message}\n")

print(logo)

should_continue = True
while should_continue:
  # Main program will loop over and over until user inputs no 
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  shift = shift % 26
  caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
  result = input("Type 'yes' to run program again. Otherwise type 'no'.\n")
  if result == 'no':
    should_continue = False
    print("Goodbye")
