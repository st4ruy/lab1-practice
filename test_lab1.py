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
        """Перевіряє створення трикутника з правильними сторонами."""
        triangle = TriangleCalculator(5, 4, 2)
        self.assertIsNotNone(triangle)
        self.assertEqual(triangle.a, 5)
        self.assertEqual(triangle.b, 4)
        self.assertEqual(triangle.c, 2)

    def test_invalid_triangle(self):
        """Перевіряє викидання помилки для неіснуючого трикутника."""
        with self.assertRaises(ValueError):
            TriangleCalculator(1, 1, 5)

    def test_semiperimeter(self):
        """Перевіряє обчислення півпериметра."""
        triangle = TriangleCalculator(5, 4, 2)
        self.assertEqual(triangle.semiperimeter(), 5.5)

    def test_area(self):
        """Перевіряє обчислення площі за формулою Герона."""
        triangle = TriangleCalculator(5, 4, 2)
        self.assertAlmostEqual(triangle.area(), 3.7997, places=4)

    def test_equilateral_triangle(self):
        """Перевіряє обчислення площі рівностороннього трикутника."""
        triangle = TriangleCalculator(3, 3, 3)
        expected_area = (math.sqrt(3) / 4) * 9
        self.assertAlmostEqual(triangle.area(), expected_area, places=4)


class TestArithmeticExpression(unittest.TestCase):
    """
    Тести для класу ArithmeticExpression (обчислення складного виразу).
    """

    def test_valid_parameters(self):
        """Перевіряє створення об'єкта з правильними параметрами."""
        expr = ArithmeticExpression(0.5, 0.34, 1.65)
        self.assertIsNotNone(expr)
        self.assertEqual(expr.a, 0.5)
        self.assertEqual(expr.x, 0.34)
        self.assertEqual(expr.alpha, 1.65)

    def test_invalid_x(self):
        """Перевіряє викидання помилки при x > 1."""
        with self.assertRaises(ValueError):
            ArithmeticExpression(0.5, 1.5, 1.65)

    def test_invalid_x_negative(self):
        """Перевіряє викидання помилки при x < -1."""
        with self.assertRaises(ValueError):
            ArithmeticExpression(0.5, -1.5, 1.65)

    def test_numerator(self):
        """Перевіряє обчислення чисельника."""
        expr = ArithmeticExpression(0.5, 0.34, 1.65)
        self.assertAlmostEqual(expr.calculate_numerator(), -1.081924, places=6)

    def test_denominator(self):
        """Перевіряє обчислення знаменника."""
        expr = ArithmeticExpression(0.5, 0.34, 1.65)
        self.assertAlmostEqual(expr.calculate_denominator(), 2.296870, places=6)

    def test_result(self):
        """Перевіряє обчислення кінцевого результату Y."""
        expr = ArithmeticExpression(0.5, 0.34, 1.65)
        self.assertAlmostEqual(expr.calculate_result(), -0.4710428805, places=10)

    def test_get_details(self):
        """Перевіряє наявність всіх ключів у словнику."""
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
    """Тести для граничних випадків."""

    def test_zero_denominator(self):
        """Перевіряє роботу з граничними значеннями."""
        expr = ArithmeticExpression(1.0, 0.0, 1.0)
        self.assertIsNotNone(expr)

    def test_negative_a(self):
        """Перевіряє роботу з від'ємним a."""
        expr = ArithmeticExpression(-0.5, 0.34, 1.65)
        result = expr.calculate_result()
        self.assertIsInstance(result, float)


# ===================================================================
# ЗАПУСК ТЕСТІВ
# ===================================================================

if __name__ == "__main__":
    # Запускаємо всі тести
    unittest.main()
    
