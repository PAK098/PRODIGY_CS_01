def caesar_encrypt(text, shift):
    result = ""
    for char in text:
        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)
        else:
            result += chr((ord(char) + shift - 97) % 26 + 97)
    return result

def caesar_decrypt(text, shift):
    result = ""
    for char in text:
        if char.isupper():
            result += chr((ord(char) - shift - 65) % 26 + 65)
        else:
            result += chr((ord(char) - shift - 97) % 26 + 97)
    return result

while True:
    print("1. Encrypt")
    print("2. Decrypt")
    print("3. Terminate The Process")
    choice = input("Choose an option: ")
    if choice == "1":
        text = input("Enter the text to encrypt: ")
        if text.isalpha():
            shift = int(input("Enter the shift value: "))
            encrypted_text = caesar_encrypt(text, shift)
            print(f"Encrypted text: {encrypted_text}")
        else :
              print("Please write text in Alphabets \n")
    elif choice == "2":
        text = input("Enter the text to decrypt: ")
        if text.isalpha():
          shift = int(input("Enter the shift value: "))
          decrypted_text = caesar_decrypt(text, shift)
          print(f"Decrypted text: {decrypted_text}")
        else :
            print("Please write text in Alphabets ! \n")
    elif choice == "3":
        print("Process Terminated !")
        exit()
    else:
        print("Invalid choice. Please choose 1 for encryption or 2 for decryption.")