import os

def get_env_variable(var_name):
    """ Get the environment variable or return exception """
    try:
        return os.environ[var_name]
    except KeyError:
        error_msg = "Set the %s env variable" % var_name
        raise Exception(error_msg)


class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = 'this-really-needs-to-be-changed'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    SQLALCHEMY_DATABASE_URI = "postgres://" + \
        get_env_variable('POSTGRES_USER') + ":" + \
        get_env_variable('POSTGRES_PASSWORD') + "@" + \
        get_env_variable('POSTGRES_HOST') + "/" + \
        get_env_variable('POSTGRES_DB')


class ProductionConfig(Config):
    DEBUG = False


class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class TestingConfig(Config):
    TESTING = True

    DB_NAME = get_env_variable('POSTGRES_DB') + "-testing"

    SQLALCHEMY_DATABASE_URI = "postgres://" + \
        get_env_variable('POSTGRES_USER') + ":" + \
        get_env_variable('POSTGRES_PASSWORD') + "@" + \
        get_env_variable('POSTGRES_HOST') + "/" + \
        get_env_variable('POSTGRES_DB') + "-testing"
