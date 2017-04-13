#!/usr/bin/env python

import os
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

from main import app, db
from commands import LoadTeams

app.config.from_object(os.environ['APP_SETTINGS'])

migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)
manager.add_command('load-teams', LoadTeams)


if __name__ == '__main__':
    manager.run()
