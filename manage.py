import os
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from bucketlist.run import app, db
from bucketlist import config

app.config.from_object("bucketlist.config.DevelopmentConfig")
manager = Manager(app)
migrate = Migrate(app, db)
manager.add_command('db', MigrateCommand)
if __name__ == '__main__':
    manager.run()
