Player
======
This is the motherload. All player stats and information available from the NHL API.
*Note: You need a player id to instantiate this class*

This class has 13 methods.

Player Info
-----------
Get player information.

**Usage**

    .. code-block:: python

        from easy_nhl import Team, Player

        # We can use the team roster to get a player id.
        for player in Team(7).roster():
            if player['person']['fullName'] == 'Jack Eichel':
                eichel_id = player['person']['id']
        
        # Now we can get Jack's info
        eichel = Player(eichel_id)
        eichel_info = eichel.player_info()

Season Stats
------------
Get a player's stats from the provided season.

You can provide a season to search for this method, but it must be passed as '20192020' for any given season.

**Usage**

    .. code-block:: python

        from easy_nhl import Team, Player

        # We can use the team roster to get a player id.
        for player in Team(7).roster():
            if player['person']['fullName'] == 'Jack Eichel':
                eichel_id = player['person']['id']
        
        # Now we can get Jack's season stats
        eichel = Player(eichel_id)
        eichel_current_season = eichel.season_stats()

        # Or we can check previous season_stats
        eichel_rookie_stats = eichel.season_stats('20152016')

Goals By Game Situation
-----------------------
Get goals of a given player with details of the game situation in which they were scored.

You can provide a season to search for this method, but it must be passed as '20192020' for any given season.

**Usage**

    .. code-block:: python

        from easy_nhl import Team, Player

        # We can use the team roster to get a player id.
        for player in Team(7).roster():
            if player['person']['fullName'] == 'Jack Eichel':
                eichel_id = player['person']['id']
        
        # Now we can get Jack's goals by game situation
        eichel = Player(eichel_id)
        eichel_current_gbgs = eichel.goals_by_game_situation()

        # Or we can check previous season gbgs
        eichel_rookie_gbgs = eichel.goals_by_game_situation('20152016')

Win Loss Record
---------------
Get a goalies win loss record for a current season

You can provide a season to search for this method, but it must be passed as '20192020' for any given season.

**Usage**

    .. code-block:: python

        from easy_nhl import Team, Player

        # We can use the team roster to get a player id.
        for player in Team(7).roster():
            if player['person']['fullName'] == 'Linus Ullmark':
                ullmark_id = player['person']['id']
        
        # Now we can get Ullmark's win/loss record
        ullmark = Player(ullmark_id)
        ullmark_win_loss = ullmark.win_loss_record()

        # Or we can check previous season gbgs
        ullmark_win_loss_last = ullmark.win_loss_record('20192020')

Home Away Stats
---------------
Get a players stats broken up by home and away games.

You can provide a season to search for this method, but it must be passed as '20192020' for any given season.

**Usage**

    .. code-block:: python

        from easy_nhl import Team, Player

        # We can use the team roster to get a player id.
        for player in Team(7).roster():
            if player['person']['fullName'] == 'Jack Eichel':
                eichel_id = player['person']['id']
        
        # Now we can get Jack's stats by home away
        eichel = Player(eichel_id)
        eichel_current_has = eichel.home_away_stats()

        # Or we can check previous season home away
        eichel_rookie_has = eichel.home_away_stats('20152016')

Stats Split By Month
--------------------
Get a players stats broken up by month.

You can provide a season to search for this method, but it must be passed as '20192020' for any given season.

**Usage**

    .. code-block:: python

        from easy_nhl import Team, Player

        # We can use the team roster to get a player id.
        for player in Team(7).roster():
            if player['person']['fullName'] == 'Jack Eichel':
                eichel_id = player['person']['id']
        
        # Now we can get Jack's stats split by month
        eichel = Player(eichel_id)
        eichel_current_month_split = eichel.stats_split_by_month()

        # Or we can check previous season split by month
        eichel_rookie_month_split = eichel.stats_split_by_month('20152016')

Stats Split By Day of Week
--------------------------
Get a players stats broken up by day of week.

You can provide a season to search for this method, but it must be passed as '20192020' for any given season.

