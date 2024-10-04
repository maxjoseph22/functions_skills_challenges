
def encode(text, key):
    cipher = make_cipher(key)
    print(f"* this encode function takes some text e.g. {text} and a key e.g. {key}")
    print(f"* it then uses the key as an input for the make_cipher function (which has not yet been defined), to create a variable 'cipher'")

    ciphertext_chars = []
    
    print(chr(97))
    print(chr(100))
    print(f"* an empty list is generated for the ciphertext_characters")
    print(f"* a for loop starts, iterating over each character in the text {text}")
    print(f"* we create a new variable ciphered_char by running the chr function on the number 65 + the index value of the character we are ciphering")
    for i in text:
        
        ciphered_char = chr(65 + cipher.index(i))
        print(f"{ciphered_char}")
        ciphertext_chars.append(ciphered_char)

    return "".join(ciphertext_chars)


def decode(encrypted, key):
    cipher = make_cipher(key)

    plaintext_chars = []
    for i in encrypted:
        plain_char = cipher[ord(i) - 65]
        plaintext_chars.append(plain_char)

    return "".join(plaintext_chars)


def make_cipher(key):
    alphabet = [chr(i + 96) for i in range(1, 27)]
    cipher_with_duplicates = list(key) + alphabet

    print(f"an 'alphabet' list is created by using the chr() function on a range of numbers from 1 to 26 and adding 98 to each number")

    cipher = []
    for i in range(0, len(cipher_with_duplicates)):
        if cipher_with_duplicates[i] not in cipher_with_duplicates[:i]:
            cipher.append(cipher_with_duplicates[i])

    return cipher

# # When you run this file, these next lines will show you the expected
# # and actual outputs of the functions above.
print(f"""
 Running: encode("theswiftfoxjumpedoverthelazydog", "secretkey")
Expected: EMBAXNKEKSYOVQTBJSWBDEMBPHZGJSL
  Actual: {encode('theswiftfoxjumpedoverthelazydog', 'secretkey')}
""")

print(f"""
 Running: decode("EMBAXNKEKSYOVQTBJSWBDEMBPHZGJSL", "secretkey")
Expected: theswiftfoxjumpedoverthelazydog
  Actual: {decode('EMBAXNKEKSYOVQTBJSWBDEMBPHZGJSL', 'secretkey')}
""")
