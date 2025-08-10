from telethon import TelegramClient, events
from telethon.errors import FloodWaitError, PeerIdInvalidError, ChatWriteForbiddenError
import asyncio
import time
import os

# Введи свои данные API
api_id = 'api_id'
api_hash = 'api_hash'
phone_number = 'phone_number'

# Удаляем существующую сессию, если она есть
session_name = 'session_name'
if os.path.exists(f'{session_name}.session'):
    os.remove(f'{session_name}.session')

# Создаем клиента
client = TelegramClient(session_name, api_id, api_hash)

# Список чатов для рассылки
chat_ids = ['@cookiestock_chat', '@cookie_roblox_5tore', '@rbxglobalchat']  # Можно использовать username 

# Сообщение для рассылки
message = "Ваше сообщение"

async def send_message_to_chats():
    for chat_id in chat_ids:
        try:
            await client.send_message(chat_id, message)
            print(f"Сообщение отправлено в чат {chat_id}")
        except FloodWaitError as e:
            print(f"Ошибка FloodWait: нужно подождать {e.seconds} секунд. Ждем...")
            time.sleep(e.seconds)
        except PeerIdInvalidError:
            print(f"Ошибка: неверный ID чата {chat_id}")
        except ChatWriteForbiddenError:
            print(f"Ошибка: нет прав на отправку сообщений в чат {chat_id}")
        except Exception as e:
            print(f"Неизвестная ошибка при отправке в чат {chat_id}: {e}")

async def main():
    await client.start(phone=phone_number)
    print("Клиент запущен.")
    while True:
        await send_message_to_chats()
        print("Ожидание 30 минут перед следующей рассылкой...")
        await asyncio.sleep(1800)  # 1800 секунд = 30 минут

if __name__ == '__main__':
    with client:
        client.loop.run_until_complete(main())
