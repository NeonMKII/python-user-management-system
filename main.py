print("=== Система управления пользователями ===")

# Получаем данные пользователя
full_name = input("Введите ФИО: ")
login = input("Введите логин: ")
role = input("Введите роль: ")
birth_year = int(input("Введите год рождения: "))
current_year = int(input("Введите текущий год: "))

# Выполняем вычисление возраста
user_age = current_year - birth_year

# Выводим карточку пользователя
print("\n--- Карточка пользователя ---")
print(f"ФИО: {full_name}")
print(f"Логин: {login}")
print(f"Роль: {role}")
print(f"Возраст: {user_age}")