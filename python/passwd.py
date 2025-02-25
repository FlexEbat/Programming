import random
import secrets
import os
import string
import time

# Для английских слов
import nltk
from nltk.corpus import words
nltk.download("words")

# Описание программы
def print_instructions():
    print("""
----------------------------------------
    Welcome to the Password Generator App!
----------------------------------------

!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
!BEFORE YOU START USING IT, YOU SHOULD READ THIS HELP!
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

This application helps you generate secure passwords
with different methods and save them to a file.

You can choose from three password generation methods:

1. **Normal Generator** (Method 1) 
   - Generates a password using a mix of uppercase (A-Z),
     lowercase (a-z) letters, digits (0-9), and special
     characters (!@#$%^&*). You can specify the desired
     password length.

2. **Cryptographic Generator** (Method 2) 
   - Generates a cryptographically secure password using the
     `secrets` library. Ideal for sensitive applications
     requiring high security.

3. **Hard Generator** (Method 3) 
   - Generates a strong password by combining random words,
     leet substitutions, random case letters, numbers, and
     special characters.

Once you select a method, the generated password will be saved
in a file called **'passwords.txt'**, along with the name of the
service you're creating the password for.

----------------------------------------
    Good Luck :)
----------------------------------------
""")

# Вызов функции печати инструкций
print_instructions()



service = input("Name of Services: ")
choice = int(input("Your choice (1, 2, or 3): "))

def SimplePassword(password_length):
    Alphabet = list(string.ascii_letters)
    Numbers = list(string.digits)
    SpecialSymbols = list("!@#$%^&*")
    
    # Собираем все символы для генерации пароля
    all_chars = Alphabet + Numbers + SpecialSymbols
    return ''.join(random.choices(all_chars, k=password_length))

def leetify(word):
    """Заменяет буквы на похожие символы"""
    replacements = {"a": "@", "o": "0", "i": "1", "e": "3", "s": "$"}
    return "".join(replacements.get(c.lower(), c) for c in word)

def random_case(word):
    """Меняет регистр букв случайным образом"""
    return "".join(random.choice([c.upper(), c.lower()]) for c in word)

def ComplexGenerator():
    """Генерация сложного пароля из слов"""
    word_list = words.words()
    
    # Берём 3 случайных слова
    selected_words = random.choices(word_list, k=3)
    
    # Применяем случайный регистр и Leet-замены
    transformed_words = [leetify(random_case(word)) for word in selected_words]
    
    # Добавляем случайные цифры в конец каждого слова
    transformed_words = [word + str(random.randint(10, 99)) for word in transformed_words]
    
    # Собираем финальный пароль
    password = "+".join(transformed_words)
    
    # Добавляем случайный спецсимвол в случайное место
    special_chars = "!@#$%^&*()_+=<>?/|"
    insert_pos = random.randint(0, len(password))
    password = password[:insert_pos] + random.choice(special_chars) + password[insert_pos:]
    
    return password

def save_password_to_file(service, password):
    """Сохраняет пароль в файл, дополняя его новыми данными."""
    with open("passwords.txt", "a", encoding="utf-8") as file:
        file.write(f"Service: {service} | Password: {password}\n")
    print(f"Password for {service} saved in passwords.txt")

if choice == 1:
    password_length = int(input("Enter max password length (e.g., 16): "))  # Запрашиваем длину пароля только для SimplePassword
    password = SimplePassword(password_length)  # Сохраняем пароль в переменную
    print(f"Your password: {password}, be safe!")
    save_password_to_file(service, password)  # Теперь передаем переменную password
elif choice == 2:
    password = secrets.token_urlsafe(16)  # Генерация криптографически безопасного пароля
    print(f"Your password: {password}, be safe!")
    save_password_to_file(service, password)  # Теперь передаем переменную password
elif choice == 3:
    password = ComplexGenerator()  # Для сложного генератора тоже сохраняем в переменную
    print(f"Your password: {password}, be safe!")
    save_password_to_file(service, password)  # Передаем в функцию
else:
    print("Invalid choice. Please select 1, 2, or 3.")
