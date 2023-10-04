import telebot
from extensions import APIException, CurrencyConverter
import config

bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(commands=['start', 'help'])
def handle_start_help(message):
    bot.send_message(message.chat.id, f"Здравствуйте, {message.from_user.first_name}! Вот мой бот конвертации валют.\n"
                                      "Напишите сообщение в формате:\n"
                                      "|Название первой валюты|, "
                                      "|Название второй валюты|, "
                                      "|Нужное количество|.\n"
                                      "Пример: USD EUR 100\n"
                                      "Также, можно в нижнем регистре!\n"
                                      "Для получения списка доступных валют: /values.")


@bot.message_handler(commands=['values'])
def handle_values(message):
    values = CurrencyConverter.get_supported_currencies()
    bot.send_message(message.chat.id, "Доступные валюты:\n" + "\n".join(values))


@bot.message_handler(content_types=['text'])
def handle_text(message):
    try:
        text = message.text.lower()
        base, quote, amount = message.text.split()
        base = base.upper()
        quote = quote.upper()
        result = CurrencyConverter.get_price(base, quote, float(amount))
        bot.send_message(message.chat.id, f"{amount} {base} = {result} {quote}")
    except ValueError:
        bot.send_message(message.chat.id,"Вы указали неправильный текст. Необходимо написать название первой валюты, второй и количество!\n"
                                         "Пример: USD RUB 1")
    except APIException as e:
        bot.send_message(message.chat.id, f"Ошибка: {str(e)}")


if __name__ == '__main__':
    bot.polling(none_stop=True)
