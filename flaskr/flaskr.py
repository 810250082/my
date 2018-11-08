import os
import sqlite3
from flask import Flask , request ,session , g , redirect , url_for , abort , \
    render_template , flash
import config


app = Flask(__name__)
#app.config.from_envvar('FLASKR_SETTINGS' , silent=True)
app.config.from_object(config)
app.secret_key = 'e\x91\x92\xe4<\xb6\xa4\xb3\xc6\xf2|\xdb\xb8I:e\xed\xc46\xbb\xb7\xf6\xf1\xc0'

def connect_db():
    rv = sqlite3.connect(app.config['DATABASE'])
    rv.row_factory = sqlite3.Row
    return rv

def get_db():
    if not hasattr(g , 'sqlite_db'):
        g.sqlite_db = connect_db()
    return g.sqlite_db

@app.teardown_appcontext
def close_db(error):
    if hasattr(g , 'sqlite_db'):
        g.sqlite_db.close()

def init_db():
    with app.app_context():
        db = get_db()
        with app.open_resource('schema.sql' , mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()

@app.route('/')
def show_entries():
    db = get_db()
    cur = db.execute('select title , text from entries order by id desc')
    entries = [dict(title=row[0] , text=row[1]) for row in cur.fetchall()]
    return render_template('show_entries.html' , entries = entries)

@app.route('/add')
def add_entry():
    db = get_db()
    db.execute('insert into entries(title , text) values (? ,?)', [request.args.get('title') , request.args.get('cont')])
    db.commit()
    return 'insert ok!'

if __name__ == "__main__":

    app.run(host='0.0.0.0' , debug=True)