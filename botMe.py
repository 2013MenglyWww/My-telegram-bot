
import telebot
from telebot import types
import re

API_TOKEN = '7529486010:AAHoIAuQX-lhNX58VSSjGPyFzk2JC_TEmAk'  # ✅ ប្តូរជា Token របស់អ្នក
bot = telebot.TeleBot(API_TOKEN)

# ✅ លុប Webhook មុនពេល run
bot.remove_webhook()

# ✅ start command
@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add("គំរូ: 10 + 5 × 2")
    bot.send_message(
        message.chat.id,
        "សូមស្វាគមន៍មកកាន់ Bot គណិត!\n\nបញ្ចូលប្រមាណវិធីដូចជា:\n10 + 5 × 2 - 3 ÷ 2",
        reply_markup=markup
    )

# ✅ ប处理សារ math
@bot.message_handler(func=lambda message: True)
def calculate_math(message):
    expression = message.text.strip()

    # ប្តូរសញ្ញាឲ Python អាចយល់បាន
    expression = expression.replace('×', '*').replace('÷', '/').replace('–', '-').replace('%', '/100')

    # ត្រួតពិនិត្យបែបផែនប្រមាណវិធី
    if re.fullmatch(r'[0-9\.\+\-\*/\s]+', expression):
        try:
            result = eval(expression)
            bot.reply_to(message, f"ចម្លើយ៖ {result}")
        except ZeroDivisionError:
            bot.reply_to(message, "មិនអាចចែកនឹងសូន្យបានទេ!")
        except Exception:
            bot.reply_to(message, "មានបញ្ហាក្នុងការគណនា។ សូមពិនិត្យប្រមាណវិធីម្តងទៀត។")
    else:
        bot.reply_to(message, "សូមវាយតែប្រមាណវិធីគណិត: 10 + 5 × 2 - 3 ÷ 2")

# ✅ កំណត់ bot polling ដោយចាប់សម្រួល error
if __name__ == '__main__':
    while True:
        try:
            bot.infinity_polling()
        except Exception as e:
            print(f"Bot error: {e}")
