class Calculator:

    def add(self, a: float, b: float) -> float:
        return a + b

    def subtract(self, a: float, b: float) -> float:
        return a - b

    def multiply(self, a: float, b: float) -> float:
        return a * b

    def divide(self, a: float, b: float) -> float:
        if b == 0:
            raise ValueError("Деление на ноль невозможно")
        return a / b

    def power(self, a: float, b: float) -> float:
        return a ** b

    def calculate(self, operation: str, a: float, b: float) -> float:
        operations = {
            'add': self.add,
            'subtract': self.subtract,
            'multiply': self.multiply,
            'divide': self.divide,
            'power': self.power
        }

        if operation not in operations:
            raise ValueError(f"Неизвестная операция: {operation}")

        return operations[operation](a, b)

