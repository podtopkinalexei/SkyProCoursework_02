# Парсер вакансий с HeadHunter

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)

Проект представляет собой консольное приложение для поиска и анализа вакансий с платформы HeadHunter (hh.ru) с возможностью фильтрации и сохранения результатов.

## 📌 Основные возможности

- 🔍 Поиск вакансий по ключевым словам
- 📂 Сохранение результатов в JSON-файл
- 🎯 Фильтрация вакансий по:
  - Ключевым словам
  - Диапазону зарплат
  - Количеству (топ-N)
- 📊 Сравнение вакансий по уровню зарплат
- 🚀 Интуитивно понятный консольный интерфейс

## ⚙️ Установка и запуск

1. Клонируйте репозиторий:
```bash
git clone https://github.com/podtopkinalexei/SkyProCoursework_02.git
cd hh-parser
```

2. Установите зависимости:

```bash
pip install -r requirements.txt
```

3. Запустите приложение:

```bash
python main.py
```

## 🛠 Техническая реализация

### Архитектура проекта
```text
project/
├── src/                  # Исходный код
│   ├── abstract_classes/ # Абстрактные классы
│   ├── api/              # Модули работы с API
│   ├── models/           # Модели данных
│   ├── utils/            # Вспомогательные функции
│   └── main.py          # Точка входа
├── tests/               # Тесты
└── data/                # Примеры данных
```

### Основные компоненты

Класс Vacancy:

Хранение данных о вакансии

Сравнение вакансий по зарплате

Валидация данных

HeadHunterAPI:

Подключение к API hh.ru

Парсинг результатов поиска

Обработка ошибок

JSONHandler:

Сохранение данных в JSON

Чтение данных из файла

Удаление дубликатов

## 🧪 Тестирование

Запуск тестов:

```bash
pytest -v --cov=src --cov-report=html
```

Покрытие тестами:

Модульные тесты - 95%

Интеграционные тесты - 85%

## 📄 Лицензия
Проект распространяется под лицензией MIT. Подробнее см. в файле LICENSE.

## ✉️ Контакты
Автор: [PodtopkinAlexei]
Email: podtopkinalexei@gmail.com
GitHub: @podtopkinalexei