from telethon import TelegramClient, events
from telethon.errors import FloodWaitError, PeerIdInvalidError, ChatWriteForbiddenError, SendCodeUnavailableError
import asyncio
import time
import os

# Введи свои данные API
api_id = '26149338'
api_hash = 'd05903ca9a75adb39a732336eb41a871'
phone_number = '+1 220 977 8849'

# Удаляем существующую сессию, если она есть
session_name = 'session_name'
if os.path.exists(f'{session_name}.session'):
    os.remove(f'{session_name}.session')

# Создаем клиента
client = TelegramClient(session_name, api_id, api_hash)

# Список чатов для рассылки
chat_ids = ['@cookiestock_chat', '@cookie_roblox_5tore', '@rbxglobalchat']  # Можно использовать username 

# Сообщение для рассылки
message = "Продам: Авто рассылка в Telegram - 100р                                                Верифицированный 18+ Аккаунт (В наличии 2 шт) - 100р                                      Байпасс/Способ 17- вериф/невериф - 30р                                                                                    И да, это сообщение отправлено той самой авто рассылкой"

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
    try:
        await client.start(phone=phone_number)
        print("Клиент запущен.")
    except SendCodeUnavailableError:
        print("Ошибка: все методы отправки кода подтверждения были использованы. Пожалуйста, попробуйте позже.")
        return
    except Exception as e:
        print(f"Неизвестная ошибка при запуске клиента: {e}")
        return

    while True:
        await send_message_to_chats()
        print("Ожидание 30 минут перед следующей рассылкой...")
        await asyncio.sleep(1800)  # 1800 секунд = 30 минут

if __name__ == '__main__':
    with client:
        client.loop.run_until_complete(main())
