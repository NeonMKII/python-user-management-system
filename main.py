
# Импорт функций из собственных модулей

from validation import validate_age, validate_login, validate_role
from user_service import add_user, find_user
from reports import filter_users_by_role, get_oldest_user
from utils import format_user


# Список для хранения пользователей
users = []


# Главное меню программы
while True:
    print("\nСистема управления пользователями")
    print("1 — Добавить пользователя")
    print("2 — Показать всех пользователей")
    print("3 — Найти пользователя по логину")
    print("4 — Показать пользователей по роли")
    print("5 — Показать пользователя с максимальным возрастом")
    print("0 — Выход")

    choice = input("Выберите пункт: ").strip()

    # 1. Добавление пользователя
    if choice == "1":
        login = input("Введите логин: ").strip()
        role = input("Введите роль: ").strip()
        age_text = input("Введите возраст: ").strip()

        # Проверяем введённые данные
        if (
            not validate_login(login)
            or not validate_role(role)
            or not validate_age(age_text)
        ):
            print("Ошибка: проверьте логин, роль и возраст.")

        # Проверяем уникальность логина и добавляем пользователя
        elif not add_user(users, login, role, int(age_text)):
            print("Пользователь с указанным логином уже существует.")

        else:
            print("Пользователь добавлен.")

    # 2. Просмотр всех пользователей
    elif choice == "2":
        if not users:
            print("Список пользователей пуст.")
        else:
            print("\nСписок пользователей:")
            print("Всего пользователей:", len(users))

            for number, user in enumerate(users, start=1):
                print(f"{number}. {format_user(user)}")

    # 3. Поиск пользователя по логину
    elif choice == "3":
        search_login = input("Введите логин для поиска: ").strip()

        user = find_user(users, search_login)

        if user is None:
            print("Пользователь не найден.")
        else:
            print("Пользователь найден:")
            print(format_user(user))

    # 4. Фильтрация пользователей по роли
    elif choice == "4":
        role = input(
            "Введите роль (Администратор/Пользователь): "
        ).strip()

        filtered_users = filter_users_by_role(users, role)

        if not filtered_users:
            print("Пользователи с указанной ролью не найдены.")
        else:
            print("\nРезультаты фильтрации:")

            for number, user in enumerate(filtered_users, start=1):
                print(f"{number}. {format_user(user)}")

    # 5. Поиск пользователя с максимальным возрастом
    elif choice == "5":
        user = get_oldest_user(users)

        if user is None:
            print("Список пользователей пуст.")
        else:
            print("Пользователь с максимальным возрастом:")
            print(format_user(user))

    # 0. Выход из программы
    elif choice == "0":
        print("Работа программы завершена.")
        break

    # Обработка неправильного пункта меню
    else:
        print("Предупреждение: выберите пункт меню от 0 до 5.")
