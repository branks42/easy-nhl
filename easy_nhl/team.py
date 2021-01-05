import requests

from .base_url import base_url


class Team:
    """
    Team endpoints of the NHL API.
    """
    
    def __init__(self, team_id=None):
        self.base_url = f"{base_url}/api/v1/teams/"
        self.teams = requests.get('https://statsapi.web.nhl.com/api/v1/teams/').json()['teams']
        self.team_id = team_id

    def team_info(self):
        """
        Get info of a given team id.
        """
        response = requests.get(f"{self.base_url}{self.team_id}")
        if response.status_code != 200:
            return {"error": f"Team with ID '{self.team_id}' not found."}

        return response.json()['teams'][0]

    def roster(self, season=None):
        """
        Get the roster of a given team
        """
        if season:
            response = requests.get(f"{self.base_url}{self.team_id}/roster?season={season}")
        else:
            response = requests.get(f"{self.base_url}{self.team_id}/roster")

        if response.status_code != 200:
            return {"error": f"Team with ID '{self.team_id}' not found."}

        return response.json()['roster']
    
    def next_game(self):
        """
        Get a given team's next scheduled game.
        """
        response = requests.get(f"{self.base_url}{self.team_id}?expand=team.schedule.next")
        if response.status_code != 200:
            return {"error": f"Team with ID '{self.team_id}' not found."}

        return response.json()['teams'][0]['nextGameSchedule']['dates'][0]['games'][0]
    
    def previous_game(self):
        """
        Get a given team's previous game.
        """
        response = requests.get(f"{self.base_url}{self.team_id}?expand=team.schedule.previous")
        if response.status_code != 200:
            return {"error": f"Team with ID '{self.team_id}' not found."}

        return response.json()['teams'][0]['previousGameSchedule']['dates'][0]['games'][0]
    
    def season_stats(self, season=None):
        """
        Get a given teams current season stats.
        """
        if season:
            response = requests.get(f"{self.base_url}{self.team_id}/stats?season={season}")
        else:
            response = requests.get(f"{self.base_url}{self.team_id}/stats")

        if response.status_code != 200:
            return {"error": f"Team with ID '{self.team_id}' not found."}

        return response.json()['stats']
    
