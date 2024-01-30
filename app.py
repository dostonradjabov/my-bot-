from flask import Flask
import telegram
# Create the application instance
app = Flask(__name__)

@app.route('/')
def index():
    return 'index page'

if __name__=="__main__":
    app.run(debug=True)