# Лабораторная работа 1
# Вариант 6
# Студент: [Кравцов Олександр Іванович]
# Группа: [535а]

import math

print("\n === ЗАДАНИЕ 1 ===")
print("Вычисление площади треугольника по формуле Герона")

a = 5
b = 4
c = 2

print(f"Стороны треугольника: a = {a}, b = {b}, c = {c}")

# Вычисляем полупериметр
p = (a + b + c) / 2
print(f"Полупериметр p = {p}")

# Вычисляем площадь по формуле Герона
S = math.sqrt(p * (p - a) * (p - b) * (p - c))
print(f"Площадь треугольника S = {S:.2f}\n\n\n")  # :.2f - округляем до 2 знаков после запятой


print("=== ЗАДАНИЕ 2 ===")
print("Вычисление сложного арифметического выражения")

# Исходные данные
a = 0.5
x = 0.34
alpha = 1.65

print(f"Исходные значения: a = {a}, x = {x}, α = {alpha}")

# Часть 1: sin(3α)
part1 = math.sin(3 * alpha)

# Часть 2: (x² + 1) * cos²α * x
part2 = (x**2 + 1) * (math.cos(alpha)**2) * x

# Часть 3: 0.8 * 10^(-2a) * e^x
part3 = 0.8 * (10**(-2 * a)) * math.exp(x)

# Весь числитель
numerator = part1 + part2 - part3
print(f"\nЧИСЛИТЕЛЬ:")
print(f"sin(3α) = {part1:.6f}")
print(f"(x² + 1)*cos²α*x = {part2:.6f}")
print(f"0.8*10^(-2a)*e^x = {part3:.6f}")
print(f"Сумма: {numerator:.6f}")


# Часть 4: ∛(x + 1 - lg(α²x) + 0.3(x³ - a))
# lg(α²x) - это логарифм по основанию 10
lg_part = math.log10(alpha**2 * x)  # lg(α²x)

# Выражение под корнем: x + 1 - lg(α²x) + 0.3(x³ - a)
under_root = x + 1 - lg_part + 0.3 * (x**3 - a)

# Кубический корень ∛
part4 = under_root ** (1/3)  # ∛(выражение)

# Часть 5: arccos(x)
part5 = math.acos(x)

# Весь знаменатель
denominator = part4 + part5
print(f"\nЗНАМЕНАТЕЛЬ:")
print(f"lg(α²x) = {lg_part:.6f}")
print(f"Выражение под корнем: {under_root:.6f}")
print(f"∛(...) = {part4:.6f}")
print(f"arccos(x) = {part5:.6f}")
print(f"Сумма: {denominator:.6f}")

# РЕЗУЛЬТАТ
Y = numerator / denominator
print(f"\nРЕЗУЛЬТАТ:")
print(f"Y = {Y:.10f}")

# инфа для проверка
print(f"\nПроверочные значения:")
print(f"sin(3α) = sin({3*alpha:.2f}) = {part1:.6f}")
print(f"cos(α) = cos({alpha:.2f}) = {math.cos(alpha):.6f}")
print(f"e^x = e^{x} = {math.exp(x):.6f}")
print(f"10^(-2a) = 10^{-2*a} = {10**(-2*a):.6f}")
