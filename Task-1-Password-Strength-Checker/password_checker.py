
import math

# Password Strength Checker

common_passwords = [
    "password",
    "123456",
    "12345678",
    "qwerty",
    "admin",
    "password123",
    "welcome",
    "letmein"
]

print("=" * 45)
print("       PASSWORD STRENGTH CHECKER")
print("=" * 45)

password = input("\nEnter your password: ")

# Check password characteristics
length = len(password)
has_upper = any(char.isupper() for char in password)
has_lower = any(char.islower() for char in password)
has_digit = any(char.isdigit() for char in password)
has_symbol = any(not char.isalnum() for char in password)

# Calculate score
score = 0

if length >= 8:
    score += 1

if length >= 12:
    score += 1

if has_upper:
    score += 1

if has_lower:
    score += 1

if has_digit:
    score += 1

if has_symbol:
    score += 1

# Check common passwords
is_common = password.lower() in common_passwords

# Determine password strength
if is_common:
    strength = "Weak"
elif score <= 2:
    strength = "Weak"
elif score <= 4:
    strength = "Medium"
else:
    strength = "Strong"

# Display results
print("\n" + "=" * 45)
print("             ANALYSIS RESULT")
print("=" * 45)

print("Password Length:", length)
print("Uppercase:", has_upper)
print("Lowercase:", has_lower)
print("Digits:", has_digit)
print("Symbols:", has_symbol)
print("Score:", score, "/ 6")

if is_common:
    print("\nWARNING: This is a common password!")

print("\nPassword Strength:", strength)

# Improvement feedback
print("\nSuggestions:")

if length < 12:
    print("- Use at least 12 characters.")

if not has_upper:
    print("- Add uppercase letters.")

if not has_lower:
    print("- Add lowercase letters.")

if not has_digit:
    print("- Include numbers.")

if not has_symbol:
    print("- Include special symbols.")

if is_common:
    print("- Avoid common or easily guessed passwords.")

if strength == "Strong" and not is_common:
    print("- Good! Your password meets all strength checks.")

# Bonus: Estimate time to crack
character_pool = 0

if has_lower:
    character_pool += 26

if has_upper:
    character_pool += 26

if has_digit:
    character_pool += 10

if has_symbol:
    character_pool += 33

if character_pool > 0:
    entropy = length * math.log2(character_pool)
    guesses = 2 ** entropy
    guesses_per_second = 10**10
    seconds = guesses / guesses_per_second

    print("\nEstimated Entropy:", round(entropy, 2), "bits")

    if seconds < 60:
        print("Estimated Crack Time: Less than a minute")
    elif seconds < 3600:
        print("Estimated Crack Time:", round(seconds / 60, 2), "minutes")
    elif seconds < 86400:
        print("Estimated Crack Time:", round(seconds / 3600, 2), "hours")
    elif seconds < 31536000:
        print("Estimated Crack Time:", round(seconds / 86400, 2), "days")
    else:
        print("Estimated Crack Time:", round(seconds / 31536000, 2), "years")

print("\n" + "=" * 45)
print("           CHECK COMPLETED")
print("=" * 45)
