from caesar_cipher import CaesarCipher

def demonstrate_basic_usage():
    print("\n=== Базовое использование шифра Цезаря ===")
    cipher = CaesarCipher(shift=3)
    message = "Hello, World!"
    
    print(f"Исходное сообщение: {message}")
    encrypted = cipher.encrypt(message)
    print(f"Зашифрованное: {encrypted}")
    decrypted = cipher.decrypt(encrypted)
    print(f"Расшифрованное: {decrypted}")

def demonstrate_different_shifts():
    print("\n=== Работа с разными значениями сдвига ===")
    message = "Hello, World!"
    
    for shift in [1, 5, 10, 25]:
        cipher = CaesarCipher(shift=shift)
        encrypted = cipher.encrypt(message)
        decrypted = cipher.decrypt(encrypted)
        print(f"\nСдвиг {shift}:")
        print(f"  Исходное: {message}")
        print(f"  Зашифрованное: {encrypted}")
        print(f"  Расшифрованное: {decrypted}")

def demonstrate_special_cases():
    print("\n=== Особые случаи ===")
    cipher = CaesarCipher(shift=3)
    
    print("\nЦиклический сдвиг:")
    message = "XYZ"
    encrypted = cipher.encrypt(message)
    print(f"  Исходное: {message}")
    print(f"  Зашифрованное: {encrypted}")
    
    print("\nСпециальные символы:")
    message = "Hello! @#$%^&*()_+ 123"
    encrypted = cipher.encrypt(message)
    print(f"  Исходное: {message}")
    print(f"  Зашифрованное: {encrypted}")
    
    print("\nПустая строка:")
    message = ""
    encrypted = cipher.encrypt(message)
    print(f"  Исходное: '{message}'")
    print(f"  Зашифрованное: '{encrypted}'")

def demonstrate_case_sensitivity():
    print("\n=== Работа с разным регистром букв ===")
    cipher = CaesarCipher(shift=3)
    
    print("\nСмешанный регистр:")
    message = "HeLlO, WoRlD!"
    encrypted = cipher.encrypt(message)
    print(f"  Исходное: {message}")
    print(f"  Зашифрованное: {encrypted}")
    
    print("\nТолько строчные:")
    message = "hello, world!"
    encrypted = cipher.encrypt(message)
    print(f"  Исходное: {message}")
    print(f"  Зашифрованное: {encrypted}")
    
    print("\nТолько заглавные:")
    message = "HELLO, WORLD!"
    encrypted = cipher.encrypt(message)
    print(f"  Исходное: {message}")
    print(f"  Зашифрованное: {encrypted}")

def main():
    print("=== Демонстрация работы шифра Цезаря ===")
    print("Этот файл показывает различные примеры использования шифра Цезаря.")
    
    demonstrate_basic_usage()
    demonstrate_different_shifts()
    demonstrate_special_cases()
    demonstrate_case_sensitivity()
    
    print("\n=== Демонстрация завершена ===")

if __name__ == "__main__":
    main() 