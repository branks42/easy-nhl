import requests

from .base_url import base_url


class Schedule:
    """
    Schedule endpoints of the NHL API
    """

    def __init__(self):
        self.base_url = f"{base_url}/api/v1/schedule"

    def today(self, team_id=None):
        """
        Get scheduled games for todays date.

        Args:
            team_id [int]: Team id to check for. Defaults to None.

        Returns:
            [dict]: The payload of the API call.
        """
        if team_id:
            response = requests.get(f"{self.base_url}?teamId={team_id}")
        else:
            response = requests.get(self.base_url)

        if response.json()['dates']:
            return response.json()['dates'][0]['games']
        else:
            return []

    def date(self, date_of_games=None, team_id=None):
        """
        Get scheduled games from a specified date.

        Args:
            date_of_games (str): The date to use. Format is 'YYYY-MM-DD'
            team_id [int]: The id number of the team to check.
        """
        if date_of_games and team_id:
            response = requests.get(f"{self.base_url}?date={date_of_games}&teamId={team_id}")
            if response.status_code != 200:
                return {}
            elif response.json()['dates']:
                return response.json()['dates'][0]['games'][0]
            else:
                return {}

        elif date_of_games and not team_id:
            response = requests.get(f"{self.base_url}?date={date_of_games}")
            if response.status_code != 200:
                return {}
            elif response.json()['dates']:
                return response.json()['dates'][0]['games']
            else:
                return []

        elif not date_of_games and team_id:
            return self.today(team_id)
        else:
            return self.today()

    def linescore(self, date_of_games=None, team_id=None):
        """
        Get more detailed scoring information for games of a given date.

        Args:
            date_of_games [str]: The date to use. Format is 'YYYY-MM-DD'
            team_id [int]: The id number of the team to check.
        """
        if date_of_games and team_id:
            response = requests.get(
                f"{self.base_url}?date={date_of_games}&expand=schedule.linescore&teamId={team_id}")
            if response.status_code != 200:
                return {}
            elif response.json()['dates']:
                return response.json()['dates'][0]['games'][0]
            else:
                return {}

        elif date_of_games and not team_id:
            response = requests.get(
                f"{self.base_url}?date={date_of_games}&expand=schedule.linescore")

        elif not date_of_games and team_id:
            response = requests.get(f"{self.base_url}?expand=schedule.linescore&teamId={team_id}")

        else:
            response = requests.get(f"{self.base_url}?expand=schedule.linescore")

        if response.status_code != 200:
            return {}
        elif response.json()['dates']:
            return response.json()['dates'][0]['games']
        else:
            return []

    def tickets(self, date_of_games=None, team_id=None):
        """
        Ticket information.

        Args:
            date_of_games [str]: The date to use. Format is 'YYYY-MM-DD'
            team_id [int]: The id number of the team to check.
        """
        if date_of_games and team_id:
            response = requests.get(
                f"{self.base_url}?date={date_of_games}&expand=schedule.ticket&teamId={team_id}")
            if response.status_code != 200:
                return {}
            elif response.json()['dates']:
                return response.json()['dates'][0]['games'][0]
            else:
                return {}

        elif date_of_games and not team_id:
            response = requests.get(
                f"{self.base_url}?date={date_of_games}&expand=schedule.ticket")

        elif not date_of_games and team_id:
            response = requests.get(f"{self.base_url}?expand=schedule.ticket&teamId={team_id}")

        else:
            response = requests.get(f"{self.base_url}?expand=schedule.ticket")

        if response.status_code != 200:
            return {}
        elif response.json()['dates']:
            return response.json()['dates'][0]['games']
        else:
            return []
