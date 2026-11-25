
APP_TITLE = "Система управления пользователями — списки"

# Список для хранения всех пользователей
# Каждая запись имеет вид: [login, role, age]
users = []

while True:
    print(f"\n{APP_TITLE}")
    print("1 — Добавить пользователя")
    print("2 — Показать всех пользователей")
    print("3 — Найти пользователя по логину")
    print("4 — Показать пользователей по роли")
    print("5 — Показать пользователя с максимальным возрастом")
    print("0 — Выход")

    menu_choice = input("Выберите пункт: ").strip()

    # 1. Добавление пользователя
    if menu_choice == "1":
        login = input("Введите логин: ").strip()
        role = input(
            "Введите роль (Администратор/Пользователь): "
        ).strip()
        age_text = input("Введите возраст: ").strip()

        # Проверка заполнения всех полей
        if not login or not role or not age_text:
            print("Ошибка: все поля обязательны для заполнения.")

        # Проверка допустимой роли
        elif role != "Администратор" and role != "Пользователь":
            print(
                "Ошибка: допустимы роли "
                "'Администратор' или 'Пользователь'."
            )

        # Проверка возраста
        elif not age_text.isdigit():
            print(
                "Ошибка: возраст должен быть целым "
                "неотрицательным числом."
            )

        else:
            age = int(age_text)

            # Проверка уникальности логина
            login_exists = False

            for user in users:
                if user[0] == login:
                    login_exists = True
                    break

            # Добавление пользователя, если логин уникален
            if login_exists:
                print(
                    "Пользователь с указанным логином "
                    "уже существует."
                )
            else:
                users.append([login, role, age])
                print("Пользователь добавлен.")

    # 2. Просмотр всех пользователей
    elif menu_choice == "2":
        if not users:
            print("Список пользователей пуст.")
        else:
            print("\nСписок пользователей:")
            print("Всего пользователей:", len(users))

            for number, user in enumerate(users, start=1):
                print(f"\nПользователь №{number}")
                print("Логин:", user[0])
                print("Роль:", user[1])
                print("Возраст:", user[2])

    # 3. Поиск пользователя по логину
    elif menu_choice == "3":
        search_login = input(
            "Введите логин для поиска: "
        ).strip()

        found_user = None

        # Линейный поиск по списку
        for user in users:
            if user[0] == search_login:
                found_user = user
                break

        if found_user is None:
            print("Пользователь не найден.")
        else:
            print("\nПользователь найден:")
            print("Логин:", found_user[0])
            print("Роль:", found_user[1])
            print("Возраст:", found_user[2])

    # 4. Фильтрация пользователей по роли
    elif menu_choice == "4":
        role_filter = input(
            "Введите роль для фильтрации "
            "(Администратор/Пользователь): "
        ).strip()

        filtered_users = []

        # Отбор всех пользователей с указанной ролью
        for user in users:
            if user[1] == role_filter:
                filtered_users.append(user)

        if not filtered_users:
            print("Пользователи с указанной ролью не найдены.")
        else:
            print("\nПользователи с ролью:", role_filter)

            for number, user in enumerate(filtered_users, start=1):
                print(f"\nПользователь №{number}")
                print("Логин:", user[0])
                print("Роль:", user[1])
                print("Возраст:", user[2])

    # 5. Поиск пользователя с максимальным возрастом
    elif menu_choice == "5":
        if not users:
            print("Список пользователей пуст.")
        else:
            # Сначала считаем первого пользователя самым старшим
            oldest_user = users[0]

            # Сравниваем возраст остальных пользователей
            for user in users[1:]:
                if user[2] > oldest_user[2]:
                    oldest_user = user

            print("\nПользователь с максимальным возрастом:")
            print("Логин:", oldest_user[0])
            print("Роль:", oldest_user[1])
            print("Возраст:", oldest_user[2])

    # 0. Выход из программы
    elif menu_choice == "0":
        print("Работа программы завершена.")
        break

    # Обработка неправильного пункта меню
    else:
        print("Ошибка: выберите существующий пункт меню.")
