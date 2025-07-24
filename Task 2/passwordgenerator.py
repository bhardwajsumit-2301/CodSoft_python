import random
import string

def generate_password(password_length):
    """Generates a random password of specified length."""
    if password_length < 4:
        return "Password length should be at least 4 characters for better security."
    

    char_pool = string.ascii_letters + string.digits + string.punctuation

    password_chars = [
        random.choice(string.ascii_uppercase),
        random.choice(string.ascii_lowercase),
        random.choice(string.digits),
        random.choice(string.punctuation)
    ]

    password_chars += random.choices(char_pool, k=password_length - 4)

    random.shuffle(password_chars)

    final_password = ''.join(password_chars)
    return final_password

def main():
    print("🔐 Welcome to the Secure Password Generator!")
    try:
        password_length = int(input("Enter the desired password length: "))
        final_password = generate_password(password_length)
        print(f"Generated Password: {final_password}")
    except ValueError:
        print("❌ Invalid input! Please enter a numeric value.")

if __name__ == "__main__":
    main()