from flask.ext.script import Manager
from flask_migrate import Migrate, MigrateCommand
from app.base_model import db
from run import app
from app.model import *

migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()