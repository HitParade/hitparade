import re
import boto3
from stattlepy import Stattleship
from config import get_env_variable


def get_stattleship_client():

    s = Stattleship()
    s.set_token(get_env_variable('STATTLESHIP_TOKEN'))

    return s

def s3_get_file(bucket, key, file):

    key = boto3.resource('s3').Object(bucket, key).get()
    with file as f:
        chunk = key['Body'].read(1024*8)
        while chunk:
            f.write(chunk)
            chunk = key['Body'].read(1024*8)


first_cap_re = re.compile('(.)([A-Z][a-z]+)')
all_cap_re = re.compile('([a-z0-9])([A-Z])')

def convert_camel2snake(name):
    name = name.replace("BABIP", "BaBIP")
    s1 = first_cap_re.sub(r'\1_\2', name)
    return all_cap_re.sub(r'\1_\2', s1).lower()
