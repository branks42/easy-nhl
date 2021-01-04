Game
====
Game endpoints! Hizzah! *Note: You will need a game id to instantiate this class.*

There are 3 methods available to this class.

Boxscore
--------
This will get the boxscore date of a given game id.

**Usage**

    .. code-block:: python

        from easy_nhl import Schedule, Game

        schedule = Schedule()
        
        # Let's get a game id
        todays_game = schedule.today(7)
        game_pk = todays_game[0]['gamePk']

        # Here we can instantiate our Game class
        sabres_capitals = Game(game_pk)

        boxscore = sabres_capitals.boxscore()

Live Feed All Stats
-------------------
This will get the live feed data of a given game id.

**Usage**

    .. code-block:: python

        from easy_nhl import Schedule, Game

        schedule = Schedule()
        
        # Let's get a game id
        todays_game = schedule.today(7)
        game_pk = todays_game[0]['gamePk']

        # Here we can instantiate our Game class
        sabres_capitals = Game(game_pk)

        live_feed_stats = sabres_capitals.live_feed_all_stats()

Highlights and Media
--------------------
This will get the highlights and media snippets of a given game id.

**Usage**

    .. code-block:: python

        from easy_nhl import Schedule, Game

        schedule = Schedule()
        
        # Let's get a game id
        todays_game = schedule.today(7)
        game_pk = todays_game[0]['gamePk']

        # Here we can instantiate our Game class
        sabres_capitals = Game(game_pk)

        highlights = sabres_capitals.highlights_and_media()
