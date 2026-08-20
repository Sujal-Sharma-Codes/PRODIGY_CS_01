def caesar_cipher(message, shift):
    result = ""
    for char in message:
        # For uppercase letters
        if char.isupper():
            position = ord(char) - ord('A')
            new_position = (position + shift) % 26
            new_char = chr(new_position + ord('A'))
            result += new_char
        # For lowercase letters
        elif char.islower():
            position = ord(char) - ord('a')
            new_position = (position + shift) % 26
            new_char = chr(new_position + ord('a'))
            result += new_char
        # Keep spaces, numbers and special characters unchanged
        else:
            result += char
    return result
print("===== CAESAR CIPHER =====")
message = input("Enter your message: ")
shift = int(input("Enter shift value: "))
print("\n1. Encrypt")
print("2. Decrypt")
choice = input("Enter your choice: ")
if choice == "1":
    encrypted_message = caesar_cipher(message, shift)
    print("\nEncrypted message:", encrypted_message)
elif choice == "2":
    decrypted_message = caesar_cipher(message, -shift)
    print("\nDecrypted message:", decrypted_message)
else:
    print("\nInvalid choice!")