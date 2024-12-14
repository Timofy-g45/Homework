import random

class Encryptor:
    def __init__(self, number):
        self._number = number

    def process(self):
        operation = random.choice(["+", "-", "*", "/"])
        operand = random.randint(7, 65) or 76
        return eval(f"{self._number} {operation} {operand}")

encryptor = Encryptor(10)
result = encryptor.process()
print(f"Оброблений результат {result}")

