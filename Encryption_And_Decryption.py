import random
import string

# Create character set and a shuffled key
chars = list(string.ascii_letters + string.digits + string.punctuation + " ")
key = chars.copy()
random.shuffle(key)

print("=== Simple Substitution Cipher ===")
print("Note: The key is random for this session only.\n")

# ----- ENCRYPTION -----
text = input("Enter a message to ENCRYPT: ")
encrypted_text = ""

for letter in text:
    if letter in chars:
        index = chars.index(letter)
        encrypted_text += key[index]
    else:
        # Keep unknown characters as they are
        encrypted_text += letter

print(f"\nOriginal Message : {text}")
print(f"Encrypted Message: {encrypted_text}")

# ----- DECRYPTION -----
print("\n" + "-" * 40)
decrypted_input = input("Enter a message to DECRYPT (paste the encrypted text): ")
decrypted_text = ""

for letter in decrypted_input:
    if letter in key:
        index = key.index(letter)
        decrypted_text += chars[index]
    else:
        decrypted_text += letter

print(f"\nEncrypted Message: {decrypted_input}")
print(f"Decrypted Message: {decrypted_text}")
