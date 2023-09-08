from text_to_morse_code import text_to_morse_code

text = input("Input a text you would like to convert to morse code?\n").lower()

output = ""

for char in text:
    try:
        morse = text_to_morse_code[char]
    except KeyError:
        output = f"{char} cannot be converted to morse code"
        break
    else:
        output += morse

print(output)