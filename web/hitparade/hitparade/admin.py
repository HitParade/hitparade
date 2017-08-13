from __future__ import division

from django.contrib import admin
from django.conf import settings

from hitparade.models import *


class GameStatPlayerFilter(admin.SimpleListFilter):

    title = 'Player'

    # Parameter for the filter that will be used in the URL query.
    parameter_name = 'player'

    def lookups(self, request, model_admin):

        retval = []
        distinct_players = GameStat.objects.values('player', 'player__name').distinct()

        for p in distinct_players:
            retval.append((p['player'], p['player__name']))

        return retval

    def queryset(self, request, queryset):

        if self.value() is None:
            return queryset
        else:
            return queryset.filter(player=self.value())


class GameStatusFilter(admin.SimpleListFilter):

    title = 'Status'

    # Parameter for the filter that will be used in the URL query.
    parameter_name = 'status'

    def lookups(self, request, model_admin):
        return (
            (Game.STATUS_UPCOMING, "Upcoming"),
            (Game.STATUS_IN_PROGRESS, "In Progress"),
            (Game.STATUS_CLOSED, "Finished"),
        )

    def queryset(self, request, queryset):

        if self.value() is None:
            return queryset
        else:
            return queryset.filter(status__exact=self.value())


class TeamFilter(admin.SimpleListFilter):

    title = 'Team'

    # Parameter for the filter that will be used in the URL query.
    parameter_name = 'team'

    # Model parameter to search on
    model_attribute = 'team'

    def lookups(self, request, model_admin):

        teams = Team.objects.all()
        return [(t.id, t.name) for t in teams]


    def queryset(self, request, queryset):

        if self.value() is None:
            return queryset
        else:
            kwargs = {self.model_attribute:self.value()}
            return queryset.filter(**kwargs)


class HomeTeamFilter(TeamFilter):
    title = 'Home Team'
    parameter_name = 'home_team'
    model_attribute = 'home_team'


class AwayTeamFilter(TeamFilter):
    title = 'Away Team'
    parameter_name = 'away_team'
    model_attribute = 'away_team'


class WinningTeamFilter(TeamFilter):
    title = 'Winning Team'
    parameter_name = 'winning_team'
    model_attribute = 'winning_team'


class TimeStampedAdmin(admin.ModelAdmin):
    readonly_fields = ('created','modified')

class PlayerAdmin(TimeStampedAdmin):
    list_display = ('name', 'team', 'position_name',)
    search_fields = ('name', 'first_name', 'last_name', 'nickname',)
    list_filter = (TeamFilter, 'active',)

class GameBattingLineupAdmin(admin.TabularInline):
    model = GameBattingLineup
    fields = ('team_nickname', 'order', 'player_name', 'position', 'handedness',)
    readonly_fields = ('team_nickname','player_name',)
    ordering = ('team', 'order',)

    def team_nickname(self, instance):
        return instance.team.nickname

    def player_name(self, instance):
        return instance.player.name


class GameAdmin(TimeStampedAdmin):
    list_display = ('title', 'started_at', 'status', )
    list_filter = (GameStatusFilter, AwayTeamFilter, HomeTeamFilter, WinningTeamFilter)
    ordering = ('started_at',)
    inlines = [GameBattingLineupAdmin]


class GameStatAdmin(TimeStampedAdmin):
    # status is required, but I don't know what for. - CH
    status = None
    list_per_page = 50
    list_display = ('__unicode__', 'player', 'car_game_num', 'game_date',)
    list_filter = (TeamFilter, GameStatPlayerFilter, )
    ordering = ('-game_date', 'team')

    # TODO: Set game filter once game is properly linked.


class AtBatAdmin(TimeStampedAdmin):
    status = None
    list_display = ('__unicode__', 'inning',)
    ordering = ('-game__started_at', '-inning',)


class PitchAdmin(TimeStampedAdmin):
    status = None
    list_display = ('__unicode__', 'inning',)
    ordering = ('-game__started_at', 'hitter__name', 'sequence',)


class VenueAdmin(TimeStampedAdmin):
    status = None
    list_display = ('__unicode__', 'abbreviation', 'name', 'city', 'state', 'field_type',)


class TeamAdmin(TimeStampedAdmin):
    list_display = ('__unicode__', 'name', 'location',)

class OfficialAdmin(TimeStampedAdmin):
    status = None
    list_display = ('__unicode__', 'first_name', 'last_name')

class OfficialAdmin(TimeStampedAdmin):
    status = None
    list_display = ('__unicode__', 'first_name', 'last_name')

class RotowireScrapeLineupLogAdmin(TimeStampedAdmin):
    status = None
    list_display = ('__unicode__', 'started_at', 'ended_at', 'was_rotowire_scraped', 'was_data_complete', 'error_text',)
    ordering = ('-started_at',)

class RotowireScrapeOfficialLogAdmin(TimeStampedAdmin):
    status = None
    list_display = ('__unicode__', 'started_at', 'ended_at', 'was_rotowire_scraped', 'was_data_complete', 'error_text',)
    ordering = ('-started_at',)

admin.site.register(Player, PlayerAdmin)
admin.site.register(Game, GameAdmin)
admin.site.register(GameStat, GameStatAdmin)
admin.site.register(AtBat, AtBatAdmin)
admin.site.register(Pitch, PitchAdmin)
admin.site.register(Venue, VenueAdmin)
admin.site.register(Team, TeamAdmin)
admin.site.register(Official, OfficialAdmin)
admin.site.register(RotowireScrapeLineupLog, RotowireScrapeLineupLogAdmin)
admin.site.register(RotowireScrapeOfficialLog, RotowireScrapeOfficialLogAdmin)
