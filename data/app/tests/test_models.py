import os
import unittest
import tempfile
from flask_migrate import Migrate, upgrade, init
from sqlalchemy_utils import database_exists, create_database, drop_database
from sqlalchemy.exc import AmbiguousForeignKeysError

os.environ['APP_SETTINGS'] = "app.config.TestingConfig"
from app.main import create_app
from app.models import Game

class HitParadeTestCase(unittest.TestCase):

    def setUp(self):

        app, db = create_app()

        self.app = app
        self.db = db

        migrate = Migrate(app, db)

        with app.app_context():

            if not database_exists(app.config['SQLALCHEMY_DATABASE_URI']):
                create_database(app.config['SQLALCHEMY_DATABASE_URI'])

            upgrade()


    def tearDown(self):

        drop_database(self.app.config['SQLALCHEMY_DATABASE_URI'])


    def test_game_basic(self):

        g = Game(season='2017')
        g.save()


    def test_game_update_ss_fail(self):

        g = Game(season='2017')

        with self.assertRaises(AmbiguousForeignKeysError) as context:
            g.update_from_ss()



if __name__ == '__main__':
    unittest.main()
