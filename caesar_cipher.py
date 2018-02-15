def shift(letter, shift_amount):
    unicode_value = ord(letter) + shift_amount
    
    if unicode_value >= 126:
        unicode_value = 32 + (unicode_value - 126)

    new_letter = chr(unicode_value)

    return new_letter

def encrypt(message, shift_amount):
    encrypt_msg = ''

    for letter in message:
        encrypt_msg += shift(letter, shift_amount)
        
    return encrypt_msg


def decrypt(message, shift_amount):
    return encrypt(message, -1 * shift_amount)

secret_message = "UPPERCASE!!! lowercase. BoTh?"
encrypted_message = encrypt(secret_message, 70)
decrypted_message = decrypt(secret_message, 0)

print(secret_message)
print(encrypted_message)
print(decrypted_message)
