import telebot
from pyowm import OWM

# API-ключи
owm = OWM("c7537f90396e238b00fc4c29c1763eb2")
bot = telebot.TeleBot("6057563499:AAF9ZosdCUz0YIThrT-hwQtS6FXvLEo9iVU")


# Функция для обработки сообщений
@bot.message_handler(commands=['start', 'help'])
def start(message):
    bot.send_message(message.chat.id,
                     "Привет! Я могу рассказать тебе о погоде. Просто отправь мне название города.(бот от компании Migen-AI)")


@bot.message_handler(content_types=['text'])
def get_weather(message):
    city = message.text
    try:
        mgr = owm.weather_manager()
        observation = mgr.weather_at_place(city)
        w = observation.weather
        temp = w.temperature('celsius')['temp']
        feels_like = w.temperature('celsius')['feels_like']
        wind = w.wind()['speed']
        humidity = w.humidity

        # Определение одежды
        clothes = []
        if temp > 25:
            clothes.append("футболка")
            clothes.append("шорты")
        elif temp > 15:
            clothes.append("рубашка")
            clothes.append("джинсы")
        elif temp > 10:
            clothes.append("свитер")
            clothes.append("брюки")
        else:
            clothes.append("куртка")
            clothes.append("шапка")
            clothes.append("шарф")

        # Выбор смайлика
        emoji = ""
        if temp > 25:
            emoji = "☀️"
        elif temp > 15:
            emoji = "⛅"
        elif temp > 10:
            emoji = "☁️"
        else:
            emoji = "❄️"

        answer = f"В городе {city} {emoji}:\n\nТемпература: {temp:.1f}°C\nОщущается как: {feels_like:.1f}°C\nВетер: {wind:.1f} м/с\nВлажность: {humidity}%"
        answer += "\n\nРекомендуемая одежда: " + ", ".join(clothes)
        bot.send_message(message.chat.id, answer)
    except:
        bot.send_message(message.chat.id, "Пожалуйста, введите корректное название города.")


# Запуск бота
bot.polling()