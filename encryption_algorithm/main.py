from cipher import encrypt_bytes, decrypt_bytes, generate_iv, generate_key
from pathlib import Path
import pyautogui 
import shutil
import tkinter as tk
from tkinter import simpledialog

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
    #encrypted_filepath = str(filepath) + '.enc'


    save_file(filepath, bytes([iv]) + encrypted_data)
    return filepath, key

def decrypt_file(filepath, key):
    data = read_file(filepath)
    if not data:
        raise ValueError("The file is empty.")
    iv = data[0] #extract iv
    encrypted_data = data[1:]

    '''key_hex = input("Enter your decryption key:    ")
    try:

        key = bytes.fromhex(key_hex)
    except ValueError:
        print('Invalid key format. Enter a hexadecimal key.')
        return'''
    if len(key) != 32:
        raise ValueError("Invalid key length. Expected 32 bytes.")
    
    decrypted_data = decrypt_bytes(encrypted_data, key, iv)



    save_file(filepath, decrypted_data)
    return filepath


class KeyDialog(simpledialog.Dialog):
    def body(self, master):
        tk.Label(
            master,
            text=(
                "Enter your hexadecimal decryption key:\n\n"
                "WARNING: the file is overwritten IN PLACE. "
                "A wrong key will permanently destroy it."
            ),
            justify=tk.LEFT
        ).grid(row=0, columnspan=2, sticky="w")
        self.entry = tk.Entry(master, name="entry", show="*")
        self.entry.grid(row=1, columnspan=2, padx=5, sticky="we")
        self.entry.bind("<Return>", self.ok)
        self.entry.bind("<Escape>", self.cancel)
        return self.entry

    def buttonbox(self):
        box = tk.Frame(self)
        self.show_var = tk.BooleanVar(master=self)
        tk.Checkbutton(
            box,
            text="Show key",
            variable=self.show_var,
            command=self.toggle_visibility
        ).pack(side=tk.LEFT, padx=5, pady=5)
        tk.Button(
            box, text="OK", width=10, command=self.ok, default=tk.ACTIVE
        ).pack(side=tk.LEFT, padx=5, pady=5)
        tk.Button(
            box, text="Cancel", width=10, command=self.cancel
        ).pack(side=tk.LEFT, padx=5, pady=5)
        self.bind("<Return>", self.ok)
        self.bind("<Escape>", self.cancel)
        box.pack()

    def toggle_visibility(self):
        self.entry.config(show="" if self.show_var.get() else "*")

    def apply(self):
        self.result = self.entry.get()


def ask_key_with_toggle():
    root = tk.Tk()
    root.withdraw()
    dialog = KeyDialog(root, title="Decryption")
    
    result = dialog.result
    root.destroy()
    return result


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
            filepath = filepath.strip().strip('"').strip("'")

        if filepath:

            if not Path(filepath).is_file():
                pyautogui.alert(
                    "The selected file does not exist.",
                    title="Error"
                )

            else:
                confirmation = pyautogui.confirm(
                    text=(
                        f"Encrypt this file?\n\n{filepath}\n\n"
                        "The original file will be OVERWRITTEN."
                        
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
            text="Enter the full path of the encrypted file:",
            title="Select File"
        )
        if filepath:
            filepath = filepath.strip().strip('"').strip("'")
        if filepath:

            if not Path(filepath).is_file():
                pyautogui.alert(
                    "The selected file does not exist.",
                    title="Error"
                )

            

            else:
                
                backup_path = filepath + ".bak"
                backup_choice = pyautogui.confirm(
                    text=(
                        "Create a backup copy of the encrypted file before decrypting?\n\n"
                        f"Backup path:\n{backup_path}"
                    ),
                    title="Create Backup?",
                    buttons=["Yes", "No"]
                )

                proceed = True
                if backup_choice == "Yes":
                    try:
                        shutil.copy2(filepath, backup_path)
                        pyautogui.alert(
                            f"Backup created:\n{backup_path}",
                            title="Backup Created"
                        )
                    except OSError as error:
                        pyautogui.alert(str(error), title="Backup Error")
                        proceed = False
                elif backup_choice == "No":
                    final = pyautogui.confirm(
                        text=(
                            "FINAL WARNING\n\n"
                            "No backup will be made. If the key is wrong, "
                            "the encrypted file will be permanently destroyed "
                            "and cannot be recovered.\n\n"
                            "Continue anyway?"
                        ),
                        title="Final Warning",
                        buttons=["Continue", "Cancel"]
                    )
                    if final != "Continue":
                        pyautogui.alert("Decryption cancelled.", title="Cancelled")
                        proceed = False
                else:
                    proceed = False

                if proceed:

                    key_hex = ask_key_with_toggle()

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
                                    f"File restored in place:\n{decrypted_filepath}"
                                ),
                                title="Decryption Complete"
                            )

                        except (OSError, ValueError) as error:
                            pyautogui.alert(
                                str(error),
                                title="Decryption Error"
                            )
