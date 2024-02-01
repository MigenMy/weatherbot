import telebot
from pyowm import OWM

# API-ключи
owm = OWM("c7537f90396e238b00fc4c29c1763eb2")
bot = telebot.TeleBot('6137705667:AAFk0Jvmhfxf2s8xGjEAdzEAFfk2UlvKIek')

# Функция для обработки сообщений
@bot.message_handler(commands=['start', 'help'])
def start(message):
    bot.send_message(message.chat.id, "Привет! Я могу рассказать тебе о погоде. Просто отправь мне название города.")

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
        answer = f"В городе {city}:\n\nТемпература: {temp:.1f}°C\nОщущается как: {feels_like:.1f}°C\nВетер: {wind:.1f} м/с\nВлажность: {humidity}%"
        bot.send_message(message.chat.id, answer)
    except:
        bot.send_message(message.chat.id, "Пожалуйста, введите корректное название города.")

# Запуск бота
bot.polling()
