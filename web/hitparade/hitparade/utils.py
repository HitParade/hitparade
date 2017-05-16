import os
import re
import json
import pprint
import datetime
import dateutil.parser
import random
import requests
import tempfile
import subprocess
import boto3
import botocore

from stattlepy import Stattleship
from django.core.exceptions import ImproperlyConfigured
from django.conf import settings


def get_random_num_excluding(range_, exclude):

    # If a tuple is passed, expand it to full range (list)
    if type(range_) == 'tuple':
        range_ = range(expand(range_))

    if exclude not in range_:
        raise ValueError("Excluded number should be within range")

    index = range_.index(exclude)

    front_range = range(0, index+1)
    back_range = range(index+2, len(range_)+1)

    numbers = front_range + back_range
    return random.choice(numbers)


def v_url(pattern):
    vs = "|".join(settings.ALLOWED_VERSIONS)
    return r"^(?P<version>(%s))/%s" % (vs, pattern)


def get_env_variable(var_name):
    """ Get the environment variable or return exception """
    try:
        return os.environ[var_name]
    except KeyError:
        error_msg = "Set the %s env variable" % var_name
        raise ImproperlyConfigured(error_msg)


def get_stattleship_client():

    s = Stattleship()
    s.set_token(get_env_variable('STATTLESHIP_TOKEN'))

    return s


def s3_get_file(bucket, key, file=None):

    if not file:
        file = tempfile.NamedTemporaryFile(delete=False)

    try:
        key = boto3.resource('s3').Object(bucket, key).get()
    except botocore.exceptions.ClientError as e:
        if e.response['ResponseMetadata']['HTTPStatusCode'] == 404:
            return False
        else:
            raise

    with file as f:
        chunk = key['Body'].read(1024*8)
        while chunk:
            f.write(chunk)
            chunk = key['Body'].read(1024*8)

    return f


first_cap_re = re.compile('(.)([A-Z][a-z]+)')
all_cap_re = re.compile('([a-z0-9])([A-Z])')

def convert_camel2snake(name):
    name = name.replace("BABIP", "BaBIP")
    s1 = first_cap_re.sub(r'\1_\2', name)
    return all_cap_re.sub(r'\1_\2', s1).lower()


def move_ssid(thing):

    if 'id' in thing:
        thing['ss_id'] = thing['id']

        del thing['id']

    return thing

