import secrets
key = secrets.token_bytes(32) #random 32 bit key

def generate_key():
    pass

def encrypt_bytes(data, key,iv ):

    #ENCRYPTION ALGORITHM: Encrypted_byte = ((original_byte XOR first_selected_key_byte) + second_selected_key_byte + previous_byte) % 256  <-- this is a reversible operation
    if not key:
        raise ValueError("Encryption key field cannot be empty.")
    encrypted = bytearray()

    for i in range(len(data)):
        original_byte = data[i]
        key_byte = key[i%len(key)]
        next_key_byte = key[(i+1) % len(key)]

        if i == 0:
            previous_byte = iv #intialising vector
        else:
            previous_byte = encrypted[i-1]
        encrypted_byte = ((original_byte ^ key_byte) + next_key_byte + previous_byte) % 256

        encrypted.append(encrypted_byte)

    return bytes(encrypted) #converting to bytes because a bytearray object is immutable

def decrypt_bytes(data,key, iv):
    if not key:
        raise ValueError("Decryption key field cannot be empty.")
    decrypted = bytearray()

    for i in range(len(data)):
        encrypted_byte = data[i]

        key_byte = key[i%len(key)]
        next_key_byte = key[(i+1)%len(key)]

        if i == 0:
            previous_byte = iv
        else:
            previous_byte = data[i-1]
        
        #DECRYPTION ALGO: Decrypted_byte = ((encrypted_byte - next_key_byte - previous_byte) % 256) XOR key_byte   

        decrypted_byte = ((encrypted_byte - next_key_byte - previous_byte) % 256) ^ key_byte
        decrypted.append(decrypted_byte)

    return bytes(decrypted)

if __name__ == '__main__':
    original = b"Hello. This is a test."
    key = bytes([15, 72, 193, 44])

    encrypted = encrypt_bytes(original, key)
    decrypted = decrypt_bytes(encrypted, key)

    print("Original:", original.decode("utf-8"))
    print("Encrypted:", encrypted)
    print("Decrypted:", decrypted.decode("utf-8"))

    print("Successfully restored:", original == decrypted)
