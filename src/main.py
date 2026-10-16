import logging
from src.calculator import Calculator

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


def main():
    calculator = Calculator()

    print("Добро пожаловать в калькулятор!")
    print("Доступные операции: +, -, *, /, ^")

    try:
        a = float(input("Введите первое число: "))
        b = float(input("Введите второе число: "))
        operation = input("Введите операцию (+, -, *, /, ^): ")

        operation_map = {
            '+': 'add',
            '-': 'subtract',
            '*': 'multiply',
            '/': 'divide',
            '^': 'power'
        }

        if operation not in operation_map:
            print("Ошибка: Неизвестная операция")
            return

        method_name = operation_map[operation]
        result = calculator.calculate(method_name, a, b)

        logger.info(f"Выполнена операция {operation} с числами {a} и {b}")
        print(f"Результат: {result}")

    except ValueError as e:
        logger.error(f"Ошибка ввода: {e}")
        print(f"Ошибка: {e}")
    except Exception as e:
        logger.error(f"Непредвиденная ошибка: {e}")
        print(f"Произошла ошибка: {e}")


if __name__ == "__main__":
    main()
