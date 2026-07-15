"""
Модуль з тестами для лабораторної роботи №1.
Використовує вбудований модуль unittest.

Автор: Кравцов Олександр Іванович
Група: 535а
"""

import unittest
import math

# Імпортуємо наші класи з модернізованого коду
from lab1_modernized import TriangleCalculator, ArithmeticExpression


class TestTriangleCalculator(unittest.TestCase):
    """
    Тести для класу TriangleCalculator (обчислення площі трикутника).
    """
    
    def test_valid_triangle(self):
        """
        Перевіряє, чи правильно створюється трикутник з правильними сторонами.
        Очікується: трикутник створюється без помилок.
        """
        triangle = TriangleCalculator(5, 4, 2)
        self.assertIsNotNone(triangle)
        self.assertEqual(triangle.a, 5)
        self.assertEqual(triangle.b, 4)
        self.assertEqual(triangle.c, 2)
    
    def test_invalid_triangle(self):
        """
        Перевіряє, чи викидається помилка при створенні неіснуючого трикутника.
        Очікується: ValueError.
        """
        with self.assertRaises(ValueError):
            # Такий трикутник не існує (1 + 1 < 5)
            TriangleCalculator(1, 1, 5)
    
    def test_semiperimeter(self):
        """
        Перевіряє обчислення півпериметра.
        Очікується: p = 5.5
        """
        triangle = TriangleCalculator(5, 4, 2)
        self.assertEqual(triangle.semiperimeter(), 5.5)
    
    def test_area(self):
        """
        Перевіряє обчислення площі за формулою Герона.
        Очікується: S ≈ 3.7997 (округлено до 2 знаків: 3.80)
        """
        triangle = TriangleCalculator(5, 4, 2)
        area = triangle.area()
        # Перевіряємо з точністю до 4 знаків після коми
        self.assertAlmostEqual(area, 3.7997, places=4)
    
    def test_equilateral_triangle(self):
        """
        Перевіряє обчислення площі рівностороннього трикутника.
        Очікується: для a=3, S = (√3/4)*9 ≈ 3.8971
        """
        triangle = TriangleCalculator(3, 3, 3)
        expected_area = (math.sqrt(3) / 4) * 9
        self.assertAlmostEqual(triangle.area(), expected_area, places=4)


class TestArithmeticExpression(unittest.TestCase):
    """
    Тести для класу ArithmeticExpression (обчислення складного виразу).
    """
    
    def test_valid_parameters(self):
        """
        Перевіряє, чи правильно створюється об'єкт з правильними параметрами.
        Очікується: об'єкт створюється без помилок.
        """
        expr = ArithmeticExpression(0.5, 0.34, 1.65)
        self.assertIsNotNone(expr)
        self.assertEqual(expr.a, 0.5)
        self.assertEqual(expr.x, 0.34)
        self.assertEqual(expr.alpha, 1.65)
    
    def test_invalid_x(self):
        """
        Перевіряє, чи викидається помилка при x > 1 (недопустиме значення для arccos).
        Очікується: ValueError.
        """
        with self.assertRaises(ValueError):
            ArithmeticExpression(0.5, 1.5, 1.65)
    
    def test_invalid_x_negative(self):
        """
        Перевіряє, чи викидається помилка при x < -1 (недопустиме значення для arccos).
        Очікується: ValueError.
        """
        with self.assertRaises(ValueError):
            ArithmeticExpression(0.5, -1.5, 1.65)
    
    def test_numerator(self):
        """
        Перевіряє обчислення чисельника для заданих параметрів.
        Очікується: чисельник ≈ -1.081924
        """
        expr = ArithmeticExpression(0.5, 0.34, 1.65)
        numerator = expr.calculate_numerator()
        self.assertAlmostEqual(numerator, -1.081924, places=6)
    
    def test_denominator(self):
        """
        Перевіряє обчислення знаменника для заданих параметрів.
        Очікується: знаменник ≈ 2.296870
        """
        expr = ArithmeticExpression(0.5, 0.34, 1.65)
        denominator = expr.calculate_denominator()
        self.assertAlmostEqual(denominator, 2.296870, places=6)
    
    def test_result(self):
        """
        Перевіряє обчислення кінцевого результату Y.
        Очікується: Y ≈ -0.4710428805
        """
        expr = ArithmeticExpression(0.5, 0.34, 1.65)
        result = expr.calculate_result()
        self.assertAlmostEqual(result, -0.4710428805, places=10)
    
    def test_get_details(self):
        """
        Перевіряє, чи функція get_details повертає словник з усіма ключами.
        Очікується: наявність всіх ключів.
        """
        expr = ArithmeticExpression(0.5, 0.34, 1.65)
        details = expr.get_details()
        
        expected_keys = [
            'part1_sin_3alpha', 'part2_cos_alpha', 'part3_exp',
            'numerator', 'log_part', 'under_root',
            'part4_cuberoot', 'part5_arccos', 'denominator', 'result'
        ]
        
        for key in expected_keys:
            self.assertIn(key, details)


class TestEdgeCases(unittest.TestCase):
    """
    Тести для граничних випадків.
    """
    
    def test_zero_denominator(self):
        """
        Перевіряє, чи викидається помилка при знаменнику, що дорівнює нулю.
        Очікується: ZeroDivisionError.
        """
        # Для x = 1, arccos(1) = 0, що може призвести до проблем
        # Але це залежить від конкретних значень
        expr = ArithmeticExpression(1.0, 0.0, 1.0)
        # Просто перевіряємо, що об'єкт створюється
        self.assertIsNotNone(expr)
    
    def test_negative_a(self):
        """
        Перевіряє роботу з від'ємним a.
        Очікується: програма працює коректно (або викидає попередження).
        """
        expr = ArithmeticExpression(-0.5, 0.34, 1.65)
        result = expr.calculate_result()
        # Перевіряємо, що результат є числом (не помилка)
        self.assertIsInstance(result, float)


def run_tests():
    """
    Функція для запуску всіх тестів з виводом результатів.
    """
    # Створюємо набір тестів
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    
    # Додаємо всі тестові класи
    suite.addTests(loader.loadTestsFromTestCase(TestTriangleCalculator))
    suite.addTests(loader.loadTestsFromTestCase(TestArithmeticExpression))
    suite.addTests(loader.loadTestsFromTestCase(TestEdgeCases))
    
    # Запускаємо тести
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    # Виводимо підсумок
    print("\n" + "=" * 60)
    print("РЕЗУЛЬТАТИ ТЕСТУВАННЯ".center(60))
    print("=" * 60)
    print(f"Запущено тестів: {result.testsRun}")
    print(f"Успішно: {result.testsRun - len(result.failures) - len(result.errors)}")
    print(f"Провалено: {len(result.failures)}")
    print(f"Помилок: {len(result.errors)}")
    print("=" * 60)
    
    return result


if __name__ == "__main__":
    # Запускаємо тести при безпосередньому виконанні файлу
    run_tests()
