# Використання базового образу Python з Alpine Linux
FROM python:3.12.3-alpine3.18

# Встановлення залежностей для PostgreSQL
RUN apk update && \
    apk add --no-cache postgresql-dev gcc python3-dev musl-dev

# Створення та перехід до директорії додатка
WORKDIR /app

# Копіювання файлів залежностей
COPY requirements.txt /app/

# Встановлення залежностей за допомогою pip
RUN pip install --no-cache-dir -r requirements.txt

# Копіювання всіх файлів додатка до контейнера
COPY . /app/

# Встановлення змінних середовища Django
ENV DJANGO_SETTINGS_MODULE=doc_manager.settings

# Використання порту 8000 для з'єднання
EXPOSE 8000

# Команда для запуску Django сервера
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "doc_manager.wsgi:application"]
