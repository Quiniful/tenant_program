"""
Модуль отображения данных.
Отвечает за форматированный вывод таблиц в консоль.
"""

def print_header():
    """Печатает заголовок таблицы."""
    print("-" * 153)
    # Используем простой метод выравнивания
    print(
        f"| {'№':3} |"
        f" {'Фамилия':20} |"
        f" {'Имя':15} |"
        f" {'Отчество':20} |"
        f" {'Улица':20} |"
        f" {'Дом':5} |"
        f" {'Кв':4} |"
        f" {'Эт':2} |"
        f" {'Общ.пл':8} |"
        f" {'Жил.пл':8} |"
        f" {'Людей':5} |"
        f" {'Льгота':6} |"
    )
    print("-" * 153)

def print_record(index, database_string):
    """
    Печатает одну строку таблицы.

    Args:
        index (int): Порядковый номер записи.
        database_string (dict): Словарь записи квартиросъемщика.
    """
    subsidy = "Да" if database_string['has_subsidy'] else "Нет"
    print(
        f"| {index:3} |"
        f" {database_string['surname']:20} |"
        f" {database_string['name']:15} |"
        f" {database_string['patronymic']:20} |"
        f" {database_string['street']:20} |"
        f" {database_string['house']:5} |"
        f" {database_string['apartment']:4} |"
        f" {database_string['floor']:2} |"
        f" {database_string['total_area']:8.1f} |"
        f" {database_string['living_area']:8.1f} |"
        f" {database_string['registered_count']:5} |"
        f" {subsidy:6} |"
    )

def show_table(data):
    """
    Выводит полный список данных в виде таблицы с нумерацией строк.

    Args:
        data (list): Список записей.
    """
    if not data:
        print("Список пуст.")
        return

    print_header()
    # Используем enumerate, чтобы получить автоматический счетчик (i),
    # начиная с 1
    for string_number, database_string in enumerate(data, 1):
        print_record(string_number, database_string)
    print("-" * 153)