print("Система управления пользователями")
print("Проверка данных пользователя")

full_name = input("Введите ФИО: ").strip()
login = input("Введите логин: ").strip()
role = input("Введите роль (Администратор/Пользователь): ").strip()
birth_year_text = input("Введите год рождения: ").strip()
current_year_text = input("Введите текущий год: ").strip()

# Сначала проверяем обязательные текстовые поля
if not full_name or not login or not role:
    print("Ошибка: ФИО, логин и роль обязательны для заполнения.")

# Проверяем, что годы состоят из цифр
elif not birth_year_text.isdigit() or not current_year_text.isdigit():
    print("Ошибка: год рождения и текущий год должны быть целыми числами.")

else:
    birth_year = int(birth_year_text)
    current_year = int(current_year_text)

    # Проверяем допустимость роли
    if role != "Администратор" and role != "Пользователь":
        print("Ошибка: допустимы роли 'Администратор' или 'Пользователь'.")

    # Проверяем диапазон года рождения
    elif birth_year < 1900 or birth_year > current_year:
        print("Ошибка: проверьте корректность года рождения.")

    else:
        # Если все проверки пройдены, вычисляем возраст
        user_age = current_year - birth_year

        print("\nКарточка пользователя")
        print(f"ФИО: {full_name}")
        print(f"Логин: {login}")
        print(f"Роль: {role}")
        print(f"Возраст: {user_age}")