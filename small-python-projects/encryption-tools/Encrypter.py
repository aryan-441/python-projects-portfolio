filepath = input("Enter the filepath here:        ").strip()    #Asks user for filepath and removes blankspaces
try:
    with open(filepath, 'r') as file:     #opens the file in reading mode as variable 'file'
        lines = file.readlines()     #converts lines into a list for individual editing and reads the lines out
    cleanlines = []    #creates an empty list for clean-lines
    for line in lines:  #for loop which reiterates over every line in lines
        if line.strip():     #checks if condition is True
            cleanlines.append(line.strip())    #adds cleaned lines to the list

    cleanedcontent = "\n".join(cleanlines)
except FileNotFoundError:
    print("File not found! Please check the file path.")
except Exception as e:
    print(f"An error occurred: {e}")

def enc(text):
     enctext = ''
     for char in text:
        enctext += enc_map.get(char, char)
     return enctext

encryptedcontent = enc(cleanedcontent)
with open(filepath, 'w') as file:
         
    file.write(encryptedcontent)

    print(f"The file {filepath} has successfully been cleaned and encrypted.")


        



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
    '>': 'ztylw', '?': 'wkxpl', '`': 'njqzw', '~': 'mzpkx', ' ': '-rejv-'
}

dec_map = {value: key for key, value in enc_map.items()}

# Encryption function
def enc(text):
    enctext = ''
    for char in text:
        enctext += enc_map.get(char, char)
    return enctext

# Decryption function
def dec(text):
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

# Main loop
while True:
    choice = input("Do you want to 'encrypt' or 'decrypt'? ").upper()
    if choice == 'ENCRYPT':
        text = input("Enter the text you want to encrypt: ")
        encrypted_text = enc(text)
        print("Encrypted text: ", encrypted_text)
    elif choice == 'DECRYPT':
        text = input("Enter the text you want to decrypt: ")
        decrypted_text = dec(text)
        print("Decrypted text: ", decrypted_text)
    else:
        print("Invalid choice.")

    # Ask if the user wants to continue
    repeat = input("Do you want to perform another operation? (yes/no): ").lower()
    if repeat != 'yes':
        print("Thank you for using the encryption program. Goodbye!")
        break
