from caesar_cipher import CaesarCipher

def get_valid_shift():
    while True:
        try:
            shift = int(input("Введите значение сдвига (1-25): "))
            if 1 <= shift <= 25:
                return shift
            print("Ошибка: значение сдвига должно быть от 1 до 25")
        except ValueError:
            print("Ошибка: введите целое число")

def show_examples():
    print("\n=== Примеры работы с разным регистром ===")
    cipher = CaesarCipher(shift=3)
    
    examples = [
        "Hello, World!",
        "HELLO, WORLD!",
        "hello, world!",
    ]
    
    for text in examples:
        encrypted = cipher.encrypt(text)
        print(f"\nИсходный текст: {text}")
        print(f"Зашифрованный: {encrypted}")
        print(f"Расшифрованный: {cipher.decrypt(encrypted)}")

def main():
    print("=== Программа шифрования Цезаря ===")
    print("1. Зашифровать текст")
    print("2. Расшифровать текст")
    print("3. Показать примеры")
    print("4. Выход")
    
    while True:
        choice = input("\nВыберите действие (1-4): ")
        
        if choice == "4":
            print("До свидания!")
            break
            
        if choice == "3":
            show_examples()
            continue
            
        if choice not in ["1", "2"]:
            print("Ошибка: выберите 1, 2, 3 или 4")
            continue
            
        shift = get_valid_shift()
        cipher = CaesarCipher(shift=shift)
        
        if choice == "1":
            text = input("Введите текст для шифрования (регистр букв сохраняется): ")
            result = cipher.encrypt(text)
            print(f"\nИсходный текст: {text}")
            print(f"Зашифрованный текст: {result}")
        else:
            text = input("Введите текст для расшифровки (регистр букв сохраняется): ")
            result = cipher.decrypt(text)
            print(f"\nЗашифрованный текст: {text}")
            print(f"Расшифрованный текст: {result}")

if __name__ == "__main__":
    main() 