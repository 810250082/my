from flask_migrate import Migrate, MigrateCommand
from ext import db
from flask_script import Manager
from flask import Flask
from config import DEFAULT_DB_URI, MY_DOM_DB_URI
import models
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = DEFAULT_DB_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_BINDS'] = {
    'my_dom': MY_DOM_DB_URI,
}
db.init_app(app)
migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()