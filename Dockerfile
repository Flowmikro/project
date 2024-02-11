FROM python:3.11-alpine


RUN mkdir /fastapi_app
WORKDIR /fastapi_app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

CMD ["sh", "-c", "pytest test/ && alembic upgrade head && uvicorn main:app --host 0.0.0.0 --port 8000"]

