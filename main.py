# Импортируем всё необходимое из FastAPI и стандартных библиотек тест
from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from datetime import timedelta, date
# Импортируем свои модули
from models import UserLogin, Token, SalaryInfo
from auth import create_access_token, verify_token
from users import authenticate_user, users_db

# Создаём экземпляр приложения FastAPI
app = FastAPI(title="Salaries API", description="REST API для просмотра зарплаты и даты следующего повышения с авторизацией")

# Эндпоинт для авторизации. Принимает логин и пароль, возвращает токен
@app.post("/login", response_model=Token)
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(form_data.username, form_data.password)
    if not user:
        # Если пользователь не найден или пароль неверный — ошибка
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Incorrect username or password")
    # Генерируем токен на 30 минут
    access_token = create_access_token(data={"sub": user["username"]}, expires_delta=timedelta(minutes=30))
    return {"access_token": access_token, "token_type": "bearer"}

# Эндпоинт для получения зарплаты. Требует валидный токен
@app.get("/salary", response_model=SalaryInfo)
def get_salary_info(username: str = Depends(verify_token)):
    user = users_db.get(username)
    if not user:
        # Если пользователя нет в базе — ошибка
        raise HTTPException(status_code=404, detail="User not found")
    # Возвращаем зарплату и дату следующего повышения
    return SalaryInfo(current_salary=user["salary"], next_raise_date=user["next_raise_date"]) 