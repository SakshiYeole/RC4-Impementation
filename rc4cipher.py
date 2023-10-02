def encrypt(key, plain_text):
    # Initializing state vector S (Step 1)
    S = list(range(256))
    
    # Initializing temporary vector T (Step 2)
    T = list(range(256))
    for i in range(256):
        T[i] = ord(key[i % len(key)])

    # (Step 3)
    j = 0
    for i in range(256):
        j = (j + S[i] + T[i]) % 256
        S[i], S[j] = S[j] , S[i]

    cipher_text = ""
    # Generating pseudo random byte stream (Step 4)
    i = j = 0

    for t in range(len(plain_text)):
        x = ord(plain_text[t])
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S[i], S[j] = S[j], S[i]
        k = (S[i] + S[j]) % 256
        cipher_text += chr(S[k] ^ x)

    return cipher_text

def decrypt(key, cipher_text):
    return encrypt(key, cipher_text)

def print_in_hexadecimal_form(cipher_text):
    print("Cipher Text in Hexadecimal Form: ", end =" ")
    for char in cipher_text:
        print(f"{ord(char):02x} ", end = " ")
    print()

def main():
    key = input("Enter the key: ")
    plain_text = input("Enter the Plain Text: ")
    print()

    print("Encryption: ")
    cipher_text = encrypt(key, plain_text)
    print(f"Cipher Text: {cipher_text}")
    print_in_hexadecimal_form(cipher_text)
    print()

    print("Decryption: ")
    decrypted_cipher_text = decrypt(key, cipher_text)
    print(f"Decrypted Cipher Text: {decrypted_cipher_text}")

if __name__ == "__main__":
    main()
