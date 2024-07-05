import re

def check_password_strength(password):
    length_criteria = len(password) >= 8
    uppercase_criteria = bool(re.search(r'[A-Z]', password))
    lowercase_criteria = bool(re.search(r'[a-z]', password))
    number_criteria = bool(re.search(r'[0-9]', password))
    special_char_criteria = bool(re.search(r'[!@#$%^&*(),.?":{}|<>]', password))

    strength = 0
    if length_criteria:
        strength += 1
    if uppercase_criteria:
        strength += 1
    if lowercase_criteria:
        strength += 1
    if number_criteria:
        strength += 1
    if special_char_criteria:
        strength += 1

    feedback = []
    if not length_criteria:
        feedback.append("Password should be at least 8 characters long.")
    if not uppercase_criteria:
        feedback.append("Password should contain at least one uppercase letter.")
    if not lowercase_criteria:
        feedback.append("Password should contain at least one lowercase letter.")
    if not number_criteria:
        feedback.append("Password should contain at least one number.")
    if not special_char_criteria:
        feedback.append("Password should contain at least one special character.")

    strength_levels = {
        0: "Very Weak",
        1: "Weak",
        2: "Medium",
        3: "Strong",
        4: "Very Strong",
        5: "Excellent"
    }

    password_strength = strength_levels[strength]
    
    return password_strength, feedback

def main():
    print("Password Strength Checker")
    password = input("Enter a password to check its strength: ").strip()
    
    strength, feedback = check_password_strength(password)
    
    print(f"Password Strength: {strength}")
    if feedback:
        print("Feedback:")
        for f in feedback:
            print(f"- {f}")

if __name__ == "__main__":
    main()
