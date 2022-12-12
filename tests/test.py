import pytest

from app.calc import Calculator


class TestCalc:
    def setup(self): #Обычно в методе setup реализуются необходимые приготовления для запуска тестов
        self.calc = Calculator #В данном случае мы запускаем приложение калькулятора

    def test_multiply_success(self): #Положительный умножение
        assert self.calc.multiply(self, 7, 7) == 49

    def test_division_success(self): #Положительный деление
        assert self.calc.division(self, 666, 111) == 6

    def test_subtraction_success(self): #Положительный вычитание
        assert self.calc.subtraction(self, 18, 6) == 12

    def test_adding_success(self): #Положительный сложение
        assert self.calc.adding(self, 2, 2) == 4

    def test_zero_division(self): #Негативный тест деление на ноль
        with pytest.raises(ZeroDivisionError): #метод .raises тестирует ошибку
            self.calc.division(1, 0)

    def teardown(self): #Метод teardown выполняется в любом случае
        print('Выполнение метода Teardown')