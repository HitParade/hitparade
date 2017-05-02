#!/usr/bin/env python

import os
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

from main import create_app
from commands import *

app, db = create_app()

from models import *

migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)
manager.add_command('load-teams', LoadTeams)
manager.add_command('load-players', LoadPlayers)
manager.add_command('load-games', LoadGames)
manager.add_command('load-bis-hist', LoadHistorical)
manager.add_command('update-games', UpdateGames)


if __name__ == '__main__':
    manager.run()
