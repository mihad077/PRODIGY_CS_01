# Function to encrypt the text using Caesar Cipher
def caesar_encrypt(text, shift):
    result = ""

    # Traverse through each character in the text
    for char in text:
        # Check if the character is an uppercase letter
        if char.isupper():
            # Shift character and wrap around if needed
            result += chr((ord(char) + shift - 65) % 26 + 65)
        # Check if the character is a lowercase letter
        elif char.islower():
            # Shift character and wrap around if needed
            result += chr((ord(char) + shift - 97) % 26 + 97)
        # If the character is not a letter, leave it unchanged
        else:
            result += char

    return result


# Function to decrypt the text using Caesar Cipher
def caesar_decrypt(text, shift):
    # Decryption is just encryption with a negative shift
    return caesar_encrypt(text, -shift)


# Main program to interact with the user
def main():
    print("Caesar Cipher Program")

    # Input: Message and shift value
    message = input("Enter your message: ")
    shift = int(input("Enter the shift value (number): "))

    # Input: Choose encryption or decryption
    choice = input("Do you want to (E)ncrypt or (D)ecrypt the message? ").upper()

    if choice == 'E':
        encrypted_message = caesar_encrypt(message, shift)
        print(f"Encrypted Message: {encrypted_message}")
    elif choice == 'D':
        decrypted_message = caesar_decrypt(message, shift)
        print(f"Decrypted Message: {decrypted_message}")
    else:
        print("Invalid choice! Please select either 'E' for encrypt or 'D' for decrypt.")


# Run the main program
if __name__ == "__main__":
    main()
