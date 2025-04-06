# Bot Publisher

Этот скрипт отправляет случайный комикс XKCD в Telegram-чат.

## Требования

Python 3.8+

Виртуальное окружение (рекомендуется)

Telegram Bot API Token

Установленные зависимости

## Установка и запуск

1. Настройка окружения
   
- Клонируем репозиторий

- Создаем виртуальное окружение
```
python -m venv venv
```
- Активируем виртуальное окружение

Для Windows
```
venv\Scripts\activate
```
Для macOS и Linux
```
source venv/bin/activate
```

2. Установка зависимостей
```
pip install -r requirements.txt
```
4. Создание .env файла

Создайте файл .env в корне проекта и добавьте в него:
```
TG_TOKEN=your_telegram_bot_token
CHAT_ID=your_chat_id
```
Замените `your_telegram_bot_token` на токен вашего Telegram-бота, а `your_chat_id` на ID чата, куда будут отправляться комиксы.

5. Запуск бота
```
python publisher.py
```

## Как работает скрипт

- Получает последний номер комикса с XKCD.

- Выбирает случайный комикс из доступных.

- Загружает его изображение и описание.

- Отправляет комикс в Telegram-чат через бот API.
