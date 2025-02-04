from typing import Protocol


class Mask(Protocol):
    def adjust_length_for(self, value: str) -> str:
        ...


class EnscryptMask(Mask):
    def __init__(self, mask: int) -> None:
        self.mask = str(bin(mask)[2:])

    def adjust_length_for(self, value: str) -> str:
        repeat_count = len(value) // len(self.mask)
        rest = len(value) % len(self.mask)
        return (self.mask * repeat_count) + self.mask[:rest]


class CipherStrategy(Protocol):
    def process(self, text: str, mask: Mask) -> str:
        ...


class Enscryptor(CipherStrategy):
    def process(self, text: str, mask: Mask) -> str:
        cipher = []
        for char in text:
            unicode_code = ord(char)
            binary_code = bin(unicode_code)[2:].zfill(16)
            adjusted_mask = mask.adjust_length_for(binary_code)

            bits = [int(bit) for bit in binary_code]
            for i in range(len(bits)):
                if adjusted_mask[i] == "1":
                    bits[i] = 0 if bits[i] == 1 else 1

            cipher.append(''.join(str(bit) for bit in bits))
        return "::".join(cipher)


class Decryptor(CipherStrategy):
    def process(self, text: str, mask: Mask) -> str:
        enscrypted_separatedText = text.split("::")
        decrypted_separatedText = []

        for char in enscrypted_separatedText:
            bits = [int(bit) for bit in char]
            adjusted_mask = mask.adjust_length_for(char)

            for i in range(len(bits)):
                if adjusted_mask[i] == "1":
                    bits[i] = 0 if bits[i] == 1 else 1

            decrypted_binary = ''.join(str(bit) for bit in bits)
            decrypted_unicode = int(decrypted_binary, 2)
            decrypted_separatedText.append(chr(decrypted_unicode))

        return ''.join(decrypted_separatedText)


class TextConvertor:
    def __init__(self, encryptor: CipherStrategy, decryptor: CipherStrategy) -> None:
        self.encryptor = encryptor
        self.decryptor = decryptor

    def enscrypt(self, text: str, mask: Mask) -> str:
        return self.encryptor.process(text, mask)

    def decrypt(self, text: str, mask: Mask) -> str:
        return self.decryptor.process(text, mask)


if __name__ == "__main__":
    text = input("Оригінальний текст: ")
    
    mask = EnscryptMask(7342342348)
    encryptor = Enscryptor()
    decryptor = Decryptor()
    convertor = TextConvertor(encryptor, decryptor)

    enscryptedText = convertor.enscrypt(text, mask)
    print(f"\nЗашифрований текст: {enscryptedText}")

    decryptedText = convertor.decrypt(enscryptedText, mask)
    print(f"\nВідновлений текст: {decryptedText}\n")
