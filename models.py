from pydantic import BaseModel
from datetime import date

# Модель для логина пользователя
class UserLogin(BaseModel):
    username: str
    password: str

# Модель для токена авторизации
class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"

# Модель для информации о зарплате
class SalaryInfo(BaseModel):
    current_salary: float
    next_raise_date: date 