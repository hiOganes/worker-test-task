# HR Worker Management System

Система управления работниками для HR-отдела с REST API, импортом Excel, Django Admin, пагинацией, фильтрацией и тестами.

## Technologies

- Python 3.12+
- Django 4.2+
- Django REST Framework
- drf-yasg (Swagger)
- django-filter
- openpyxl (Excel)
- Poetry 2.0+ (dependency management)

## Installation and start project with poetry

1. **Clone the repository**
    ```bash
    git clone git@github.com:hiOganes/store-test-task.git

2. **Install Poetry (if not installed)**
    ```bash
    pip install poetry

3. **Install dependencies**
    ```bash
    poetry install

4. **Apply migrations and create superuser**
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    python manage.py createsuperuser

5. **Start tests**
    ```bash
    python manage.py test .

6. **Start server**
    ```bash
    python manage.py runserver


## Installation and start project with docker

1. **Clone the repository**
    ```bash
    git clone git@github.com:hiOganes/store-test-task.git

2. **Install Poetry (if not installed)**
    ```bash
    docker compose up

3. **Create superuser**
    ```bash
    python manage.py createsuperuser

4. **Open new terminal**
    ```bash
    docker compose exec web python manage.py test .


## Endpoints

### - Open your browser and go to [OpenAPI](http://127.0.0.1:8001//swagger/)


## Тестирование импорта данных

### Подготовка Excel файла

Используйте шаблон **`example_import.xlsx`** с **табличным форматом**:

| first_name | middle_name | last_name | email | position |
|------------|-------------|-----------|-------|----------|
| **Обязательно** | **Необязательно** | **Обязательно** | **Обязательно** | **Обязательно** |
| John | Ivanovich | Doe | john.doe@company.com | Developer |
| Jane | Petrovna | Smith | jane.smith@company.com | Manager |

#### Правила формата:
- **Первая строка** = заголовки столбцов **ТОЧНО**:
  - `first_name`
  - `middle_name` (может быть пустым)
  - `last_name`
  - `email`
  - `position`
- **Обязательные поля**: `first_name`, `last_name`, `email`, `position`
- **`middle_name`** - необязательное (может отсутствовать)
- **Email** - должен быть **уникальным** и в **валидном формате**
- **Формат файла**: только **`.xlsx`** (не `.xls` или `.csv`)
- **Кодировка**: UTF-8 (автоматически обрабатывается)

#### Создание файла:
1. **Скачайте** `example_import.xlsx` из репозитория
2. **Откройте** в Excel/LibreOffice
3. **Заполните** данными работников с 2-й строки
4. **Сохраните** как `.xlsx`
5. **Проверьте** заголовки (без пробелов, точно как указано)


### Тестирование через Postman

Method: POST

URL: http://127.0.0.1:8001/api/workers/import/

Body → form-data:

Key: file
Value: выберите example_import.xlsx

Send