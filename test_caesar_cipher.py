import unittest
from caesar_cipher import CaesarCipher

class TestCaesarCipher(unittest.TestCase):
    def setUp(self):
        self.cipher = CaesarCipher(shift=3)
        print("\nИнициализация тестов с шифром Цезаря (сдвиг = 3)")
    
    def test_encryption(self):
        print("\n=== Тестирование шифрования ===")
        test_cases = [
            ("HELLO", "KHOOR"),
            ("PYTHON", "SBWKRQ"),
            ("ABC", "DEF"),
            ("XYZ", "ABC"),
            ("HELLO, WORLD!", "KHOOR, ZRUOG!"),
        ]
        
        for input_text, expected in test_cases:
            with self.subTest(input_text=input_text):
                result = self.cipher.encrypt(input_text)
                print(f"Входной текст: {input_text}")
                print(f"Ожидаемый результат: {expected}")
                print(f"Полученный результат: {result}")
                self.assertEqual(result, expected, 
                    f"Ошибка шифрования!\nВходной текст: {input_text}\n"
                    f"Ожидалось: {expected}\nПолучено: {result}")
    
    def test_decryption(self):
        print("\n=== Тестирование расшифровки ===")
        test_cases = [
            ("KHOOR", "HELLO"),
            ("SBWKRQ", "PYTHON"),
            ("DEF", "ABC"),
            ("ABC", "XYZ"),
            ("KHOOR, ZRUOG!", "HELLO, WORLD!"),
        ]
        
        for input_text, expected in test_cases:
            with self.subTest(input_text=input_text):
                result = self.cipher.decrypt(input_text)
                print(f"Зашифрованный текст: {input_text}")
                print(f"Ожидаемый результат: {expected}")
                print(f"Полученный результат: {result}")
                self.assertEqual(result, expected,
                    f"Ошибка расшифровки!\nЗашифрованный текст: {input_text}\n"
                    f"Ожидалось: {expected}\nПолучено: {result}")
    
    def test_case_sensitivity(self):
        print("\n=== Тестирование сохранения регистра ===")
        test_cases = [
            ("Hello", "Khoor"),
            ("HELLO", "KHOOR"),
            ("hello", "khoor"),
            ("HeLlO", "KhOoR"),
        ]
        
        for input_text, expected in test_cases:
            with self.subTest(input_text=input_text):
                result = self.cipher.encrypt(input_text)
                print(f"Входной текст: {input_text}")
                print(f"Ожидаемый результат: {expected}")
                print(f"Полученный результат: {result}")
                self.assertEqual(result, expected,
                    f"Ошибка сохранения регистра!\nВходной текст: {input_text}\n"
                    f"Ожидалось: {expected}\nПолучено: {result}")
                
                decrypted = self.cipher.decrypt(result)
                self.assertEqual(decrypted, input_text,
                    f"Ошибка сохранения регистра при расшифровке!\n"
                    f"Зашифрованный текст: {result}\n"
                    f"Ожидалось: {input_text}\nПолучено: {decrypted}")
    
    def test_invalid_shift(self):
        print("\n=== Тестирование некорректных значений сдвига ===")
        invalid_shifts = [0, 26, -1]
        
        for shift in invalid_shifts:
            with self.subTest(shift=shift):
                print(f"Проверка сдвига: {shift}")
                with self.assertRaises(ValueError):
                    CaesarCipher(shift=shift)
                print(f"✓ Сдвиг {shift} корректно отклонен")

if __name__ == '__main__':
    unittest.main(verbosity=2) 