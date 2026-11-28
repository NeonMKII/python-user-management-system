
# Форматирование информации о пользователе
def format_user(user):
    return (
        f'{user["login"]} | '
        f'{user["role"]} | '
        f'возраст: {user["age"]}'
    )
