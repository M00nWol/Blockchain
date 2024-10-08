from digital_signature import generate_keys, save_keys, load_keys, sign_message, verify_signature

def generate_and_save_keys():
    private_key, public_key = generate_keys()
    save_keys(private_key, public_key)
    print("Keys have been generated and saved.")

def sign_user_message():
    message = input("Enter the message to sign: ").encode()
    try:
        private_key, _ = load_keys()
        signature = sign_message(private_key, message)
        with open('signature.sig', 'wb') as sig_file:
            sig_file.write(signature)
        print(f"Message signed. Signature saved to 'signature.sig'.")
        print(f"Signature: {signature.hex()}")
    except FileNotFoundError:
        print("Key files not found. Please generate keys first.")

def verify_user_signature():
    message = input("Enter the message to verify: ").encode()
    try:
        _, public_key = load_keys()
        with open('signature.sig', 'rb') as sig_file:
            signature = sig_file.read()
        is_valid = verify_signature(public_key, message, signature)
        if is_valid:
            print("Signature is valid.")
        else:
            print("Signature is invalid.")
    except FileNotFoundError:
        print("Signature file or key files not found. Please ensure they are available.")

def main():
    while True:
        print("\nDigital Signature Tool")
        print("1. Generate and Save Keys")
        print("2. Sign a Message")
        print("3. Verify a Signature")
        print("4. Exit")

        choice = input("Select an option: ")

        if choice == '1':
            generate_and_save_keys()
        elif choice == '2':
            sign_user_message()
        elif choice == '3':
            verify_user_signature()
        elif choice == '4':
            print("Exiting the tool.")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
