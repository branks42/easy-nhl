import requests

from .base_url import base_url


class Player():
    """
    Player endpoints of the NHL API.
    """

    def __init__(self, player_id):
        self.player_id = player_id
        self.player_url = f"{base_url}/api/v1/people"
    
    def player_info(self):
        """
        Get player information.
        """
        response = requests.get(f"{self.player_url}/{self.player_id}")
        if response.status_code != 200:
            return {"error": f"Player with ID '{self.player_id}' not found."}
        if "fullName" not in response.json()['people'][0]:
            return {"error": f"Player with ID '{self.player_id}' not found."}
        
        return response.json()['people'][0]
    
    def season_stats(self, season=None):
        """
        Get a player's stats from the provided season

        Args:
            season (str, optional): Defaults to current season, must be 2 consecutive years with no spaces.
        """
        if season:
            response = requests.get(f"{self.player_url}/{self.player_id}/stats?stats=statsSingleSeason&season={season}")
        else:
            response = requests.get(f"{self.player_url}/{self.player_id}/stats?stats=statsSingleSeason")
        
        if response.status_code != 200:
            return {"error": f"Player with ID '{self.player_id}' not found."}

        return response.json()['stats'][0]['splits']
    

    def goals_by_game_situation(self, season=None):
        """
        Get goals of a given player with details of the game situation in which they were scored.

        Args:
            season [str]: Defaults to current season, must be 2 consecutive years with no spaces.
        """
        if season:
            response = requests.get(f"{self.player_url}/{self.player_id}/stats?stats=goalsByGameSituation&season={season}")
        else:
            response = requests.get(f"{self.player_url}/{self.player_id}/stats?stats=goalsByGameSituation")

        if response.status_code != 200:
            return {"error": f"Player with ID '{self.player_id}' not found."}

        return response.json()['stats'][0]['splits']
    
    def win_loss_record(self, season=None):
        """
        Get a goalies win loss record for a current season

        Args:
            season [str]: Defaults to current season, must be 2 consecutive years with no spaces.
        """
        if season:
            response = requests.get(f"{self.player_url}/{self.player_id}/stats?stats=winLoss&season={season}")
        else:
            response = requests.get(f"{self.player_url}/{self.player_id}/stats?stats=winLoss")

        if response.status_code != 200:
            return {"error": f"Player with ID '{self.player_id}' not found."}

        return response.json()['stats'][0]['splits']
    
    def home_away_stats(self, season=None):
        """
        Get a players stats broken up by home and away games.

        Args:
            season [str]: Defaults to current season, must be 2 consecutive years with no spaces.
        """
        if season:
            response = requests.get(f"{self.player_url}/{self.player_id}/stats?stats=homeAndAway&season={season}")
        else:
            response = requests.get(f"{self.player_url}/{self.player_id}/stats?stats=homeAndAway")

        if response.status_code != 200:
            return {"error": f"Player with ID '{self.player_id}' not found."}

        return response.json()['stats'][0]['splits']
    
    def stats_split_by_month(self, season=None):
        """
        Get a players stats broken up by month.

        Args:
            season [str]: Defaults to current season, must be 2 consecutive years with no spaces.
        """
        if season:
            response = requests.get(f"{self.player_url}/{self.player_id}/stats?stats=byMonth&season={season}")
        else:
            response = requests.get(f"{self.player_url}/{self.player_id}/stats?stats=byMonth")
        
        if response.status_code != 200:
            return {"error": f"Player with ID '{self.player_id}' not found."}

        return response.json()['stats'][0]['splits']
    
    def stats_split_by_day_of_week(self, season=None):
        """
        Get a players stats broken up by day of the week.

        Args:
            season [str]: Defaults to current season, must be 2 consecutive years with no spaces.
        """
        if season:
            response = requests.get(f"{self.player_url}/{self.player_id}/stats?stats=byDayOfWeek&season={season}")
        else:
            response = requests.get(f"{self.player_url}/{self.player_id}/stats?stats=byDayOfWeek")

        if response.status_code != 200:
            return {"error": f"Player with ID '{self.player_id}' not found."}

        return response.json()['stats'][0]['splits']
    
    def stats_split_by_division(self, season=None):
        """
        Get a players stats broken up by division.

        Args:
            season [str]: Defaults to current season, must be 2 consecutive years with no spaces.
        """
        if season:
            response = requests.get(f"{self.player_url}/{self.player_id}/stats?stats=vsDivision&season={season}")
        else:
            response = requests.get(f"{self.player_url}/{self.player_id}/stats?stats=vsDivision")

        if response.status_code != 200:
            return {"error": f"Player with ID '{self.player_id}' not found."}

        return response.json()['stats'][0]['splits']
    
    def stats_split_by_conference(self, season=None):
        """
        Get a players stats broken up by conference.

        Args:
            season [str]: Defaults to current season, must be 2 consecutive years with no spaces.
        """
        if season:
            response = requests.get(f"{self.player_url}/{self.player_id}/stats?stats=vsConference&season={season}")
        else:
            response = requests.get(f"{self.player_url}/{self.player_id}/stats?stats=vsConference")

        if response.status_code != 200:
            return {"error": f"Player with ID '{self.player_id}' not found."}

        return response.json()['stats'][0]['splits']
    
    def stats_split_by_team(self, season=None):
        """
        Get a players stats broken up by team.

        Args:
            season [str]: Defaults to current season, must be 2 consecutive years with no spaces.
        """
        if season:
            response = requests.get(f"{self.player_url}/{self.player_id}/stats?stats=vsTeam&season={season}")
        else:
            response = requests.get(f"{self.player_url}/{self.player_id}/stats?stats=vsTeam")

        if response.status_code != 200:
            return {"error": f"Player with ID '{self.player_id}' not found."}

        return response.json()['stats'][0]['splits']
    
    def stats_split_by_game(self, season=None):
        """
        Get a players stats broken up by game.

        Args:
            season [str]: Defaults to current season, must be 2 consecutive years with no spaces.
        """
        if season:
            response = requests.get(f"{self.player_url}/{self.player_id}/stats?stats=gameLog&season={season}")
        else:
            response = requests.get(f"{self.player_url}/{self.player_id}/stats?stats=gameLog")

        if response.status_code != 200:
            return {"error": f"Player with ID '{self.player_id}' not found."}

        return response.json()['stats'][0]['splits']
    
    def stats_standings(self, season=None):
        """
        Get a players stats standings.

        Args:
            season [str]: Defaults to current season, must be 2 consecutive years with no spaces.
        """
        if season:
            response = requests.get(f"{self.player_url}/{self.player_id}/stats?stats=regularSeasonStatRankings&season={season}")
        else:
            response = requests.get(f"{self.player_url}/{self.player_id}/stats?stats=regularSeasonStatRankings")

        if response.status_code != 200:
            return {"error": f"Player with ID '{self.player_id}' not found."}

        return response.json()['stats'][0]['splits']

    def stats_on_pace_for(self):
        """
        Get a players projected stats.

        Args:
            season [str]: Defaults to current season, must be 2 consecutive years with no spaces.
        """
        response = requests.get(f"{self.player_url}/{self.player_id}/stats?stats=onPaceRegularSeason")
        if response.status_code != 200:
            return {"error": f"Player with ID '{self.player_id}' not found."}
        
        return response.json()['stats'][0]['splits']
