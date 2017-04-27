import os

from flask_script import Manager, Server
from flask_migrate import Migrate, MigrateCommand

from bucketlist import db, app
from bucketlist.view import BucketListItemView, BucketlistView
from bucketlist.user import UserLogin, UserRegistration
from bucketlist import routes

db.configure_mappers()
migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)
manager.add_command("runserver", Server())
if __name__ == '__main__':
    manager.run()
