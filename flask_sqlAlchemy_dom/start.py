from flask import Flask
from database import db_session

app = Flask(__name__)
app.config.from_object('config')

@app.teardown_request
def shutdown_session(exception=None):
    db_session.remove()


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)