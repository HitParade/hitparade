from __future__ import absolute_import, unicode_literals
from celery import shared_task

import pprint
import datetime
from hitparade.models import *
from hitparade.utils import get_stattleship_client, move_ssid

@shared_task
def debug_task(x, y):
    print "debug_task"
    print x
    print 7
    return x + y


@shared_task
def load_at_bats(game_id):

    print "Received %i" % game_id

    pp = pprint.PrettyPrinter(indent=2)
    year = datetime.datetime.now().year
    s = get_stattleship_client()
    game = Game.objects.get(pk=game_id)

    page = 1
    len_atbats = -1

    while len_atbats != 0:

        print "%s : %i" % (str(game.id), int(page))


        result = s.ss_get_results(sport='baseball',
                                league='mlb',
                                ep='at_bats',
                                game_id=game.slug,
                                page=page,
                                per_page=40,
                                verbose=False
                            )

        # print result[0].keys()
        # pp.pprint(result[0]['at_bats'][0])
        # pp.pprint(result[0]['baseball_pitches'][0])
        # return


        len_atbats = len(result[0]['at_bats'])
        page = page + 1

        print "len_atbats" + str(len_atbats)

        if len_atbats == 0:
            continue


        # Load Officials
        for o in result[0]['officials']:
            Official.create_from_ss(o)


        # Load Venues
        for v in result[0]['venues']:
            Venue.create_from_ss(v)


        # Load Games
        for g in result[0]['games']:
            g[u'season'] = year
            Game.create_from_ss(g)


        # Load Players
        for p in result[0]['hitters']:
            Player.create_from_ss(p)


        for p in result[0]['pitchers']:
            Player.create_from_ss(p)


        # Load pitches
        for p in result[0]['baseball_pitches']:
            p['game'] = game
            Pitch.create_from_ss(p)


        # Load at Bats
        for ab in result[0]['at_bats']:
            ab['game'] = game
            AtBat.create_from_ss(ab)

    game.at_bats_loaded = True
    game.save()



