"""
ЛАБОРАТОРНА РОБОТА №1 (МОДЕРНІЗОВАНА ВЕРСІЯ)
Варіант 6
Студент: Кравцов Олександр Іванович
Група: 535а

Тема: Обчислення площі трикутника за формулою Герона
      та складного арифметичного виразу.

Модернізація виконана за допомогою AI-агента (DeepSeek)
у середовищі PyCharm.
"""

# Імпортуємо модуль math для використання математичних функцій
import math
import logging
from typing import Dict, Optional

# ===================================================================
# НАЛАШТУВАННЯ СИСТЕМИ ЛОГУВАННЯ
# ===================================================================

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename='lab1.log',
    filemode='w',
    encoding='utf-8'
)


# ===================================================================
# КЛАС ДЛЯ ОБЧИСЛЕННЯ ПЛОЩІ ТРИКУТНИКА
# ===================================================================

class TriangleCalculator:
    """
    Клас для обчислення площі трикутника за формулою Герона.

    Атрибути:
        a (float): довжина сторони a
        b (float): довжина сторони b
        c (float): довжина сторони c
    """

    def __init__(self, a: float, b: float, c: float) -> None:
        """
        Ініціалізація трикутника з заданими сторонами.

        Аргументи:
            a (float): довжина сторони a
            b (float): довжина сторони b
            c (float): довжина сторони c

        Raises:
            ValueError: якщо трикутник з такими сторонами не існує
        """
        # Зберігаємо значення сторін
        self.a = a
        self.b = b
        self.c = c

        # Перевіряємо, чи існує трикутник
        if not self._is_valid_triangle():
            raise ValueError(
                f"Трикутник зі сторонами {a}, {b}, {c} не існує. "
                "Сума двох сторін має бути більшою за третю."
            )

        # Логуємо створення об'єкта
        logging.info(f"Створено трикутник зі сторонами: a={a}, b={b}, c={c}")

    def _is_valid_triangle(self) -> bool:
        """
        Перевіряє, чи існує трикутник з заданими сторонами.

        Повертає:
            bool: True якщо трикутник існує, False якщо ні
        """
        # Умова існування трикутника:
        # сума будь-яких двох сторін має бути більшою за третю
        return (
                self.a + self.b > self.c and
                self.a + self.c > self.b and
                self.b + self.c > self.a
        )

    def semiperimeter(self) -> float:
        """
        Обчислює півпериметр трикутника.

        Повертає:
            float: півпериметр
        """
        # Півпериметр = (a + b + c) / 2
        return (self.a + self.b + self.c) / 2

    def area(self) -> float:
        """
        Обчислює площу трикутника за формулою Герона.

        Формула: S = √(p·(p-a)·(p-b)·(p-c))
        де p - півпериметр

        Повертає:
            float: площа трикутника
        """
        # Обчислюємо півпериметр
        p = self.semiperimeter()

        # Обчислюємо площу за формулою Герона
        area = math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))

        logging.info(f"Площа трикутника обчислена: {area:.2f}")
        return area

    def __str__(self) -> str:
        """Повертає рядкове представлення трикутника"""
        return f"Трикутник(a={self.a}, b={self.b}, c={self.c})"


# ===================================================================
# КЛАС ДЛЯ ОБЧИСЛЕННЯ СКЛАДНОГО АРИФМЕТИЧНОГО ВИРАЗУ
# ===================================================================

