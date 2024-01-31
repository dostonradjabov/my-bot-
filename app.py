from flask import Flask
import telegram
# Create the application instance
TOKEN ='6765226621:AAExg4YCtHJPi3vwJcZdLtAGIBRKGGU9YxU'
bot = telegram.Bot(TOKEN)
chat_id = '5377837814'
app = Flask(__name__)

@app.route('/')
@app.route('/',methods=["POST"])
def index():
    bot.send_message(chat_id,text="hello word")
    return 'index page'

if __name__=="__main__":
    app.run(debug=True)