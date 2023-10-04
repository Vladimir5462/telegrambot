import telebot
from telebot import types

bot = telebot.TeleBot('6649439126:AAHeUv0FYjetwcrBXCCEeA8WpD1g-_aPJ9o')

## Cтарт, начало и кнопки
@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup()
    btn1 = types.KeyboardButton('Первая команда')
    btn2 = types.KeyboardButton('Вторая')
    markup.row(btn1, btn2)
    btn3 = types.KeyboardButton('Третья ')
    btn4 = types.KeyboardButton('Четвертая')
    markup.row(btn3, btn4)

    bot.send_message(message.chat.id, f'<b>Privet, <u>{message.from_user.first_name}</u>!\n Главные кнопки: </b>', parse_mode='html', reply_markup=markup)

    bot.register_next_step_handler(message, on_click)

def on_click(message):
        if message.text == 'Первая команда':
            bot.send_message(message.chat.id, 'site open')
        elif message.text == 'Вторая':
            bot.send_message(message.chat.id, 'vtoroi')

## Ссылка на сайт
@bot.message_handler(commands=['site'])
def site(message):
    link_text = "[Нажми на текст](https://www.youtube.com)"
    bot.send_message(message.chat.id, parse_mode='Markdown', text=link_text)
## Список команд
@bot.message_handler(commands=['help'])
def main(message):
    bot.send_message(message.chat.id, '<b><u>Список команд:</u> \n /start - Запуск бота\n /site - Наш сайт\n /id - ID Пользователя </b>', parse_mode='html')
## Вывод айди
@bot.message_handler(commands=['id'])
def main(message):
    bot.reply_to(message, f'ID: {message.from_user.id}')

@bot.message_handler()
def info(message):
    if message.text.lower() == 'привет':   ## Текст от пользователя на которое будет отвечать бот
        bot.send_message(message.chat.id, f'<b>Здравствуйте, <u>{message.from_user.first_name}!</u> Введите команду "/help", чтобы ознакомиться со всем списком возможностей.</b>', parse_mode='html')
    elif message.text.lower() == 'hi':
        bot.send_message(message.chat.id, f'<b>Здравствуйте, <u>{message.from_user.first_name}!</u> Введите команду "/help", чтобы ознакомиться со всем списком возможностей.</b>', parse_mode='html')
    elif message.text.lower() == 'ghbdtn':
        bot.send_message(message.chat.id, f'<b>Здравствуйте, <u>{message.from_user.first_name}!</u> Введите команду "/help", чтобы ознакомиться со всем списком возможностей.</b>', parse_mode='html')
## Отправляем фото в бота и вывод кнопок
@bot.message_handler(content_types=['photo'])
def get_photo(message):
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton('Перейти на сайт', url='https://www.youtube.com/watch?v=RpiWnPNTeww&list=PL0lO_mIqDDFUev1gp9yEwmwcy8SicqKbt&index=3')
    btn2 = types.InlineKeyboardButton('Перейти на сайт', url='https://www.youtube.com/watch?v=RpiWnPNTeww&list=PL0lO_mIqDDFUev1gp9yEwmwcy8SicqKbt&index=3')
    markup.row(btn1, btn2)
    btn3 = types.InlineKeyboardButton('Перейти на сайт', url='https://www.youtube.com/watch?v=RpiWnPNTeww&list=PL0lO_mIqDDFUev1gp9yEwmwcy8SicqKbt&index=3')
    btn4 = types.InlineKeyboardButton('Удалить', callback_data='delete')
    markup.row(btn3, btn4)
    bot.reply_to(message, 'Мы получили ваше фото!', reply_markup=markup)

@bot.callback_query_handler(func=lambda callback: True)
def callback_message(callback):
    if callback.data == 'delete':
        bot.delete_message(callback.message.chat.id, callback.message.message_id - 1)

bot.polling(none_stop=True)
