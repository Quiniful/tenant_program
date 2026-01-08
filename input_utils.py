"""
Модуль для безопасного ввода данных.
Содержит функции для проверки типов вводимых значений.
"""


def get_integer(prompt):
    """
    Запрашивает у пользователя целое число.

    Args:
        prompt (str): Текст приглашения для ввода.

    Returns:
        int: Введенное целое число.
    """
    while True:
        try:
            value = int(input(prompt))

            if 'Квартира' in prompt or 'Кол-во прописанных' in prompt:
                if value <= 0:
                    raise ValueError

            if 'Дом' in prompt:
                if value < 0:
                    raise ValueError

            return value

        except ValueError:
            print("Ошибка: Введите другое целое число.")


def get_float(prompt):
    """
    Запрашивает у пользователя вещественное число.

    Args:
        prompt (str): Текст приглашения для ввода.

    Returns:
        float: Введенное вещественное число.
    """
    while True:
        try:
            value = float(input(prompt))

            if 'Общая площадь' in prompt or 'Жилая площадь' in prompt:
                if value <= 0:
                    raise ValueError

            return value
        except ValueError:
            print("Ошибка: Введите число (можно с точкой).")


def get_boolean(prompt):
    """
    Запрашивает у пользователя булево значение (Да/Нет).

    Args:
        prompt (str): Текст приглашения для ввода.

    Returns:
        bool: True, если ввод 'да'/'y', иначе False.
    """
    value = input(prompt + " (да/нет): ").lower().strip()
    if value == 'да' or value == 'y' or value == 'yes':
        return True
    return False


def get_string(prompt):
    """
    Запрашивает непустую строку.

    Args:
        prompt (str): Текст приглашения для ввода.

    Returns:
        str: Введенная строка.
    """
    while True:
        value = input(prompt).strip()

        if len(value) > 0:
            return value
        print("Ошибка. Введите другую строку.")
