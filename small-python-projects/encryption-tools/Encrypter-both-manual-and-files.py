# Encryption map
enc_map = {
    'a': 'fewkj', 'b': 'plsmq', 'c': 'rtznv', 'd': 'krzop', 'e': 'mqlsk',
    'f': 'npwtx', 'g': 'ozurv', 'h': 'ytclp', 'i': 'dkqfb', 'j': 'vwzsn',
    'k': 'zxnlm', 'l': 'bftqy', 'm': 'ghprk', 'n': 'jyxzw', 'o': 'rtcvp',
    'p': 'lfwbq', 'q': 'mnzsy', 'r': 'vxtkl', 's': 'pqrwv', 't': 'kjfnc',
    'u': 'wlxzp', 'v': 'smbtr', 'w': 'nzvpq', 'x': 'lkrcy', 'y': 'bhgqn',
    'z': 'prxjt', 'A': 'FEWKJ', 'B': 'PLSMQ', 'C': 'RTZNV', 'D': 'KRZOP',
    'E': 'MQLSK', 'F': 'NPWTX', 'G': 'OZURV', 'H': 'YTCLP', 'I': 'DKQFB',
    'J': 'VWZSN', 'K': 'ZXNLM', 'L': 'BFTQY', 'M': 'GHPRK', 'N': 'JYXZW',
    'O': 'RTCVP', 'P': 'LFWBQ', 'Q': 'MNZSY', 'R': 'VXTKL', 'S': 'PQRWV',
    'T': 'KJFNC', 'U': 'WLXZP', 'V': 'SMBTR', 'W': 'NZVPQ', 'X': 'LKRCY',
    'Y': 'BHGQN', 'Z': 'PRXJT', '0': 'qlrvx', '1': 'tkbzp', '2': 'xmjwf',
    '3': 'yqcrn', '4': 'vzpts', '5': 'nhwdk', '6': 'mjylz', '7': 'xpvqr',
    '8': 'skfrt', '9': 'bgnzw', '!': 'rj4', '@': 'mq2kz', '#': 'tbyqp',
    '$': 'vnclp', '%': 'zjwrm', '^': 'ykptq', '&': 'wsbrv', '*': 'qzjyn',
    '(': 'xmrkt', ')': 'pkvlr', '-': 'twcpz', '_': 'jnbfr', '=': 'krwtv',
    '+': 'mbqyr', '[': 'ytvnw', ']': 'plzcr', '{': 'rqmvz', '}': 'wkfnt',
    '\\': 'zpykl', '|': 'tvqrw', ';': 'wkrpj', ':': 'bqztm', '\'': 'lvyws',
    '"': 'qkptr', ',': 'nrmjw', '.': 'vkzpy', '/': 'jrwpl', '<': 'qmvby',
    '>': 'ztylw', '?': 'wkxpl', '`': 'njqzw', '~': 'mzpkx', ' ': '-rejv-',
    '\n': 'nwl',  '\t': 'tab'
}

# Decryption map, which is the reverse of enc_map
dec_map = {value: key for key, value in enc_map.items()}

# Encryption function
def enc_text(text):
    enctext = ''
    for char in text:
        enctext += enc_map.get(char, char)  # Get the corresponding encrypted character, or leave it unchanged
    return enctext

# Decryption function
# Decryption function
def dec_text(text):
    dectext = ''
    temp = ''
    for char in text:
        temp += char
        if temp in dec_map:  # Check if temp matches a key in dec_map
            dectext += dec_map[temp]  # Append the corresponding character
            temp = ''  # Reset temp after a successful match
    if temp:  # If there are unmatched characters left
        print(f"Warning: Unmatched sequence '{temp}' found.")
    return dectext


# Manual text encryption function
def manual_encrypt():
    text = input("Enter the text you want to encrypt: ")
    encrypted_text = enc_text(text)
    print("Encrypted text: ", encrypted_text)

# Manual text decryption function
def manual_decrypt():
    text = input("Enter the text you want to decrypt: ")
    decrypted_text = dec_text(text)
    print("Decrypted text: ", decrypted_text)

    encodings = ['utf-8', 'ISO-8859-1', 'windows-1252']  # List of encodings to try
    decryptedcontent = ''
    
    for enc in encodings:
        try:
            with open(filepath, 'r', encoding=enc, errors='replace') as file:
                lines = file.readlines()

            # Join the lines without removing any content
            content = ''.join(lines)

            # Decrypt the cleaned content
            decryptedcontent = dec_text(content)

            # If decryption is successful, break out of the loop
            print(f"Decryption successful with encoding {enc}.")
            break
        except Exception as e:
            print(f"Failed to decrypt with encoding {enc}: {e}")
            continue
    
    if not decryptedcontent:
        print("Failed to decrypt the file with all provided encodings.")
    else:
        # Overwrite the file with decrypted content
        try:
            with open(filepath, 'w', encoding='utf-8', errors='replace') as file:
                file.write(decryptedcontent)
            print(f"The file {filepath} has been successfully decrypted.")
        except Exception as e:
            print(f"Error writing decrypted content: {e}")



# File-based decryption function
# File-based encryption function with multiple encoding attempts and error handling

# File-based encryption function with multiple encoding attempts and error handling
def file_encrypt(filepath):
    encodings = ['utf-8', 'ISO-8859-1', 'windows-1252']  # List of encodings to try
    
    for enc in encodings:
        try:
            with open(filepath, 'r', encoding=enc, errors='replace') as file:
                lines = file.readlines()
            
            # Encrypt the content without removing line breaks
            content = ''.join(lines)
            encryptedcontent = enc_text(content)

            # Overwrite the file with encrypted content
            with open(filepath, 'w', encoding='utf-8', errors='replace') as file:
                file.write(encryptedcontent)

            print(f"The file {filepath} has successfully been cleaned and encrypted using encoding {enc}.")
            break
        except Exception as e:
            print(f"Failed to encrypt with encoding {enc}: {e}")
            continue


# Main menu to choose between encryption, decryption, and file-based operations
def main():
    while True:
        choice = input("Do you want to 'encrypt' or 'decrypt' text manually, or 'encrypt'/'decrypt' a file? (manual/file): ").lower()
        
        if choice == 'manual':
            action = input("Do you want to 'encrypt' or 'decrypt' the text? (encrypt/decrypt): ").lower()
            if action == 'encrypt':
                manual_encrypt()
            elif action == 'decrypt':
                manual_decrypt()
            else:
                print("Invalid choice.")
        elif choice == 'file':
            action = input("Do you want to 'encrypt' or 'decrypt' the file? (encrypt/decrypt): ").lower()
            filepath = input("Enter the file path here: ").strip()
            if action == 'encrypt':
                file_encrypt(filepath)
            elif action == 'decrypt':
                file_decrypt(filepath)
            else:
                print("Invalid choice.")
        else:
            print("Invalid choice. Please type 'manual' or 'file'.")
        
        # Ask if the user wants to continue
        repeat = input("Do you want to perform another operation? (yes/no): ").lower()
        if repeat != 'yes':
            print("Thank you for using the encryption program. Goodbye!")
            break

# Run the main function
if __name__ == "__main__":
    main()
