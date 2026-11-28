
# Фильтрация пользователей по роли
def filter_users_by_role(users, role):
    return [
        user for user in users
        if user["role"] == role
    ]


# Поиск пользователя с максимальным возрастом
def get_oldest_user(users):
    if not users:
        return None

    return max(users, key=lambda user: user["age"])
