from flask import Flask


app = Flask(__name__)


@app.route('/add')
def add():
    a = 1
    return 'ok'


from blue.user import user
app.register_blueprint(user, url_prefix='/user')


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
