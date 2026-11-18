print("Система управления пользователями")

while True:
    print("\nГлавное меню")
    print("1 — Проверить данные пользователя")
    print("2 — Показать статистику сеанса")
    print("3 — Показать три учебные попытки")
    print("0 — Выход")

    menu_choice = input("Выберите пункт: ").strip()

    if menu_choice == "1":
        print("Проверка пользователя будет выполнена здесь.")

    elif menu_choice == "2":
        print("Статистика будет добавлена следующим этапом.")

    elif menu_choice == "3":
        for attempt_number in range(1, 4):
            print(f"Попытка №{attempt_number}")

    elif menu_choice == "0":
        print("Работа программы завершена.")
        break

    else:
        print("Ошибка: выберите пункт 0, 1, 2 или 3.")