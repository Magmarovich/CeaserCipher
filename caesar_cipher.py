class CaesarCipher:
    def __init__(self, shift: int):
        if not 1 <= shift <= 25:
            raise ValueError("Сдвиг должен быть в диапазоне от 1 до 25")
        self.shift = shift
        self.upper_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        self.lower_alphabet = 'abcdefghijklmnopqrstuvwxyz'
    
    def _shift_char(self, char: str, shift: int) -> str:
        if char in self.upper_alphabet:
            idx = self.upper_alphabet.index(char)
            new_idx = (idx + shift) % 26
            return self.upper_alphabet[new_idx]
        elif char in self.lower_alphabet:
            idx = self.lower_alphabet.index(char)
            new_idx = (idx + shift) % 26
            return self.lower_alphabet[new_idx]
        return char
    
    def encrypt(self, message: str) -> str:
        return ''.join(self._shift_char(char, self.shift) for char in message)
    
    def decrypt(self, encrypted_message: str) -> str:
        return ''.join(self._shift_char(char, -self.shift) for char in encrypted_message) 