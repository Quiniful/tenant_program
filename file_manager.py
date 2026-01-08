"""
Модуль для работы с файловой системой.
Отвечает за чтение и запись базы данных в текстовый файл,
а также создание начальных данных.
"""

database_file = "tenants_db.txt"


def get_default_data():
    """
    Генерирует список из 25+ записей для начального заполнения БД.
    Обеспечивает разнообразие данных для проверки сортировки.

    Returns:
        list: Список словарей с данными жильцов.
    """
    data = list()
    # Формат:
    # Фамилия, Имя, Отчество, Улица, Дом, Кв, Этаж, Общ.пл,
    # Жил.пл, Кол-во чел, Льгота
    raw_data = [

        ("Пак",
         "Лев",
         "Иванович",
         "Ленина",
         "10",
         1,
         1,
         45.5,
         30.0,
         2,
         False),

        ("Петров",
         "Петр",
         "Петрович",
         "Ленина",
         "10",
         2,
         1,
         45.5,
         30.0,
         3,
         True),

        ("Сидоров",
         "Сидор",
         "Сидорович",
         "Ленина",
         "10",
         5,
         2,
         60.0,
         40.0,
         1,
         False),

        ("Алексеев",
         "Алексей",
         "Алексеевич",
         "Мира",
         "5",
         10,
         3,
         50.0,
         35.0,
         4,
         True),

        ("Борисова",
         "Анна",
         "Борисовна",
         "Мира",
         "5",
         12,
         3,
         52.0,
         36.0,
         2,
         False),

        ("Васильев",
         "Василий",
         "Васильевич",
         "Садовая",
         "1",
         101,
         10,
         100.0,
         70.0,
         5,
         False),

        ("Григорьев",
         "Григорий",
         "Григорьевич",
         "Садовая",
         "1",
         102,
         10,
         100.0,
         70.0,
         2,
         True),

        ("Дмитриев",
         "Дмитрий",
         "Дмитриевич",
         "Кирова",
         "20",
         5,
         2,
         33.0,
         18.0,
         1,
         True),

        ("Еленова",
         "Елена",
         "Еленовна",
         "Кирова",
         "20",
         6,
         2,
         33.0,
         18.0,
         1,
         False),

        ("Жуков",
         "Олег",
         "Павлович",
         "Ленина",
         "12",
         45,
         5,
         75.0,
         50.0,
         3,
         True),

        ("Зиновьев",
         "Павел",
         "Олегович",
         "Гагарина",
         "7",
         8,
         4,
         65.5,
         45.0,
         4,
         False),

        ("Ильин",
         "Илья",
         "Ильич",
         "Гагарина",
         "7",
         9,
         4,
         65.5,
         45.0,
         5,
         True),

        ("Козлов",
         "Константин",
         "Игоревич",
         "Победы",
         "2",
         15,
         5,
         80.0,
         55.0,
         2,
         False),

        ("Лавров",
         "Сергей",
         "Викторович",
         "Победы",
         "2",
         16,
         5,
         80.0,
         55.0,
         6,
         True),

        ("Миронова",
         "Мария",
         "Ивановна",
         "Ленина",
         "10",
         3,
         1,
         45.5,
         30.0,
         4,
         True),

        ("Никитин",
         "Никита",
         "Никитич",
         "Цветочная",
         "3",
         1,
         1,
         30.0,
         20.0,
         1,
         False),

        ("Орлов",
         "Олег",
         "Олегович",
         "Цветочная",
         "3",
         2,
         1,
         31.0,
         21.0,
         1,
         True),

        ("Павлов",
         "Павел",
         "Павлович",
         "Цветочная",
         "3",
         3,
         2,
         55.0,
         35.0,
         3,
         False),

        ("Романов",
         "Роман",
         "Романович",
         "Зеленая",
         "8",
         44,
         9,
         48.0,
         32.0,
         2,
         True),

        ("Соколова",
         "Светлана",
         "Сергеевна",
         "Зеленая",
         "8",
         45,
         9,
         48.0,
         32.0,
         2,
         False),

        ("Титов",
         "Тимур",
         "Тимофеевич",
         "Новая",
         "11",
         20,
         3,
         90.0,
         60.0,
         3,
         True),

        ("Уваров",
         "Устин",
         "Устинович",
         "Новая",
         "11",
         21,
         3,
         91.0,
         61.0,
         3,
         True),

        ("Федоров",
         "Федор",
         "Федорович",
         "Парковая",
         "15",
         55,
         6,
         42.0,
         28.0,
         2,
         False),

        ("Харитонов",
         "Харитон",
         "Харитонович",
         "Парковая",
         "15",
         56,
         6,
         42.0,
         28.0,
         1,
         False),

        ("Царев",
         "Иван",
         "Петрович",
         "Луговая",
         "9",
         19,
         2,
         120.0,
         80.0,
         7,
         True),

        ("Чернов",
         "Петр",
         "Иванович",
         "Луговая",
         "9",
         20,
         2,
         125.0,
         85.0,
         1,
         False)
    ]

    for item in raw_data:
        record = dict()
        record['surname'] = item[0]
        record['name'] = item[1]
        record['patronymic'] = item[2]
        record['street'] = item[3]
        record['house'] = item[4]
        record['apartment'] = item[5]
        record['floor'] = item[6]
        record['total_area'] = item[7]
        record['living_area'] = item[8]
        record['registered_count'] = item[9]
        record['has_subsidy'] = item[10]
        data.append(record)

    return data


def save_database(data):
    """
    Сохраняет список записей в файл.

    Args:
        data (list): Список словарей с данными.
    """
    try:
        file = open(database_file, 'w', encoding='utf-8')
        for record in data:
            # Преобразуем словарь в строку с разделителем |
            line = (
                f"{record['surname']}|"
                f"{record['name']}|"
                f"{record['patronymic']}|"
                f"{record['street']}|"
                f"{record['house']}|"
                f"{record['apartment']}|"
                f"{record['floor']}|"
                f"{record['total_area']}|"
                f"{record['living_area']}|"
                f"{record['registered_count']}|"
                f"{1 if record['has_subsidy'] else 0}\n"
            )
            file.write(line)
        file.close()
    except IOError:
        print("Ошибка при записи файла.")


def load_database():
    """
    Загружает данные из файла.
     Если файла нет, создает его с демо-данными.

    Returns:
        list: Список словарей с данными.
    """
    data = list()
    try:
        file = open(database_file, 'r', encoding='utf-8')
        lines = file.readlines()
        file.close()

        if len(lines) == 0:
            raise FileNotFoundError

        for line in lines:
            parts = line.strip().split('|')
            if len(parts) < 11:
                continue

            record = dict()
            record['surname'] = parts[0]
            record['name'] = parts[1]
            record['patronymic'] = parts[2]
            record['street'] = parts[3]
            record['house'] = parts[4]
            record['apartment'] = int(parts[5])
            record['floor'] = int(parts[6])
            record['total_area'] = float(parts[7])
            record['living_area'] = float(parts[8])
            record['registered_count'] = int(parts[9])
            record['has_subsidy'] = bool(int(parts[10]))

            data.append(record)

    except (IOError, FileNotFoundError):
        print("База данных не найдена или пуста."
              " Создание новой базы с демо-данными...")
        data = get_default_data()
        save_database(data)

    return data