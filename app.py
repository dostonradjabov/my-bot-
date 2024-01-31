from flask import Flask, request
import telegram
# Create the application instance
app = Flask(__name__)

TOKEN ='6765226621:AAExg4YCtHJPi3vwJcZdLtAGIBRKGGU9YxU'
bot = telegram.Bot(TOKEN)
chat_id = '5377837814'

# route for index page
@app.route('/', methods=['POST'])
def index():
    print('index page')
    #bot.send_message(chat_id=chat_id, text='Word')
    return 'index page'