# API tests for Yandex Samokat

Автотесты для учебного сервиса «Яндекс.Самокат».
Реализован по паттерну Page Object, с параметризацией тестов и отчётом в Allure.

## Технологии

- Python
- Selenium
- PyTest
- Allure

## Структура проекта

```
/
├─ allure-results/
├─ tests/
├─ conftest.py
├─ ...
```
## Установка
```
pip install -r requirements.txt
```

## Запуск тестов
```
pytest tests/ -v
```
