"""
Модуль бизнес-логики.
Содержит функции для CRUD операций (создание, чтение, обновление, удаление)
и подготовки данных для отчетов.
"""

import input_utils
import view
import sorter
import file_manager


def add_record(data):
    """
    Добавляет новую запись в базу.

    Args:
        data (list): Текущая база данных.
    """
    print("\n--- Добавление нового квартиросъёмщика ---")
    record = dict()
    record['surname'] = input_utils.get_string("Фамилия: ")
    record['name'] = input_utils.get_string("Имя: ")
    record['patronymic'] = input_utils.get_string("Отчество: ")
    record['street'] = input_utils.get_string("Улица: ")
    record['house'] = input_utils.get_string("Дом: ")
    record['apartment'] = input_utils.get_integer("Квартира: ")
    record['floor'] = input_utils.get_integer("Этаж: ")
    record['total_area'] = input_utils.get_float("Общая площадь: ")
    record['living_area'] = input_utils.get_float("Жилая площадь: ")
    record['registered_count'] = input_utils.get_integer("Кол-во прописанных: ")
    record['has_subsidy'] = input_utils.get_boolean("Есть льгота?")

    data.append(record)
    file_manager.save_database(data)
    print("Запись успешно добавлена!")


def delete_record(data):
    """
    Удаляет запись по номеру в списке.

    Args:
        data (list): Текущая база данных.
    """

    view.show_table(data)

    if not data:
        return

    try:
        string_index = input_utils.get_integer(
            "Введите номер строки для удаления (начиная с 1): "
        ) - 1

        if 0 <= string_index < len(data):

            removed = data.pop(string_index)
            file_manager.save_database(data)
            print(f"Запись '{removed['surname']}' удалена.")

        else:

            print("Ошибка: Неверный номер строки.")
            return delete_record(data)

    except Exception:
        print("Ошибка при удалении.")


def edit_record(data):
    """
    Редактирует запись по номеру.

    Args:
        data (list): Текущая база данных.
    """

    view.show_table(data)

    if not data:
        return

    string_index = input_utils.get_integer(
        "Введите номер строки для редактирования (начиная с 1): "
    ) - 1

    if 0 <= string_index < len(data):

        current_string = data[string_index]
        print("Оставьте поле пустым, если не хотите его менять.")

        edit = input(f"Фамилия [{current_string['surname']}]: ").strip()
        if edit: current_string['surname'] = edit

        edit = input(f"Имя [{current_string['name']}]: ").strip()
        if edit: current_string['name'] = edit

        edit = input(f"Отчество [{current_string['patronymic']}]: ").strip()
        if edit: current_string['patronymic'] = edit

        edit = input(f"Улица [{current_string['street']}]: ").strip()
        if edit: current_string['street'] = edit

        edit = input(f"Дом [{current_string['house']}]: ").strip()
        if edit: current_string['house'] = edit

        # Для чисел и булевых значений используем полную перезапись,
        # если пользователь решил менять
        change_num = input_utils.get_boolean(
            "Изменить числовые данные (площадь, этаж и т.д.)?"
        )

        if change_num:
            current_string['apartment'] =\
                input_utils.get_integer(
                    f"Квартира [{current_string['apartment']}]: "
                )
            current_string['floor'] =\
                input_utils.get_integer(
                    f"Этаж [{current_string['floor']}]: "
                )
            current_string['total_area'] =\
                input_utils.get_float(
                    f"Общая площадь [{current_string['total_area']}]: ")
            current_string['living_area'] =\
                input_utils.get_float(
                    f"Жилая площадь [{current_string['living_area']}]: ")
            current_string['registered_count'] =\
                input_utils.get_integer(
                f"Кол-во прописанных [{current_string['registered_count']}]: "
                )
            current_string['has_subsidy'] =\
                input_utils.get_boolean(
                f"Льгота [{str(current_string['has_subsidy'])
                .replace('True', 'да').replace('False', 'нет')}]: ")

        file_manager.save_database(data)
        print("Запись обновлена.")
    else:
        print("Неверный индекс.")
        return edit_record(data)


def report_1_all_sorted(data):
    """
    Отчет 1: Полный список.
    Сортировка: кол-во прописанных (убыв) + адрес (возр).
    """
    print("\n--- Отчет 1:"
          " Полный список "
          "(сорт: Люди(убыв) +"
          " Адрес(возр)) ---")
    sorted_data = sorter.shell_sort(data, mode=1)
    view.show_table(sorted_data)


def report_2_subsidy_sorted(data):
    """
    Отчет 2: Только льготники.
    Сортировка: этаж (возр) + кол-во прописанных (убыв) + общая площадь (возр).
    """
    print("\n--- Отчет 2:"
          " Льготники (сорт: Этаж(возр) +"
          " Люди(убыв) +"
          " Общ. Площадь(возр)) ---")

    # Фильтрация
    filtered = list()
    for database_string in data:
        if database_string['has_subsidy']:
            filtered.append(database_string)

    sorted_data = sorter.shell_sort(filtered, mode=2)
    view.show_table(sorted_data)


def report_3_area_range(data):
    """
    Отчет 3: Квартиры в диапазоне площадей.
    Сортировка: наличие льготы (возр) + общая площадь (убыв).
    """
    print("\n--- Отчет 3: Поиск по площади ---")
    min_square = input_utils.get_float("Введите минимальную площадь (N1): ")
    max_square = input_utils.get_float("Введите максимальную площадь (N2): ")

    if max_square < min_square:
        while max_square < min_square:

            print('Ошибка. Максимальная площадь'
                  ' не может быть меньше минимальной площади.')

            max_square = input_utils.get_float(
                "Введите максимальную площадь (N2): "
            )

    # Фильтрация
    filtered = list()
    for database_string in data:
        if min_square <= database_string['total_area'] <= max_square:
            filtered.append(database_string)

    print(f"\nКвартиры от {min_square} до {max_square}"
          f" кв.м (сорт: Льгота(возр) + Общ. Площадь(убыв)):")
    sorted_data = sorter.shell_sort(filtered, mode=3)
    view.show_table(sorted_data)
