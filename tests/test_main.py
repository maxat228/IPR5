import sys
import io
from unittest.mock import patch
from src.main import main


class TestMain:

    def test_main_with_valid_input(self):
        test_input = ["5", "3", "+"]

        with patch('builtins.input', side_effect=test_input):
            with patch('sys.stdout', new=io.StringIO()) as fake_output:
                main()
                output = fake_output.getvalue()
                assert "Результат: 8" in output

    def test_main_with_division_by_zero(self):
        test_input = ["5", "0", "/"]

        with patch('builtins.input', side_effect=test_input):
            with patch('sys.stdout', new=io.StringIO()) as fake_output:
                main()
                output = fake_output.getvalue()
                assert "Деление на ноль невозможно" in output

    def test_main_with_invalid_operation(self):
        test_input = ["5", "3", "%"]

        with patch('builtins.input', side_effect=test_input):
            with patch('sys.stdout', new=io.StringIO()) as fake_output:
                main()
                output = fake_output.getvalue()
                assert "Неизвестная операция" in output
