import os
import unittest
import coverage
from flask_cors import CORS

from flask_script import Manager, Server
from flask_migrate import Migrate, MigrateCommand

from bucketlist import db, create_app
from bucketlist.view import BucketListItemView, BucketlistView
from bucketlist.user import UserLogin, UserRegistration


app = create_app('development')
CORS(app)
db.configure_mappers()
migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)
manager.add_command("runserver", Server())


@manager.command
def test():
    """Runs the unit tests without test coverage."""
    tests = unittest.TestLoader().discover('bucketlist/tests',
                                           pattern='test*.py')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    return 1


if __name__ == '__main__':
    manager.run()
