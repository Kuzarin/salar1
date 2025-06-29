from datetime import date

# Моковые пользователи — в реальном проекте тут была бы база данных
users_db = {
    "alice": {
        "username": "alice",
        "password": "wonderland",
        "salary": 120000.0,
        "next_raise_date": date(2024, 12, 1)
    },
    "bob": {
        "username": "bob",
        "password": "builder",
        "salary": 95000.0,
        "next_raise_date": date(2024, 10, 15)
    }
}

def authenticate_user(username: str, password: str):
    """
    Проверяем логин и пароль пользователя. Если всё ок — возвращаем пользователя,
    иначе — None
    """
    user = users_db.get(username)
    if user and user["password"] == password:
        return user
    return None 