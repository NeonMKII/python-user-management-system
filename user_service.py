
# Поиск пользователя по логину
def find_user(users, login):
    for user in users:
        if user["login"].lower() == login.lower():
            return user

    return None


# Добавление пользователя
def add_user(users, login, role, age):
    # Проверяем, существует ли пользователь
    if find_user(users, login) is not None:
        return False

    # Добавляем нового пользователя
    users.append({
        "login": login,
        "role": role,
        "age": age
    })

    return True
