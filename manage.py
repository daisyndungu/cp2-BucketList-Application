import os
from flask_script import Manager, Server
from flask_migrate import Migrate, MigrateCommand
from bucketlist.models import db, app
from bucketlist.view import *

db.configure_mappers()
migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)
manager.add_command("runserver", Server())
if __name__ == '__main__':
    manager.run()
