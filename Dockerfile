# Указываем базовый образ
FROM python:3.12-slim

# Устанавливаем рабочую директорию в контейнере
WORKDIR /app

# Копируем остальные файлы проекта в контейнер
COPY requirements.txt ./

RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

COPY . .

ENV DJANGO_SETTINGS_MODULE='config.settings'

RUN mkdir -p /app/static

RUN mkdir -p /app/media

# Открываем порт 8000 для взаимодействия с приложением
EXPOSE 8000

# Определяем команду для запуска приложения
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
