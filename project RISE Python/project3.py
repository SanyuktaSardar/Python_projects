import random

print("Welcome to the PyPassword Generator!")
logo = '''

██████╗  █████╗ ███████╗███████╗██╗    ██╗ ██████╗ ██████╗ ██████╗      ██████╗ ███████╗███╗   ██╗███████╗██████╗  █████╗ ████████╗ ██████╗ ██████╗ 
██╔══██╗██╔══██╗██╔════╝██╔════╝██║    ██║██╔═══██╗██╔══██╗██╔══██╗    ██╔════╝ ██╔════╝████╗  ██║██╔════╝██╔══██╗██╔══██╗╚══██╔══╝██╔═══██╗██╔══██╗
██████╔╝███████║███████╗███████╗██║ █╗ ██║██║   ██║██████╔╝██║  ██║    ██║  ███╗█████╗  ██╔██╗ ██║█████╗  ██████╔╝███████║   ██║   ██║   ██║██████╔╝
██╔═══╝ ██╔══██║╚════██║╚════██║██║███╗██║██║   ██║██╔══██╗██║  ██║    ██║   ██║██╔══╝  ██║╚██╗██║██╔══╝  ██╔══██╗██╔══██║   ██║   ██║   ██║██╔══██╗
██║     ██║  ██║███████║███████║╚███╔███╔╝╚██████╔╝██║  ██║██████╔╝    ╚██████╔╝███████╗██║ ╚████║███████╗██║  ██║██║  ██║   ██║   ╚██████╔╝██║  ██║
╚═╝     ╚═╝  ╚═╝╚══════╝╚══════╝ ╚══╝╚══╝  ╚═════╝ ╚═╝  ╚═╝╚═════╝      ╚═════╝ ╚══════╝╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝

'''

print(logo)

file_path = 'Password.txt'

lower_letters = list('abcdefghijklmnopqrstuvwxyz')
upper_letters = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
numbers = list('123456789')
symbols = list('!@#$%^&*()[]')

choice = input("Type 'c' to create a password or 'd' to detect password strength: ").lower()

# ---------------- PASSWORD CREATION ----------------
if choice == 'c':
    while True:
        try:
            letters_password = int(input("How many letters would you like in your password? "))
            symbol_password = int(input("How many symbols would you like? "))
            numbers_password = int(input("How many numbers would you like? "))

            if letters_password < 0 or symbol_password < 0 or numbers_password < 0:
                print("❌ Please enter non-negative numbers only.\n")
                continue

            total_length = letters_password + symbol_password + numbers_password

            if total_length >= 12:
                break
            else:
                print(f"⚠️ Your password must be at least 12 characters long. Currently: {total_length}\n")
        except ValueError:
            print("❌ Invalid input! Please enter numbers only.\n")

    password_user = []

    # Distribute upper and lower letters
    if letters_password > 1:
        no_up_l = random.randint(1, letters_password - 1)
    else:
        no_up_l = 1
    no_l_l = letters_password - no_up_l

    for _ in range(no_up_l):
        password_user.append(random.choice(upper_letters))

    for _ in range(no_l_l):
        password_user.append(random.choice(lower_letters))

    for _ in range(symbol_password):
        password_user.append(random.choice(symbols))

    for _ in range(numbers_password):
        password_user.append(random.choice(numbers))

    random.shuffle(password_user)
    password = ''.join(password_user)

    print("-" * 60)
    print(f"✅ Your generated password is: {password}")
    print("-" * 60)

    try:
        with open(file_path, 'a') as file:
            file.write(password + "\n")
        print("💾 Password saved to Password.txt")
    except Exception as e:
        print(f"❌ Failed to save password to file: {e}")

# ---------------- PASSWORD STRENGTH DETECTOR ----------------
elif choice == 'd':
    your_password = input("Enter your password: ")
    u_letter_present = any(char in upper_letters for char in your_password)
    l_letter_present = any(char in lower_letters for char in your_password)
    number_present = any(char in numbers for char in your_password)
    symbol_present = any(char in symbols for char in your_password)

    length = len(your_password)
    print("\nAnalyzing password...")

    if u_letter_present and l_letter_present and number_present and symbol_present and length >= 12:
        print("✅ Strong Password 🎉")
        want_store = input("Do you want to store this password? (yes/no): ").lower()
        if want_store == 'yes':
            try:
                with open(file_path, 'a') as file:
                    file.write(your_password + "\n")
                print("💾 Password saved successfully.")
            except Exception as e:
                print(f"❌ Failed to save password: {e}")
    elif length < 12:
        print(f"⚠️ Medium Password: Your password length is {length}. Please add {12 - length} more characters.")
    else:
        print("😐 Medium Password: Missing some elements:")
        if not u_letter_present:
            print("• Add UPPERCASE letters")
        if not l_letter_present:
            print("• Add lowercase letters")
        if not number_present:
            print("• Add numbers")
        if not symbol_present:
            print("• Add symbols")

else:
    print("❌ Invalid choice. Please run the program again and type 'c' or 'd'.")
