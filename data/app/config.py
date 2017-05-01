import os

def get_env_variable(var_name, raise_on_unset=True):
    """ Get the environment variable or return exception """
    try:
        return os.environ[var_name]
    except KeyError:
        error_msg = "Set the %s env variable" % var_name
        if raise_on_unset:
            raise Exception(error_msg)

    return None


class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = 'this-really-needs-to-be-changed'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    AWS_ACCESS_KEY_ID = get_env_variable("AWS_ACCESS_KEY_ID", raise_on_unset=False)
    AWS_SECRET_ACCESS_KEY = get_env_variable("AWS_SECRET_ACCESS_KEY", raise_on_unset=False)
    AWS_S3_BUCKET_NAME = "hit-parade-bis"
    AWS_S3_BUCKET_BASE_KEY = "2017"

    BIS_HISTORICAL_ZIP = "HistData2.zip"


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
