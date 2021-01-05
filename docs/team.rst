Team
====
Team endpoints! So much data!

There are 5 class methods available, and one class attribute which will return all teams.

self.teams
----------
List out all teams available.

**Usage**

    .. code-block:: python

        from easy_nhl import Team

        all_teams = Team().teams

Team Info
---------
Get info of a given team id.

**Usage**

    .. code-block:: python

        from easy_nhl import Team

        sabres = Team(7)

        sabres_info = sabres.team_info()


Roster
------
Get the roster of a given team id.

**Usage**

    .. code-block:: python

        from easy_nhl import Team

        sabres = Team(7)
        sabres_roster = sabres.roster()

        # We can also get historical rosters by passing in a season
        sabres_roster_05 = sabres.roster('20052006')

Next Game
---------
Get a given team's next scheduled game.

**Usage**

    .. code-block:: python

        from easy_nhl import Team

        sabres = Team(7)

        sabres_next = sabres.next_game()

Previous Game
-------------
Get a given team's previous scheduled game.

**Usage**

    .. code-block:: python

        from easy_nhl import Team

        sabres = Team(7)

        sabres_prev = sabres.previous_game()

Season Stats
------------
Get a given teams current season stats.

**Usage**

    .. code-block:: python

        from easy_nhl import Team

        sabres = Team(7)
        sabres_stats = sabres.season_stats()

        # We can also get historical stats by passing in a season
        sabres_stats_05 = sabres.season_stats('20052006')