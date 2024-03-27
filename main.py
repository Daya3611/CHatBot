import telebot
import google.generativeai as genai
bot = telebot.TeleBot("6736012710:AAHAPDiMlU91baWlRjVzA0pA091VQcqdg2s", parse_mode=None) # You can set parse_mode by default. HTML or MARKDOWN
genai.configure(api_key="AIzaSyCyNiHkOk9S5Us6oe4uUgEqIysUAyoCnVk")

# Set up the model
generation_config = {
  "temperature": 0.9,
  "top_p": 1,
  "top_k": 1,
  "max_output_tokens": 2048,
}

safety_settings = [
  {
    "category": "HARM_CATEGORY_HARASSMENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_HATE_SPEECH",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
]

model = genai.GenerativeModel(model_name="gemini-1.0-pro",
                              generation_config=generation_config,
                              safety_settings=safety_settings)

convo = model.start_chat(history=[
])


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Hello! This Bot Is made By Dayanand Gawade @dayanand_gawade")
 
@bot.message_handler(func=lambda m: True)
def echo_all(message):
    convo.send_message(message.text)
    response = (convo.last.text)
    bot.reply_to(message, response)
 
bot.infinity_polling()

# pip install pyTelegramBotAPI
# pip install google-generativeai
# Python main.py