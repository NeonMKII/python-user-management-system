
# Допустимые роли пользователей
ALLOWED_ROLES = ("Администратор", "Пользователь")


# Проверка логина
def validate_login(login):
    login = login.strip()
    return bool(login) and len(login) >= 3


# Проверка роли
def validate_role(role):
    return role in ALLOWED_ROLES


# Проверка возраста
def validate_age(age_text):
    return age_text.isdigit() and 0 < int(age_text) < 120
