"""
KeyVault - A lightweight and secure password generator built in Python.
"""

import random
import string

def generate_password(length=12, use_special=True):
    # Формуємо набір символів
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation if use_special else ""
    
    all_chars = letters + digits + special
    
    if length < 6:
        print("Попередження: рекомендована довжина пароля — не менше 6 символів.")
    
    # Генеруємо пароль
    password = "".join(random.choice(all_chars) for _ in range(length))
    return password

def main():
    print("=== KeyVault: Генератор паролів ===")
    
    try:
        length = int(input("Введи бажану довжину пароля (за замовчуванням 12): ") or 12)
        special_input = input("Використовувати спецсимволи (!@#$ тощо)? (y/n, за замовчуванням y): ").strip().lower()
        
        use_special = False if special_input == 'n' else True
        
        secure_password = generate_password(length, use_special)
        
        print("\n" + "=" * 30)
        print(f"Твій новий пароль: {secure_password}")
        print("=" * 30)
        
    except ValueError:
        print("Помилка: будь ласка, введи число для довжини пароля.")

if __name__ == "__main__":
    main()
