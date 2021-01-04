Installation
============

Requirements
------------
* Python 3. Yes, we have completely ignored Python 2. Sorry, not sorry.

Installing the package
----------------------
`pip install nhl-api-wrapper`

Examples
--------
That's it! To test, you can run python and try the following:

    .. code-block:: python

        from easy_nhl import Team

        print(Team().teams)

This will give you a payload of all current and former NHL teams (A list of dicts). You can then use the Team class to get
rosters and more information as follows:

    .. code-block:: python

        from easy_nhl import Team

        sabres = Team(7)

        print(sabres.roster())

I will go into more detail in the classes section of the documentation.