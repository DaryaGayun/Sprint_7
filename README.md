# API tests for Yandex Samokat

Автотесты для учебного сервиса «Яндекс.Самокат».
Его документация: qa-scooter.praktikum-services.ru/docs/

## НЕСООТВЕСТВИЯ ДОКУМЕНТАЦИИ

1. При создании курьера только login и password являются обязательными (firstName необязателен)
2. При создании дубликата курьера (существующий login) сообщение об ошибке не совпадает.
3. При входе курьера без указания password - происходит зависание ответа 504.
4. При удалении курьера неверный код 404 (вместо 400) и текст об ошибке другой. 

## Технологии

- Python
- PyTest
- Allure

## Структура проекта

```
/
├─ allure-results/
├─ tests/
├─ api_client.py
├─ conftest.py
├─ data.py
├─ helpers.py
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

# Запустить тесты с генерацией Allure-отчёта
```
pytest tests/ -v --alluredir=allure_results
```

# Сгенерировать HTML-отчёт
```
allure serve allure_results
```