class ArithmeticExpression:
    """
    Клас для обчислення складного арифметичного виразу.

    Вираз: Y = [sin(3α) + (x²+1)·cos²α·x - 0.8·10^(-2a)·e^x] /
               [∛(x+1-lg(α²x)+0.3(x³-a)) + arccos(x)]

    Атрибути:
        a (float): параметр a
        x (float): параметр x
        alpha (float): параметр α (кут у радіанах)
    """

    def __init__(self, a: float, x: float, alpha: float) -> None:
        """
        Ініціалізація виразу з заданими параметрами.

        Аргументи:
            a (float): параметр a
            x (float): параметр x (має бути в діапазоні [-1, 1])
            alpha (float): параметр α (кут у радіанах)

        Raises:
            ValueError: якщо параметри не відповідають допустимим значенням
        """
        # Перевіряємо допустимість значень
        if not (-1 <= x <= 1):
            raise ValueError(f"x={x} має бути в діапазоні [-1, 1] для arccos(x)")

        # Зберігаємо параметри
        self.a = a
        self.x = x
        self.alpha = alpha

        logging.info(f"Створено вираз з параметрами: a={a}, x={x}, alpha={alpha}")

    def calculate_numerator(self) -> float:
        """
        Обчислює чисельник виразу.

        Формула: sin(3α) + (x²+1)·cos²α·x - 0.8·10^(-2a)·e^x

        Повертає:
            float: значення чисельника
        """
        # Частина 1: sin(3α)
        part1 = math.sin(3 * self.alpha)

        # Частина 2: (x² + 1) · cos²α · x
        part2 = (self.x ** 2 + 1) * (math.cos(self.alpha) ** 2) * self.x

        # Частина 3: 0.8 · 10^(-2a) · e^x
        part3 = 0.8 * (10 ** (-2 * self.a)) * math.exp(self.x)

        # Чисельник = частина1 + частина2 - частина3
        numerator = part1 + part2 - part3

        logging.debug(f"Чисельник обчислено: {numerator:.6f}")
        return numerator

    def calculate_denominator(self) -> float:
        """
        Обчислює знаменник виразу.

        Формула: ∛(x+1-lg(α²x)+0.3(x³-a)) + arccos(x)

        Повертає:
            float: значення знаменника
        """
        # Частина під коренем: x + 1 - lg(α²x) + 0.3(x³ - a)
        # Обчислюємо десятковий логарифм: lg(α²x)
        log_part = math.log10(self.alpha ** 2 * self.x)

        # Вираз під кубічним коренем
        under_root = (
                self.x + 1
                - log_part
                + 0.3 * (self.x ** 3 - self.a)
        )

        # Кубічний корінь
        part4 = under_root ** (1 / 3)

        # Арккосинус: arccos(x)
        part5 = math.acos(self.x)

        # Знаменник = part4 + part5
        denominator = part4 + part5

        logging.debug(f"Знаменник обчислено: {denominator:.6f}")
        return denominator

    def calculate_result(self) -> float:
        """
        Обчислює кінцевий результат Y = чисельник / знаменник.

        Повертає:
            float: значення виразу Y

        Raises:
            ZeroDivisionError: якщо знаменник дорівнює 0
        """
        # Отримуємо чисельник і знаменник
        numerator = self.calculate_numerator()
        denominator = self.calculate_denominator()

        # Перевірка ділення на нуль
        if abs(denominator) < 1e-10:
            raise ZeroDivisionError("Знаменник дорівнює нулю!")

        # Обчислюємо результат
        result = numerator / denominator

        logging.info(f"Результат обчислено: {result:.10f}")
        return result

    def get_details(self) -> Dict[str, float]:
        """
        Повертає всі проміжні обчислення для звіту.

        Повертає:
            Dict[str, float]: словник з усіма проміжними значеннями
        """
        # Обчислюємо всі частини окремо
        part1 = math.sin(3 * self.alpha)
        part2 = (self.x ** 2 + 1) * (math.cos(self.alpha) ** 2) * self.x
        part3 = 0.8 * (10 ** (-2 * self.a)) * math.exp(self.x)
        numerator = part1 + part2 - part3

        log_part = math.log10(self.alpha ** 2 * self.x)
        under_root = self.x + 1 - log_part + 0.3 * (self.x ** 3 - self.a)
        part4 = under_root ** (1 / 3)
        part5 = math.acos(self.x)
        denominator = part4 + part5

        # Повертаємо всі значення у словнику
        return {
            'part1_sin_3alpha': part1,
            'part2_cos_alpha': part2,
            'part3_exp': part3,
            'numerator': numerator,
            'log_part': log_part,
            'under_root': under_root,
            'part4_cuberoot': part4,
            'part5_arccos': part5,
            'denominator': denominator,
            'result': numerator / denominator if denominator != 0 else float('inf')
        }


# ===================================================================
# ДОПОМІЖНІ ФУНКЦІЇ
# ===================================================================

def display_header(title: str, char: str = '=', length: int = 60) -> None:
    """
    Виводить заголовок у консоль з обрамленням.

    Аргументи:
        title (str): текст заголовка
        char (str): символ для обрамлення
        length (int): загальна довжина рядка
    """
    print("\n" + char * length)
    print(title.center(length))
    print(char * length)


# ===================================================================
# ГОЛОВНА ФУНКЦІЯ ПРОГРАМИ
# ===================================================================

def main() -> None:
    """
    Головна функція програми.

    Демонструє роботу всіх класів та функцій.
    """
    try:
        # ===================================================================
        # ЗАВДАННЯ 1: Обчислення площі трикутника
        # ===================================================================
        display_header("ЗАВДАННЯ 1: ПЛОЩА ТРИКУТНИКА")

        # Створюємо трикутник зі сторонами (варіант 6)
        triangle = TriangleCalculator(a=5, b=4, c=2)

        # Виводимо інформацію про трикутник
        print(f"\n{triangle}")
        print(f"Півпериметр p = {triangle.semiperimeter():.2f}")
        print(f"Площа трикутника S = {triangle.area():.2f}")

        # ===================================================================
        # ЗАВДАННЯ 2: Обчислення складного виразу
        # ===================================================================
        display_header("ЗАВДАННЯ 2: СКЛАДНИЙ ВИРАЗ")

        # Створюємо вираз з параметрами (варіант 6)
        expr = ArithmeticExpression(a=0.5, x=0.34, alpha=1.65)

        # Отримуємо всі обчислення
        details = expr.get_details()

        # Виводимо результати у відформатованому вигляді
        print("\nВихідні значення:")
        print(f"  a = {0.5}")
        print(f"  x = {0.34}")
        print(f"  α = {1.65}")

        print("\nЧИСЕЛЬНИК:")
        print(f"  sin(3α) = {details['part1_sin_3alpha']:.6f}")
        print(f"  (x²+1)·cos²α·x = {details['part2_cos_alpha']:.6f}")
        print(f"  0.8·10^(-2a)·e^x = {details['part3_exp']:.6f}")
        print(f"  Сума: {details['numerator']:.6f}")

        print("\nЗНАМЕННИК:")
        print(f"  lg(α²x) = {details['log_part']:.6f}")
        print(f"  Вираз під коренем: {details['under_root']:.6f}")
        print(f"  ∛(...) = {details['part4_cuberoot']:.6f}")
        print(f"  arccos(x) = {details['part5_arccos']:.6f}")
        print(f"  Сума: {details['denominator']:.6f}")

        print("\nРЕЗУЛЬТАТ:")
        print(f"  Y = {details['result']:.10f}")

        logging.info("Програму виконано успішно")

    except ValueError as e:
        logging.error(f"Помилка валідації: {e}")
        print(f"\nПОМИЛКА: {e}")
    except ZeroDivisionError as e:
        logging.error(f"Математична помилка: {e}")
        print(f"\nПОМИЛКА: {e}")
    except Exception as e:
        logging.critical(f"Непередбачена помилка: {e}")
        print(f"\nКРИТИЧНА ПОМИЛКА: {e}")


# Перевірка, чи запускається файл як основна програма
if __name__ == "__main__":
    main()