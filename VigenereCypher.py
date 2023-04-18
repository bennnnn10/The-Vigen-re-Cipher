#Vargas, Ruben A.
#BSCPE 1-4
#Object-Oriented Programming

#Header design
print("\033[35m•\033[0m" * 58)
print("~" + "\033[;96;1;3mCodeperman\033[0m \033[;1;3mis on duty!\033[0m".center(81) + "~")
print("\033[35m•\033[0m" * 58)

#Ask the name of the user
user_name = input(f"\n\033[;33;1;3mWhat is your name? \033[0m")
print(f"\n\033[;1;3mHey there, \033[;34;1;3m" + user_name + "\033[;1;3m!\033[0m")
print("\033[0m\033[;35;1;3mPlease enter below the text that you want to encrypt!\033[0m")
print("")
print("\033[35m———\033[0m" * 19)

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
print("")
message = input("\033[;33;1;3mYour Message: \033[0m")
message = message.upper()
message = message.replace(" ","")
key = input("\033[;33;1;3mYour Key: \033[0m")
key = key.upper()
key = key.replace(" ","")

#Print the outcome
ciphertext = vigenere_cipher(message, key)
print(f"\n\033[;1;3mWait a bit....\033[0m")
print(f"\n\033[;32;1;3mAnd, done!\033[0m")
print("")
print(f"\n\033[;33;1;3mHere's the generated ciphertext:\033[0m", ciphertext)
print("\033[35m———\033[0m" * 19)

#Ask the user if they want to try it again
while True:
    print(f"\n\033[1;3mDo you want to try it again?\033[0m")
    pick_one = input("\033[40m\033[33;1;3mYES\033[0m \033[1;3mor\033[0m \033[40m\033[0m\033[33;1;3m\033[40mNO\033[0m \033[1;3m? \033[0m")
    if pick_one == "YES":
        print(f"\n")
        print("\033[32m•\033[0m" * 58)
        print("~" + "\033[;96;1;3mCodeperman\033[0m \033[;1;3mis here!\033[0m" .center(81) + "~")
        print("\033[32m•\033[0m" * 58)
        print("")
        print("\033[0m\033[;32;1;3mPlease enter the text below!\033[0m")
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
        print("")
        message = input("\033[;33;1;3mYour Message: \033[0m")
        message = message.upper()
        message = message.replace(" ","")
        key = input("\033[;33;1;3mYour Key: \033[0m")
        key = key.upper()
        key = key.replace(" ","")
#Print the outcome
        ciphertext = vigenere_cipher(message, key)
        print("")
        print(f"\n\033[;33;1;3mHere's the generated ciphertext:\033[0m", ciphertext)
        print("\033[32m———\033[0m" * 19)

    if pick_one == "NO":
        print("")
        print(f"\n\033[31;1;3mCodperman is leaving.....\033[0m")
        break