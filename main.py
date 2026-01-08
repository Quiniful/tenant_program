"""
Главный модуль программы.
Содержит точку входа и управление циклическим меню.
"""

import file_manager
import actions


def show_menu():
    """Выводит пункты меню."""
    print("\n" + "=" * 30)
    print(" МЕНЮ ПРОГРАММЫ 'КВАРТИРОСЪЁМЩИК'")
    print("=" * 30)
    print("1. Показать всех (Отчет 1: Сортировка по людям и адресу)")
    print("2. Льготники (Отчет 2: Сортировка по этажу, людям, общ. площади)")
    print("3. Поиск по площади (Отчет 3: Сортировка по льготе и общ. площади)")
    print("4. Добавить запись")
    print("5. Изменить запись")
    print("6. Удалить запись")
    print("0. Выход")
    print("-" * 30)


def main():
    """Основная функция управления."""
    # Загрузка данных при старте
    database = file_manager.load_database()

    while True:
        show_menu()
        choice = input("Выберите пункт меню: ").strip()

        if choice == '1':
            actions.report_1_all_sorted(database)
        elif choice == '2':
            actions.report_2_subsidy_sorted(database)
        elif choice == '3':
            actions.report_3_area_range(database)
        elif choice == '4':
            actions.add_record(database)
        elif choice == '5':
            actions.edit_record(database)
        elif choice == '6':
            actions.delete_record(database)
        elif choice == '0':
            print("Завершение работы программы.")
            break
        else:
            print("Ошибка: Неверный пункт меню. Повторите ввод.")

        # Небольшая пауза для удобства чтения
        input("\nНажмите Enter, чтобы продолжить...")


if __name__ == "__main__":
    main()