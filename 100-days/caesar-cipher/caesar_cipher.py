'''
Caesar Cipher (early method of encryption/decryption
'''
logo = """           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
"""
print(logo)
chars = 'abcdefghijklmnopqrstuvwxyz'
allchars = list(chars)
a=0
def encrypt():
    global encrypted_text
    for letter in msg:
        if letter in allchars:
            index = allchars.index(letter)
            new_index = (index + shift_number) % 26
            encrypted_text += allchars[new_index]
        else:
            encrypted_text += letter
    print(encrypted_text)


def decrypt():
    global decrypted_text
    for letter in msg:
        if letter in allchars:
            index = allchars.index(letter)
            new_index = (index - shift_number) % 26
            decrypted_text += allchars[new_index]
        else:
            decrypted_text += letter
    print(decrypted_text)

while a==0:
    choice = input("Do you want to encrypt or decrypt (e/d):  ").lower()
    msg = input("Enter your message:\n").lower()
    shift_number = int(input("Enter your shift number:\n"))
    encrypted_text = ''
    decrypted_text = ''

    if choice == 'e':
        encrypt()
    elif choice == 'd':
        decrypt()
    else:
        print("Invalid choice.")

    again = input("Do you want to perform an operation again (y/n)\n").upper()
    if again != 'Y':
        a = 1
        print("Thanks for trying the Caeser Cipher!")

