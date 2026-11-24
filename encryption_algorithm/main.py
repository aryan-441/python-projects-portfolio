from cipher import encrypt_bytes, decrypt_bytes, generate_iv, generate_key
from pathlib import Path
import pyautogui 

def read_file(filepath):
    with open(filepath, 'rb') as f:
        data = f.read()
    return data
    

def save_file(filepath, data):
    with open(filepath, 'wb') as f:
        f.write(data)

def encrypt_file(filepath):
    data = read_file(filepath)
    key = generate_key()
    iv = generate_iv()
    encrypted_data = encrypt_bytes(data, key, iv)
    encrypted_filepath = str(filepath) + '.enc'


    save_file(encrypted_filepath, bytes([iv]) + encrypted_data)
    return encrypted_filepath, key

def decrypt_file(filepath, key):
    data = read_file(filepath)
    if not data:
        print("The file is empty.")
        return
    iv = data[0] #extract iv
    encrypted_data = data[1:]

    '''key_hex = input("Enter your decryption key:    ")
    try:

        key = bytes.fromhex(key_hex)
    except ValueError:
        print('Invalid key format. Enter a hexadecimal key.')
        return'''
    if len(key) != 32:
        print("Invalid key length. Expected 32 bytes.")
        return
    
    decrypted_data = decrypt_bytes(encrypted_data, key, iv)

    original_path = Path(str(filepath)[:-4])
    decrypted_filepath = original_path.with_name(
        original_path.stem + ".restored" + original_path.suffix
    ) # to remove the enc and get proper suffix placement


    save_file(decrypted_filepath, decrypted_data)
    return decrypted_filepath


if __name__ == "__main__":

    pyautogui.alert(
        text=(
            "This is an experimental encryption programme.\n\n"
            "The algorithm is not cryptographically secure.\n"
            "Only use disposable test files."
        ),
        title="Security Warning"
    )

    choice = pyautogui.confirm(
        text="Choose an operation:",
        title="File Encryption",
        buttons=["Encrypt", "Decrypt", "Cancel"]
    )

    if choice == "Encrypt":

        filepath = pyautogui.prompt(
            text="Enter the full path of the file:",
            title="Select File"
        )

        if filepath:

            if not Path(filepath).is_file():
                pyautogui.alert(
                    "The selected file does not exist.",
                    title="Error"
                )

            else:
                confirmation = pyautogui.confirm(
                    text=(
                        f"Encrypt this file?\n\n{filepath}\n"
                        
                    ),
                    title="Confirm Encryption",
                    buttons=["Yes", "No"]
                )

                if confirmation == "Yes":
                    try:
                        encrypted_filepath, key = encrypt_file(filepath)

                        pyautogui.alert(
                            text=(
                                "Encryption successful.\n\n"
                                f"File saved to:\n{encrypted_filepath}\n\n"
                                f"Decryption key:\n{key.hex()}\n\n"
                                "Store this key safely. "
                                "It cannot be regenerated."
                            ),
                            title="Encryption Complete"
                        )

                    except (OSError, ValueError) as error:
                        pyautogui.alert(
                            str(error),
                            title="Encryption Error"
                        )

    elif choice == "Decrypt":

        filepath = pyautogui.prompt(
            text="Enter the full path of the encrypted .enc file:",
            title="Select File"
        )

        if filepath:

            if not Path(filepath).is_file():
                pyautogui.alert(
                    "The selected file does not exist.",
                    title="Error"
                )

            elif Path(filepath).suffix != ".enc":
                pyautogui.alert(
                    "Please select a .enc file.",
                    title="Error"
                )

            else:
                key_hex = pyautogui.password(
                    text="Enter your hexadecimal decryption key:",
                    title="Decryption",
                    mask="*"
                )

                if key_hex is not None:

                    try:
                        key = bytes.fromhex(key_hex)

                        if len(key) != 32:
                            raise ValueError(
                                "Invalid key length. Expected 64 hexadecimal characters."
                            )

                        decrypted_filepath = decrypt_file(filepath, key)

                        pyautogui.alert(
                            text=(
                                "Decryption completed.\n\n"
                                f"File saved to:\n{decrypted_filepath}"
                            ),
                            title="Decryption Complete"
                        )

                    except (OSError, ValueError) as error:
                        pyautogui.alert(
                            str(error),
                            title="Decryption Error"
                        )
