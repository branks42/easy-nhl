# [Easy NHL][docs]

[![pypi-version]][pypi]

Full documentation for the package is avalaible at https://easy-nhl.readthedocs.io/en/latest/

# Overview

Ever had a project idea that looks to take advantage of the NHL API, but you don't know where to start
because there's no documentation?

Look no further!

This api wrapper was developed to make grabbing and using that data a snap!

**Here's what you get:**

1. A few classes to make this simple
2. Built in methods on those classes, to make the data gathering a breeze

# Requirements

- Python (3.5, 3.6, 3.7, 3.8)

# Installation

`pip install easy-nhl`

# Example
```python
from easy_nhl import Team

print(Team().teams)
# This will give you a payload of all current and former NHL teams (A list of dicts). 
# You can then use the Team class to get rosters and more information as follows:
sabres = Team(7)
print(sabres.roster())

# You can get historical rosters as well by passing in a season.
# All of this is gone over in more detail in the documentation....
print(sabres.roster('20052006'))
```

[docs]: https://easy-nhl.readthedocs.io/en/latest/
[pypi-version]: https://img.shields.io/pypi/v/easy-nhl.svg
[pypi]: https://pypi.org/project/easy-nhl/