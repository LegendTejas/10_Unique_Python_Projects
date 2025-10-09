import random
import string

def generate_password(min_length, numbers=True, special_characters=True):
    try:
        if min_length <= 1:
            raise ValueError("Password length must be greater than one.")

        letters = string.ascii_letters
        digits = string.digits
        special = string.punctuation

        characters = letters
        if numbers:
            characters += digits
        if special_characters:
            characters += special

        pwd = ""
        meets_criteria = False
        has_number = False
        has_special = False

        while not meets_criteria or len(pwd) < min_length:
            new_char = random.choice(characters)
            pwd += new_char

            if new_char in digits:
                has_number = True
            elif new_char in special:
                has_special = True

            meets_criteria = True
            if numbers:
                meets_criteria = has_number
            if special_characters:
                meets_criteria = meets_criteria and has_special

        return pwd

    except Exception as e:
        print(f"Error generating password: {e}")
        return ""


try:
    min_length = int(input("Enter the minimum length: "))
    has_number = input("Do you want to have numbers (y/n)? ").strip().lower() == "y"
    has_special = input("Do you want to have special characters (y/n)? ").strip().lower() == "y"

    pwd = generate_password(min_length, has_number, has_special)

    if pwd:
        print("The generated password is:", pwd)
    else:
        print("Password generation failed. Try again.")

except ValueError:
    print("Invalid input! Please enter a valid integer for the password length.")
except KeyboardInterrupt:
    print("\nOperation cancelled by user.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")