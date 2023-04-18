#Vargas, Ruben A.
#BSCPE 1-4
#Object-Oriented Programming

#Ask the name of the user
user_name = input(f"\nWhat is your name? ")
print(f"\nHey there, " + user_name + "!")
print("Please enter below the text that you want to encrypt!")

#Create a python program using Vigenère Cipher to encrypt the message
def vigenere_cipher(message, key):
    #Convertion of message and key to their specific numerical numbers
    convert_message = [ord(i) - 65 for i in message]
    convert_key = [ord(i) - 65 for i in key]

    #Encrypt the message using Vigenère Cipher
    cipher = []
    for i in range(len(convert_message)):
        encrypted_value = (convert_message[i] + convert_key[i % len(key)]) % 26
        cipher.append(encrypted_value)

    #Ciphertext numerical numbers to letters
    ciphertext = ''.join([chr(encrypted_value + 65) for encrypted_value in cipher])
    return ciphertext

#Ask the user to enter the message and key
message = input("Your Message: ")
message = message.upper()
message = message.replace(" ","")
key = input("Your Key: ")
key = key.upper()
key = key.replace(" ","")

#Print the outcome
