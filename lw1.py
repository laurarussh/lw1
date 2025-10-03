def calculate_control_digit(iin_without_control):
    if len(iin_without_control) != 11 or not iin_without_control.isdigit():
        raise ValueError("ИИН должен содержать ровно 11 цифр")

    digits = [int(d) for d in iin_without_control]

    weights1 = list(range(1, 12))
    s1 = sum(d * w for d, w in zip(digits, weights1))
    k1 = s1 % 11

    if k1 < 10:
        return k1

    weights2 = [3, 4, 5, 6, 7, 8, 9, 10, 11, 1, 2]
    s2 = sum(d * w for d, w in zip(digits, weights2))
    k2 = s2 % 11

    return k2 if k2 < 10 else 0

iin_base = "85080831073"
control_digit = calculate_control_digit(iin_base)
full_iin = iin_base + str(control_digit)
print("Контрольный разряд:", control_digit)
print("Полный ИИН:", full_iin)
