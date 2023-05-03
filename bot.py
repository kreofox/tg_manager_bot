import telebot
from telebot.types import Message
from time import sleep
from twilio.rest import Client 

account_sid = 'your_account_sid'
auth_token = 'your_auth_token'
twilio_phone_number = 'your_twilio_phone_number'
your_phone_number = 'your_phone_number'

bot_token = 'your_bot_token'
bot = telebot.TeleBot(bot_token)

phone_numbers = ['invitation numbers']

message = 'Hello world'

@bot_message_halder(content_types = ['text'])
def haleder_text_message(message: Message):
    user_reasponse = message.text
    bot.reply_to(message, 'Hello world')
    client.message.create.create(
        to= phone_numbers[0],
        from_ = twilio_phone_number,
        body =user_reasponse
    )

for numbers in phone_numbers:
    bot.send_message(numbers, message)
    sleep(1)

bot.polling(non_stop=True)