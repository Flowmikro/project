# test
___
## Тестовое задание Python Developer.
### Реализованно
Создание API с использованием FastAPI и SQLAlchemy: ✔️
1. Создано простое API с использованием FastAPI, которая работает с
базой данных (SQLite) с помощью SQLAlchemy.
2. В базе данных храниться таблица User с полями id , username , email и
registration_date.  
3. Реализованы CRUD-операции для пользователей: создание, чтение,
обновление и удаление.
4. Реализована пагинация для получения списка пользователей.
___
Задача 2: Работа с данными и структурирование ✔️
1. Используя данные из таблицы User, реализована функцию, которая
подсчитывает количество пользователей, зарегистрированных за
последние 7 дней.
2. Реализована функцию, которая возвращает топ-5 пользователей с самыми
длинными именами.
3. Реализована функцию, которая определяет, какая доля пользователей имеет
адрес электронной почты, зарегистрированный в определенном домене
("example.com").
___
Задача 3: Объединить проект ✔️
___
Задача 4: Протестировать код ✔️
___
## Технологии 🖥️
Проект написан асинхронно  
FastAPI, SQLAlchemy, aiosqlite, alembic, uvicorn, pytest-asyncio
___
## Установка 
Установить репозиторий  
```commandline
https://github.com/Flowmikro/project.git
```
Перейти в директорию
```commandline
cd project
```
dsfsf
```commandline
docker build . -t fastapi_app:latest
```
```commandline
docker run -p 8000:8000 fastapi_app 
```
Перейти по адресу
```commandline
http://localhost:8000/docs
```
<h4>Второй способ</h4>
Активировать виртуальную вреду на Mac/Linux
```commandline
python3 -m venv venv
source venv/bin/activate
```
Активировать виртуальную вреду на Windows
```commandline
python -m venv venv
.\venv\Scripts\activate 
```
Установить пакеты
```commandline
pip install -r requirements.txt
```
Выполнить alembic миграцию
```commandline
alembic upgrade head             
```
Запустить тесты
```commandline
pytest test/            
```
