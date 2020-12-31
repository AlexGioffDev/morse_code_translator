from util import clear, logo
import time

CODE_MORSE_TABLE = {
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--.."
}

def encrypt(message): 
    '''
        Convert a string to a code morse message
        after any char add a space, if the are two 
        space mean there a new world after the last
        char, only alfabeth value
    '''
    if message.replace(' ', '').isalpha():
        message = message.upper()
        encrypt = ''
        for char in message:
            if char != ' ':
                letter = CODE_MORSE_TABLE[char]
                encrypt += letter + ' '
            else:
                encrypt += ' '
        return encrypt
    else:
        print("Please only inser alphabet character")
        return False


def decrypt(message):
    '''
        Convert a Code Morse message in a string
    '''
    if len(message) > 1 and message != '  ':
        message += ' '
        decrypt = ''
        citext = ''
        for letter in message:
            if letter != ' ':
                i = 0

                citext += letter
            else:
                i += 1

                if i == 2:
                    decrypt += ' '
                else:
                    decrypt += list(CODE_MORSE_TABLE.keys())[list(CODE_MORSE_TABLE.values()).index(citext)]
                    decrypt = decrypt.title()
                    citext = ''
        return decrypt
    else:
        return False


if __name__ == '__main__':
    while True:
        clear()
        print(logo)
        print("1) Decrypt a message\n2) Encrypt a message")
        option = input("Select an option? (Write 1 or 2, 'q' to exit): ")

        if option == "1":
            clear()
            print(logo)
            message = input("Write the message: (Only letters please)")
            encrypt_message = encrypt(message)
            if encrypt_message:
                print(f"Here's the message: {encrypt_message}")
                what_to_do = input("Go back to menu or quit? (write q to close): ")
                if what_to_do.lower() == 'q':
                    break
        elif option == "2":
            clear()
            print(logo)
            message = input("Write the message: (example code morse: .--)")
            decrypt_message = decrypt(message)
            if decrypt_message:
                print(f"Here's the message translate: {decrypt_message}")
            what_to_do = input("Go back to menu or quit? (write q to close): ")
            if what_to_do.lower() == 'q':
                break
        elif option.lower() == 'q':
            break
    








