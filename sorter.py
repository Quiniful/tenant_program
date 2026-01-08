"""
Модуль сортировки.
Реализует алгоритм сортировки Шелла и логику сравнения
для различных типов отчетов.
"""


def compare_address(first_database_string, second_database_string):
    """
    Сравнивает адреса (Улица -> Дом -> Квартира) по возрастанию.

    Args:
        first_database_string (dict): Первая запись.
        second_database_string (dict): Вторая запись.

    Returns:
        int: 1 если first_database_string > second_database_string,
         -1 если first_database_string <  second_database_string, 0 если равны.
    """
    # Сравнение улиц
    if (first_database_string['street'] >
            second_database_string['street']): return 1
    if (first_database_string['street'] <
            second_database_string['street']): return -1

    # Сравнение домов (строковое, т.к. могут быть 12а)
    if (first_database_string['house'] >
            second_database_string['house']): return 1
    if (first_database_string['house'] <
            second_database_string['house']): return -1

    # Сравнение квартир (числовое)
    if (first_database_string['apartment'] >
            second_database_string['apartment']): return 1
    if (first_database_string['apartment'] <
            second_database_string['apartment']): return -1

    return 0


def should_swap(first_database_string, second_database_string, mode):
    """
    Определяет, нужно ли менять местами две записи
     в зависимости от режима сортировки.

    Args:
        first_database_string (dict): Левый элемент сравнения.
        second_database_string (dict): Правый элемент сравнения.
        mode (int): Номер типа сортировки (1, 2 или 3).

    Returns:
        bool: True,
         если элементы стоят в неправильном порядке и их нужно поменять.
    """

    # Отчет 1: Кол-во прописанных (убыв) + Адрес (возр)
    if mode == 1:
        # Первичный ключ: Кол-во людей (по убыванию)
        if (first_database_string['registered_count'] <
                second_database_string['registered_count']):
            return True
        elif (first_database_string['registered_count'] >
              second_database_string['registered_count']):
            return False
        else:
            # Вторичный ключ: Адрес (по возрастанию)
            if compare_address(first_database_string,
                               second_database_string) > 0:
                return True
            return False

    # Отчет 2: Этаж (возр) + Кол-во прописанных (убыв) + Общая площадь (возр)
    elif mode == 2:
        # Первичный: Этаж (возр)
        if (first_database_string['floor'] >
                second_database_string['floor']):
            return True
        elif (first_database_string['floor'] <
              second_database_string['floor']):
            return False

        # Вторичный: Кол-во людей (убыв)
        if (first_database_string['registered_count'] <
                second_database_string['registered_count']):
            return True
        elif (first_database_string['registered_count'] >
              second_database_string['registered_count']):
            return False

        # Третичный: Общ площадь (возр)
        if (first_database_string['total_area'] >
                second_database_string['total_area']):
            return True
        return False

    # Отчет 3: Наличие льготы (возр) + Общая площадь (убыв)
    # False < True (0 < 1). Возрастание льготы: Сначала Нет, потом Да.
    elif mode == 3:
        # Первичный: Льгота (возр)
        first_value = 1 if first_database_string['has_subsidy'] else 0
        second_value = 1 if second_database_string['has_subsidy'] else 0

        if first_value > second_value:
            return True
        elif first_value < second_value:
            return False

        # Вторичный: Общая площадь (убыв)
        if (first_database_string['total_area'] <
                second_database_string['total_area']):
            return True
        return False

    return False


def shell_sort(data, mode):
    """
    Сортирует список словарей методом Шелла.

    Args:
        data (list): Список записей для сортировки.
        mode (int): Режим сортировки (критерии сравнения).

    Returns:
        list: Отсортированный список.
    """
    len_of_data = len(data)
    gap = len_of_data // 2 # 1. Начальный разрыв - половина длины списка

    # Копируем список, чтобы не менять оригинал
    array = data[:]

    # Пока разрыв не исчезнет
    while gap > 0:

        # Проходим по элементам от gap до конца списка
        for first_element in range(gap, len_of_data):
            temp = array[first_element] # Запоминаем текущий элемент
            second_element = first_element

            # Внутренний цикл: "Прыгаем" назад на величину gap
            # Мы проверяем: элемент слева
            # (на расстоянии gap) "больше" нашего temp
            # Функция should_swap решает,
            # кто "больше" в зависимости от ТЗ (площадь, этаж и т.д.)

            while (second_element >= gap and
                   should_swap(array[second_element - gap], temp, mode)):

                # Если элемент слева стоит неправильно, сдвигаем его вправо
                array[second_element] = array[second_element - gap]
                second_element -= gap

            # Когда нашли правильное место
            # или дошли до начала — ставим наш элемент
            array[second_element] = temp
            
        # Уменьшаем разрыв в 2 раза
        gap //= 2

    return array
