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
    '>': 'ztylw', '?': 'wkxpl', '`': 'njqzw', '~': 'mzpkx', ' ': '-rejv-'
}

# Decryption map
dec_map = {value: key for key, value in enc_map.items()}

# Encryption function
def enc(text):
    enctext = ''
    for char in text:
        enctext += enc_map.get(char, char)  # Default to the character itself if not found
    return enctext

# Decryption function
def dec(text):
    dectext = ''
    temp = ''
    for char in text:
        temp += char
        if temp in dec_map:
            dectext += dec_map[temp]
            temp = ''  # Reset temp after a successful match
    if temp:  # If leftover characters don't form a valid sequence
        print(f"Warning: Unmatched sequence '{temp}' found.")
    return dectext

# Main Program
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
