import lib
import pytest

# Тест функции, возвращающей последовательность Фибоначи до заданного числа n
class TestFib:

    # Тестируем программу на коррктных данных. Функция возвращает списко элементов.
    def test_on_correct_n(self):
        assert lib.fibonacci(7) == [1, 1, 2, 3, 5, 8, 13]

    # Тестируем программу на некоррктных данных. Функция возвращает списко элементов.
    def test_on_uncorrect_n(self):
        assert lib.fibonacci(7) == [1, 1, 2, 3, 5, 8, 13]

class TestIsOrdered:

    # Функция возвращает данные для выполнения теста - упорядоченный от мин к макс список
    @pytest.fixture
    def ordered_example(self):
        return [1, 2, 3]

    # Функция возвращает данные для выполнения теста - неупорядоченный список
    @pytest.fixture
    def unordered_example(self):
        return [1, 3, 2]

    # Функция возвращает данные для выполнения теста - массив равных по величине значений
    @pytest.fixture
    def equal_example(self):
        return [1, 1, 1]

    # Тест функции на упорядоченных от мин к макс значениях
    def test_on_ordered(self, ordered_example):
        assert lib.bubble_sort(ordered_example) == [1, 2, 3]

    # Тест функции на неупорядоченных значениях
    def test_on_unordered(self, unordered_example):
        assert lib.bubble_sort(unordered_example) == [1, 2, 3]

    # Тест функции на равных по величине значениях
    def test_on_equal(self, equal_example):
        assert lib.bubble_sort(equal_example) == [1, 1, 1]

class TestCalc:

    # Тестируем программу на коррктных данных. Функция возвращает резульлтат мат.операции
    def test_plus(self):
        assert lib.calc(1,2,"+") == 3

    # Тестируем программу на коррктных данных. Функция возвращает резульлтат мат.операции
    def test_minus(self):
        assert lib.calc(1,2,"-") == -1

    # Тестируем программу на коррктных данных. Функция возвращает резульлтат мат.операции
    def test_del(self):
        assert lib.calc(1,2,"/") == 0.5

    # Тестируем программу на коррктных данных. Функция возвращает резульлтат мат.операции
    def test_umn(self):
        assert lib.calc(1, 2, "*") == 2


    # Тестируем программу на некоррктных данных. Функция вызывает исключение IndexError.
    def test_on_zero(self):
        # Когда мы подаем на вход программе число 0 - функция поиска простых чисел завершается с ошибкой.
        # Данная строчка показывает, что внутри блока кода под ней должно возникнуть заданное исключение
        # и это нормальное поведение.
        with pytest.raises(ZeroDivisionError):
            lib.calc(2,0,"/")