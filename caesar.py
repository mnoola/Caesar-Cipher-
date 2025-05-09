'''This program implements a Caesar cipher, which is a type of substitution cipher where each letter in the plaintext 
is 'shifted' a certain number of places down or up the alphabet.'''

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']   

def main(direction, message, shift):
    cipher_text = ""
    if direction == "decode":
        shift *= -1

    for letter in message:

        if letter not in alphabet:
            cipher_text += letter
        else:
            shifted_position = alphabet.index(letter) + shift
            shifted_position %= len(alphabet) #modulo operator
            cipher_text += alphabet[shifted_position]
    print(f"The {direction}d text is {cipher_text}")

should_continue = True

while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()

    message = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n")) 
    
    main(direction, message, shift)

    restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n").lower()

    if restart == 'no':
        should_continue = False
        print("Bye")
