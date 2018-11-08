from flask import Flask
from ext import db

app = Flask(__name__)

db.init_app(app)


@app.route('/')
def index():
    return 'hello world!'


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)