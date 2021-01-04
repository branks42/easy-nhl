Division
========
Much like Conference, this class will give you access to the Division endpoints of the NHL API.

There are only 2 methods available to this class.

All Divisions
-------------
This will return a list of all divisions in the league.

**Usage**

    ..code-block:: python

        from easy_nhl import Division

        all_divisions = Division().all_divisions()

Details
-------
This will return information of a given division id.

**Usage**

    .. code-block:: python

        from easy_nhl import Division

        atlantic = Division().details(17)