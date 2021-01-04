Conference
==========
This class will give you access to the Conference endpoints of the NHL API.

There are only 2 methods available to this class.

All conferences
---------------
This will return a list of all conferences in the league.

**Usage**

    .. code-block:: python

        from easy_nhl import Conference

        all_conferences = Conference().all_conferences()

Details
-------
This will return information of a given conference id.

**Usage**

    .. code-block:: python

        from easy_nhl import Conference

        eastern = Conference().details(6)