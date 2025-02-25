# 2331818521
# 7270557558:AAEK8qmmeICFHI0ccDzJN1vGW87qBkv4iiA
# path_to_your_photo.jpg
# D:\\Code Sources\\С++\\path_to_your_photo.jpg
import telebot
import os
import time

# Токен вашего бота (полученный от BotFather)
bot_token = '7270557558:AAEK8qmmeICFHI0ccDzJN1vGW87qBkv4iiA'

bot = telebot.TeleBot(bot_token)

# Путь к папке с фото
photo_directory = 'D:\\CodeSources\\С++\\'  # Папка с изображением

# Обрабатываем команду /start
@bot.message_handler(commands=['start'])
def send_photos(message):
    chat_id = message.chat.id  # ID чата, в который бот будет отправлять фото
    
    try:
        while True:
            for filename in os.listdir(photo_directory):
                if filename == 'path_to_your_photo.jpg':  # Ищем конкретное фото
                    photo_path = os.path.join(photo_directory, filename)
                    with open(photo_path, 'rb') as photo_file:
                        bot.send_photo(chat_id, photo_file)
                    time.sleep(1)  # Задержка перед следующим фото
                    break  # Если нашёл фото, выходим из цикла
    except Exception as e:
        print(f"Error: {e}")
        time.sleep(5)

# Запускаем бота
bot.polling()
