print("Система управления пользователями")

# Счётчики и накопитель текущего сеанса
successful_checks = 0
error_checks = 0
total_age = 0

while True:
    print("\nГлавное меню")
    print("1 — Проверить данные пользователя")
    print("2 — Показать статистику сеанса")
    print("3 — Показать три учебные попытки")
    print("0 — Выход")

    menu_choice = input("Выберите пункт: ").strip()

    if menu_choice == "1":
        full_name = input("Введите ФИО: ").strip()
        login = input("Введите логин: ").strip()
        role = input(
            "Введите роль (Администратор/Пользователь): "
        ).strip()
        birth_year_text = input("Введите год рождения: ").strip()
        current_year_text = input("Введите текущий год: ").strip()

        if not full_name or not login or not role:
            print("Ошибка: ФИО, логин и роль обязательны.")
            error_checks += 1

        elif not birth_year_text.isdigit() or not current_year_text.isdigit():
            print("Ошибка: годы должны быть целыми числами.")
            error_checks += 1

        else:
            birth_year = int(birth_year_text)
            current_year = int(current_year_text)

            if role != "Администратор" and role != "Пользователь":
                print("Ошибка: допустимы роли Администратор или Пользователь.")
                error_checks += 1

            elif birth_year < 1900 or birth_year > current_year:
                print("Ошибка: проверьте корректность года рождения.")
                error_checks += 1

            else:
                user_age = current_year - birth_year

                successful_checks += 1
                total_age += user_age

                print("\nКарточка пользователя")
                print(f"ФИО: {full_name}")
                print(f"Логин: {login}")
                print(f"Роль: {role}")
                print(f"Возраст: {user_age}")

    elif menu_choice == "2":
        total_checks = successful_checks + error_checks

        print("\nСтатистика сеанса")
        print(f"Всего проверок: {total_checks}")
        print(f"Успешных: {successful_checks}")
        print(f"С ошибкой: {error_checks}")

        if successful_checks > 0:
            average_age = total_age / successful_checks
            print(f"Средний возраст успешных карточек: {average_age:.1f}")
        else:
            print("Средний возраст пока не вычисляется: нет успешных карточек.")

    elif menu_choice == "3":
        print("\nТри учебные попытки")

        for attempt_number in range(1, 4):
            print(f"Попытка №{attempt_number}")

    elif menu_choice == "0":
        print("Работа программы завершена.")
        break

    else:
        print("Ошибка: выберите пункт 0, 1, 2 или 3.")