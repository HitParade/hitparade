import os
import re
import json
import pprint
import datetime
import dateutil.parser
import requests
import tempfile
import subprocess
import boto3
import botocore

from stattlepy import Stattleship
from django.core.exceptions import ImproperlyConfigured


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

