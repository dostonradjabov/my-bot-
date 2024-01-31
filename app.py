from flask import Flask
import telegram
# Create the application instance

app = Flask(__name__)
TOKEN ='6765226621:AAExg4YCtHJPi3vwJcZdLtAGIBRKGGU9YxU'
bot = telegram.Bot(TOKEN)
chat_id = '5377837814'

# route for index page
@app.route('/')
def index():
    bot.send_message(chat_id=chat_id, text='Hello World!!!')
    return 'index page'