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
# Ensure you have run 'pip install redis'
import redis
import pickle
import requests
PLAYER_PROFILES = {}
def get_redis():
    try:
        conn = redis.StrictRedis(
            host='421575f247164452bade14068817853a.publb.rackspaceclouddb.com',
            port=6379,
            password='KsFKmtmnRAYgk6B6kNzWk93P7kKYqRFBZmzE')
        print conn
        conn.ping()
        print 'Connected!'
        return conn
    except Exception as ex:
        print 'Error:', ex
        exit('Failed to connect, terminating.')

def get_key_or_null( obj, key ):
    if key is None:
        return '';
    if obj is None:
        return '';
    try:
        return obj[key]
    except:
        # print( 'Key ' + str(key) + ' is not found in object ' + str(type(obj)) )
        # if not obj is None and type(obj) == type({}):
        #     print('keys are  ' + str(obj.keys()))
        return None
def set_redis_object(redis_, key, obj):
    if not key is None:
        if not obj is None:
            if not redis_ is None:
                print(' setting redis ' + key)
                redis_.set(key , pickle.dumps(obj))
def get_redis_object(redis_, key):
    if redis_ is None:
        redis_ = get_redis()
    try:
        return pickle.loads( redis_.get(key) )
    except:
        print(" Could not find " + str(key) + " in redis...")
        return None

def get_team_profile(conn_redis, id):
    key_='sr.team_profile.'+id
    team_profile = get_redis_object(conn_redis, key_)
    if team_profile is None:
        try:
            tp = requests.get(
                'http://api.sportradar.us/mlb-p6/teams/' + id + '/profile.json?api_key=retmw8bx9vxzw5ks5t2supz5')
            obj = tp.json()
            if not obj is None:
                set_redis_object(conn_redis, key_, obj)
            return obj
        except:
            print("Team Profile - unable to pull it")

def get_teams():
    conn_redis = get_redis()
    teams = []
    teams_name = {}
    try:
        json_obj = get_redis_object(conn_redis, '2017.rankings')
        if json_obj is None:
            tr = requests.get('http://api.sportradar.us/mlb-p6/seasontd/2017/REG/rankings.json?api_key=retmw8bx9vxzw5ks5t2supz5')
            json_obj = tr.json()
            set_redis_object(conn_redis, '2017.rankings',json_obj)
            for league in json_obj['league']['season']['leagues']:
                for division in league['divisions']:
                    print('d')
                    for team in division['teams']:
                        team_profile = get_team_profile(conn_redis,team['id'])
                        teams.append({
                            'team' : team,
                            'team_profile': team_profile
                        })
                        print('append')
            set_redis_object(conn_redis, '2017.rankings', teams)
        else:
            teams = json_obj
        if not teams is None:
            print('teams is not none')
            for t in teams:
                teams_name[t['team_profile']['name']] = t
                teams_name[t['team_profile']['name'].lower()] = t
        return teams, teams_name
    except:
        print("Exception getting teams")

def get_venues():
    redis_conn = get_redis()
    venues = get_redis_object(redis_conn, 'venues')
    name_dict = {}
    city_dict = {}
    if venues is None:
        venues = []
        try:
            r = requests.get('http://api.sportradar.us/mlb-p6/league/venues.json?api_key=retmw8bx9vxzw5ks5t2supz5')
            json_object = r.json()
            for venue in json_object['venues']:
                if not venue is None and not get_key_or_null( venue, 'city' ) is None:
                    new_venue = {}
                    new_venue['sr_id'] =  get_key_or_null( venue, 'id' )
                    new_venue['name'] =   get_key_or_null( venue, 'name' )
                    new_venue['market'] = get_key_or_null( venue, 'market' )
                    new_venue['capacity'] = get_key_or_null( venue, 'capacity' )
                    new_venue['surface'] = get_key_or_null( venue, 'surface' )
                    new_venue['address'] = get_key_or_null( venue, 'address' )
                    new_venue['city'] = get_key_or_null( venue, 'city' )
                    new_venue['state'] = get_key_or_null( venue, 'state' )
                    new_venue['zip'] = get_key_or_null( venue, 'zip' )
                    new_venue['country'] = get_key_or_null( venue, 'country' )
                    new_venue['distances_lf'] = get_key_or_null( venue['distances'], 'lf' )
                    new_venue['distances_lcf'] = get_key_or_null( venue['distances'], 'lcf' )
                    new_venue['distances_cf'] = get_key_or_null( venue['distances'], 'cf' )
                    new_venue['distances_rcf'] = get_key_or_null( venue['distances'], 'rcf' )
                    new_venue['distances_rf'] = get_key_or_null( venue['distances'], 'rf' )
                    new_venue['distances_mlf'] = get_key_or_null( venue['distances'], 'mlf' )
                    new_venue['distances_mlcf'] = get_key_or_null( venue['distances'], 'mlcf' )
                    new_venue['distances_mrcf'] = get_key_or_null( venue['distances'], 'mrcf' )
                    new_venue['distances_mrf'] = get_key_or_null( venue['distances'], 'mrf' )
                    if new_venue['city'] is None:
                        print("no city is found")
                    else:
                        print('city ==>' + new_venue['city'])
                    city_dict[new_venue['city']] = new_venue
                    city_dict[new_venue['city'].lower()] = new_venue
                    name_dict[new_venue['name']] = new_venue
                    name_dict[new_venue['name'].lower()] = new_venue
                    venues.append(new_venue)
        except:
            print("Exception making request")
    set_redis_object(redis_conn, 'venues.city', city_dict)
    set_redis_object(redis_conn, 'venues.name', name_dict)
    set_redis_object(redis_conn, 'venues', venues)
    return venues, city_dict, name_dict


