def caesar_encrypt(text, shift):
    encrypted_text = ""
    
    for char in text:
        # Check if character is a letter
        if char.isalpha():
            # Determine the case and base ASCII value
            ascii_base = ord('A') if char.isupper() else ord('a')
            # Convert to 0-25 range, apply shift, and mod 26 to wrap around
            shifted = (ord(char) - ascii_base + shift) % 26
            # Convert back to character
            encrypted_char = chr(shifted + ascii_base)
            encrypted_text += encrypted_char
        else:
            # Keep non-alphabetic characters unchanged
            encrypted_text += char
            
    return encrypted_text

def caesar_decrypt(text, shift):
    # Decryption is just encryption with negative shift
    return caesar_encrypt(text, -shift)

def main():
    print("Caesar Cipher Program")
    print("-------------------")
    
    while True:
        # Get user choice
        print("\n1. Encrypt a message")
        print("2. Decrypt a message")
        print("3. Exit")
        choice = input("Enter your choice (1-3): ")
        
        if choice == '3':
            print("Goodbye!")
            break
            
        if choice not in ['1', '2']:
            print("Invalid choice! Please select 1, 2, or 3.")
            continue
            
        # Get message and shift value
        message = input("Enter your message: ")
        try:
            shift = int(input("Enter shift value (1-25): "))
            if shift < 1 or shift > 25:
                print("Shift value must be between 1 and 25!")
                continue
        except ValueError:
            print("Please enter a valid number!")
            continue
            
        # Process based on choice
        if choice == '1':
            result = caesar_encrypt(message, shift)
            print(f"Encrypted message: {result}")
        else:
            result = caesar_decrypt(message, shift)
            print(f"Decrypted message: {result}")

if __name__ == "__main__":
    main()


#Caesar Cipher Program
-------------------

#1. Encrypt a message
#2. Decrypt a message
#3. Exit
#Enter your choice (1-3): 1
#Enter your message: Hello World!
#Enter shift value (1-25): 3
#Encrypted message: Khoor Zruog!

#1. Encrypt a message
#2. Decrypt a message
#3. Exit
#Enter your choice (1-3): 2
#Enter your message: Khoor Zruog!
#Enter shift value (1-25): 3
#Decrypted message: Hello World!

