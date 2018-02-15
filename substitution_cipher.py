alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ ~!@#$%^&*()_+-=`[]{}\|?//><,.:;/'/" 
key = "qwertyuioplkjhgfdsazxcvbnmQWERTYUIOPLKJHGFDSAZXCVBNM /"' ;:.,<.//?|\}{][`=-+_)(*&^%$#@!'

def encrypt(message):
    encrypt_msg = ""

    for letter in message:
        loc = alphabet.find(letter)
        encrypt_msg += key[loc]

    return encrypt_msg

def decrypt(message):
    decrypt_msg = ''

    for letter in message:
        qr = key.find(letter)
        decrypt_msg += alphabet[qr]

    return decrypt_msg


unencrypted_message = "encryption is fun. UPPERCASE? lowercase!"
encrypted_message = encrypt(unencrypted_message)
decrypted_message = decrypt(encrypted_message)

print(unencrypted_message)
print('')
print(encrypted_message)
print(decrypted_message)
