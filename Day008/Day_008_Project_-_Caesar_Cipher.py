# PART-1 - Encryption
# TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
# TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.
# TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message.

# PART-2 - Decryption
# TODO-1: Create a different function called 'decrypt' that takes the 'text' and 'shift' as inputs.
# TODO-2: Inside the 'decrypt' function, shift each letter of the 'text' *backwards* in the alphabet by the shift amount and print the decrypted text.
# TODO-3: Check if the user wanted to encrypt or decrypt the message by checking the 'direction' variable. Then call the correct function based on that 'direction' variable. You should be able to test the code to encrypt *AND* decrypt a message.

# PART-3 - Reorganizing our Code
# TODO-1: Combine the encrypt() and decrypt() functions into a single function called caesar().
# TODO-2: Call the caesar() function, passing over the 'text', 'shift' and 'direction' values.

# PART-4 - User Experience Improvements & Final Touches
# TODO-1: Import and print the logo from art.py when the program starts.
# TODO-2: What if the user enters a shift that is greater than the number of letters in the alphabet?
# TODO-3: What happens if the user enters a number/symbol/space?
# TODO-4: Can you figure out a way to ask the user if they want to restart the cipher program?

from caesar_cipher_logo import logo
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def caesar(plain_text, shift_amount, cipher_direction):
    cipher_text = ""
    if cipher_direction == "decode":
        shift_amount *= -1
    for character in plain_text:
        if character in alphabet:
            position = alphabet.index(character)
            new_letter = alphabet[(position + shift_amount) % len(alphabet)]
            cipher_text += new_letter
        else:
            cipher_text += character
    print(f"The {cipher_direction}d text is {cipher_text}")


print(logo)
should_continue = True
while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(text, shift, direction)

    reply = input("Do you what to continue. Type 'yes' or 'no'").lower()
    if reply == "no":
        should_continue = False
        print("Goodbye")
