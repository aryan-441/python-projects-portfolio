
import secrets

key = secrets.token_bytes(32) #random 32 BYTE key (256 bits)

def generate_key():
    return secrets.token_bytes(32)

def generate_iv():
    return secrets.randbelow(256)


def mix_pair(a,b):
    x = (a+b) % 256
    y = (a+2*b) % 256

    return x,y


def unmix_pair(x,y):
    b = (y-x) % 256 #reverse through basic math
    a = (x-b) % 256

    return a,b


def mix_bytes(data):
    mixed = bytearray()

    
    for i in range(0,len(data), 2):

        #Check whether a second byte exists
        if i + 1 < len(data):
            x,y = mix_pair(data[i], data[i+1])

            mixed.append(x)
            mixed.append(y)

        else:
            
            mixed.append(data[i])

    return bytes(mixed)


def unmix_bytes(data):
    unmixed = bytearray()

    
    for i in range(0,len(data), 2): #step size of 2

        if i + 1 < len(data):
            a,b = unmix_pair(data[i], data[i+1])

            unmixed.append(a)
            unmixed.append(b)

        else:
            unmixed.append(data[i])

    return bytes(unmixed)


def encrypt_bytes(data, key,iv ):

    #ENCRYPTION ALGORITHM: Encrypted_byte = ((original_byte XOR first_selected_key_byte XOR previous_byte) + next_key_byte) % 256  <-- this is a reversible operation
    if not key:
        raise ValueError("Encryption key field cannot be empty.")

    if not 0 <= iv <= 255:
        raise ValueError("IV must be between 0 and 255.")

    #Mix bytes before encryption
    data = mix_bytes(data)

    encrypted = bytearray()

    for i in range(len(data)):
        original_byte = data[i]
        key_byte = key[i%len(key)]
        next_key_byte = key[(i+1) % len(key)]

        if i == 0:
            previous_byte = iv #initialisation vector
        else:
            previous_byte = encrypted[i-1]

        encrypted_byte = ((original_byte ^ key_byte ^ previous_byte) + next_key_byte) % 256
        encrypted.append(encrypted_byte)

    return bytes(encrypted) #converting to bytes because a bytearray object is mutable


def decrypt_bytes(data,key, iv):
    if not key:
        raise ValueError("Decryption key field cannot be empty.")

    if not 0 <= iv <= 255:
        raise ValueError("IV must be between 0 and 255.")

    decrypted = bytearray()

    for i in range(len(data)):
        encrypted_byte = data[i]

        key_byte = key[i%len(key)]
        next_key_byte = key[(i+1)%len(key)]

        if i == 0:
            previous_byte = iv
        else:
            previous_byte = data[i-1]

        #DECRYPTION ALGO: Decrypted_byte = ((encrypted_byte - next_key_byte) % 256) XOR previous_byte XOR key_byte

        decrypted_byte = ((encrypted_byte - next_key_byte) % 256) ^ previous_byte ^ key_byte
        decrypted.append(decrypted_byte)

   
    return unmix_bytes(bytes(decrypted))


if __name__ == '__main__':
    original = b"Hello. This is a test."
    key = bytes([15, 72, 193, 44])
    iv = generate_iv()

    encrypted = encrypt_bytes(original, key, iv)
    decrypted = decrypt_bytes(encrypted, key, iv)

    print("Original:", original.decode("utf-8"))
    print("Encrypted:", encrypted)
    print("Decrypted:", decrypted.decode("utf-8"))

    print("Successfully restored:", original == decrypted)