def format_number(n):
    if n is None:
        return '00'
    else:
        if n < 10:
            return str('0') + str(n)
        else:
            return str(n)


def get_player_profile(conn_redis,player_id):
    player_profile = get_key_or_null(PLAYER_PROFILES,player_id)
    if player_profile is None:
        r = requests.get( 'http://api.sportradar.us/mlb-p6/players/' + player_id + '/profile.json?api_key=retmw8bx9vxzw5ks5t2supz5')
        player_profile = r.json()
        PLAYER_PROFILES[player_id] = player_profile
    return player_profile


def get_game_summary(conn_redis, y_,m_,d_):
    r = requests.get('http://api.sportradar.us/mlb-p6/games/'+str(y_)+'/'+format_number(m_)+'/'+format_number(d_)+'/summary.json?api_key=retmw8bx9vxzw5ks5t2supz5')
    json_object = r.json()
    all_games = []
    for g in json_object['league']['games']:
        game_details = {}
        game = g['game']
        game_details['sr_id'] = game['id']
        game_details['venue_market'] = game['venue']['market']
        game_details['venue_capacity'] = game['venue']['capacity']
        game_details['venue_name'] = game['venue']['name']
        game_details['venue_sr_id'] = game['venue']['id']
        game_details['home_team_name'] = game['home']['name']
        game_details['home_team_market'] = game['home']['market']
        game_details['home_team_abbr'] = game['home']['abbr']
        game_details['away_team_name'] = game['away']['name']
        game_details['away_team_market'] = game['away']['market']
        game_details['away_team_abbr'] = game['away']['abbr']
        game_details['innings'] = game['final']['inning']
        game_details['inning_end'] = game['final']['inning_half']
        game_details['home_team_runs'] = game['home']['runs']
        game_details['home_team_hits'] = game['home']['hits']
        game_details['home_team_errors'] = game['home']['errors']
        game_details['away_team_runs'] = game['away']['runs']
        game_details['away_team_hits'] = game['away']['hits']
        game_details['away_team_errors'] = game['away']['errors']
        game_details['away_team_wins'] = game['away']['win']
        game_details['away_team_losses'] = game['away']['loss']
        game_details['home_team_wins'] = game['home']['win']
        game_details['home_team_losses'] = game['home']['loss']
        game_details['home_team_sr_id'] = game['home']['id']
        game_details['away_team_sr_id'] = game['away']['id']
        game_details['attendance'] = game['attendance']
        game_details['duration_mins'] = (60 * int(game['duration'].split(':')[0])) + int(game['duration'].split(':')[1])
        game_details['duration'] = game['duration']
        game_details['day_night'] = game['day_night']
        game_details['scheduled'] = game['scheduled']
        lineup_home = game['home']['lineup']
        lineup_away = game['away']['lineup']
        home_lineup = {}
        away_lineup = {}
        for lh in lineup_home:
            if lh['inning'] == 0:
                home_lineup[lh['order']] = lh
        for ah in lineup_away:
            if ah['inning'] == 0:
                away_lineup[ah['order']] = ah
        game_details['lineup_home'] = home_lineup
        game_details['lineup_away'] = away_lineup
        for p in  game_details['lineup_away']:
            player_profile = get_player_profile(conn_redis, game_details['lineup_away'][p]['id'])
            game_details['lineup_away'][p]['profile'] = player_profile
        for p in  game_details['lineup_home']:
            player_profile = get_player_profile(conn_redis, game_details['lineup_away'][p]['id'])
            game_details['lineup_away'][p]['profile'] = player_profile
        all_games.append(game_details)
    return all_games


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

