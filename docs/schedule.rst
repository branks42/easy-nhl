Schedule
========
Starting to dig into the good stuff now! Schedule endpoint access!

There are 4 methods available to this class.

Today
-----
This will return the NHL schedule for todays date.

**Usage**

    .. code-block:: python

        from easy_nhl import Schedule

        schedule = Schedule()
        todays_schedule = schedule.today()

        # You can also get today's schedule for a particular team by passing in their team id
        sabres_sched_today = schedule.today(7)

Date 
----
This will return the NHL schedule for a given date. (Note: date must be passed in in 'YYYY-MM-DD' format)

**Usage**

    .. code-block:: python

        from easy_nhl import Schedule

        schedule = Schedule()

        first_day_of_season = schedule.date('2021-01-13')

        # You can also get an individual teams schedule for a given date by passing in their team id.
        sabres_sens_wild_game_1 = schedule.date('2006-05-05', 7)


Linescore
---------
This will fetch more detailed scoring information for games on a given date. (Defaults to today)

**Usage**

    .. code-block:: python

        from easy_nhl import Schedule

        schedule = Schedule()

        more_stats = schedule.linescore() # Defaults to today

        # You can also get an individual teams linescore for a given date
        sabres_sens_wild_game_1_more_data = schedule.linescore('2006-05-05', 7)

Tickets
-------
This will fetch ticket information for games on a given date. (Defaults to today)

**Usage**

    .. code-block:: python

        from easy_nhl import Schedule

        schedule = Schedule()

        ticket_info = Schedule.tickets()

        # You can specify dates and team as well

        sabres_tickets = schedule.tickets('2021-10-05', 7)

