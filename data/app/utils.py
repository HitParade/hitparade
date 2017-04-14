from stattlepy import Stattleship
from config import get_env_variable

def get_stattleship_client():

    s = Stattleship()
    s.set_token(get_env_variable('STATTLESHIP_TOKEN'))

    return s
