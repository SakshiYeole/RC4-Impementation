# RC4 Cipher Implementation in Python

This Python program implements the RC4 cipher, a symmetric key stream cipher. RC4 is a relatively simple and fast algorithm, but it's important to note that it's considered insecure for many cryptographic applications. In practice, more secure algorithms like AES are recommended.

## Usage

1. **Clone the Repository:**
    ```bash
    git clone https://github.com/SakshiYeole/RC4-Impementation.git
    ```

2. **Run the Example:**
    ```bash
    py rc4_cipher.py
    ```

3. **Output:**
    - The program will demonstrate encryption and decryption of a sample plaintext using the RC4 algorithm.

## Implementation Details

The implementation consists of three main functions:

- `encrypt(key, plain_text)`: Key-Scheduling Algorithm and Pseudo-Random Generation Algorithm is implemented.
- `decrypt(key, cipher_text)`: Decrypts the cipher text using ecrypt method.
- `print_in_hexadecimal_form(text)`: prints the text in hexadecimal form.
## Example

```python
Enter the key: SecretKey  
Enter the Plain Text: Hello, RC4!

Encryption: 
Cipher Text: \ÝP+°^>ð§'∟
Cipher Text in Hexadecimal Form:  5c  dd  50  2b  b0  5e  3e  f0  a7  27  1c

Decryption:
Decrypted Cipher Text: Hello, RC4!