**Usage**

    .. code-block:: python

        from easy_nhl import Team, Player

        # We can use the team roster to get a player id.
        for player in Team(7).roster():
            if player['person']['fullName'] == 'Jack Eichel':
                eichel_id = player['person']['id']
        
        # Now we can get Jack's stats split by day of week
        eichel = Player(eichel_id)
        eichel_current_dow_split = eichel.stats_split_by_day_of_week()

        # Or we can check previous season split by day of week
        eichel_rookie_daw_split = eichel.stats_split_by_day_of_week('20152016')

Stats Split By Division
-----------------------
Get a players stats broken up by Division.

You can provide a season to search for this method, but it must be passed as '20192020' for any given season.

**Usage**

    .. code-block:: python

        from easy_nhl import Team, Player

        # We can use the team roster to get a player id.
        for player in Team(7).roster():
            if player['person']['fullName'] == 'Jack Eichel':
                eichel_id = player['person']['id']
        
        # Now we can get Jack's stats split by division
        eichel = Player(eichel_id)
        eichel_current_division_split = eichel.stats_split_by_division()

        # Or we can check previous season split by division
        eichel_rookie_division_split = eichel.stats_split_by_division('20152016')

Stats Split By Conference
-------------------------
Get a players stats broken up by Conference.

You can provide a season to search for this method, but it must be passed as '20192020' for any given season.

**Usage**

    .. code-block:: python

        from easy_nhl import Team, Player

        # We can use the team roster to get a player id.
        for player in Team(7).roster():
            if player['person']['fullName'] == 'Jack Eichel':
                eichel_id = player['person']['id']
        
        # Now we can get Jack's stats split by conference
        eichel = Player(eichel_id)
        eichel_current_conference_split = eichel.stats_split_by_conference()

        # Or we can check previous season split by conference
        eichel_rookie_conference_split = eichel.stats_split_by_conference('20152016')

Stats Split By Team
-------------------
Get a players stats broken up by Team.

You can provide a season to search for this method, but it must be passed as '20192020' for any given season.

**Usage**

    .. code-block:: python

        from easy_nhl import Team, Player

        # We can use the team roster to get a player id.
        for player in Team(7).roster():
            if player['person']['fullName'] == 'Jack Eichel':
                eichel_id = player['person']['id']
        
        # Now we can get Jack's stats split by team
        eichel = Player(eichel_id)
        eichel_current_team_split = eichel.stats_split_by_team()

        # Or we can check previous season split by team
        eichel_rookie_team_split = eichel.stats_split_by_team('20152016')

Stats Split By Game
-------------------
Get a players stats broken up by Game.

You can provide a season to search for this method, but it must be passed as '20192020' for any given season.

**Usage**

    .. code-block:: python

        from easy_nhl import Team, Player

        # We can use the team roster to get a player id.
        for player in Team(7).roster():
            if player['person']['fullName'] == 'Jack Eichel':
                eichel_id = player['person']['id']
        
        # Now we can get Jack's stats split by game
        eichel = Player(eichel_id)
        eichel_current_game_split = eichel.stats_split_by_game()

        # Or we can check previous season split by game
        eichel_rookie_game_split = eichel.stats_split_by_game('20152016')

Stats Standings
---------------
Get a players stats standings.

You can provide a season to search for this method, but it must be passed as '20192020' for any given season.

**Usage**

    .. code-block:: python

        from easy_nhl import Team, Player

        # We can use the team roster to get a player id.
        for player in Team(7).roster():
            if player['person']['fullName'] == 'Jack Eichel':
                eichel_id = player['person']['id']
        
        # Now we can get Jack's stats standings
        eichel = Player(eichel_id)
        eichel_current_standings = eichel.stats_standings()

        # Or we can check previous season stats standings
        eichel_rookie_standings = eichel.stats_standings('20152016')

Stats on Pace For
-----------------
Get a players projected stats. Only works for current season.

**Usage**

    .. code-block:: python

        from easy_nhl import Team, Player

        # We can use the team roster to get a player id.
        for player in Team(7).roster():
            if player['person']['fullName'] == 'Jack Eichel':
                eichel_id = player['person']['id']
        
        # Now we can get Jack's pace
        eichel = Player(eichel_id)
        eichel_pace = eichel.stats_on_pace_for()