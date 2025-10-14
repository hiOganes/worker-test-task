FROM python:3.13-slim

# Установка системных зависимостей
RUN apt-get update && apt-get install -y \
    gcc \
    curl \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Установка Poetry
ENV POETRY_HOME=/opt/poetry
ENV POETRY_VIRTUALENVS_CREATE=false
ENV PYTHONUNBUFFERED=1
ENV PATH="/opt/poetry/bin:$PATH"

RUN curl -sSL https://install.python-poetry.org | python3 - \
    && poetry config virtualenvs.create false

WORKDIR /var/www/hr-worker

# Копируем файлы зависимостей
COPY pyproject.toml poetry.lock ./

# Установка зависимостей (Poetry 2.0+ синтаксис)
RUN poetry install --only main --no-interaction --no-ansi

# Копируем код
COPY . .

# Создаем директории
RUN mkdir -p static media

# Открываем порт
EXPOSE 8000

# Healthcheck
HEALTHCHECK --interval=30s --timeout=10s --start-period=30s --retries=3 \
    CMD curl -f http://localhost:8000/ || exit 1

CMD ["sh", "-c", "python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]