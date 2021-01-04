import requests

from .base_url import base_url


class Game:
    """
    Game endpoints of the NHL API.
    """

    def __init__(self, game_id):
        self.game_url = f"{base_url}/api/v1/game"
        self.game_id = game_id

    def boxscore(self):
        """
        Get the boxscore data of a given game id.
        """
        response = requests.get(f"{self.game_url}/{self.game_id}/boxscore")

        if response.status_code != 200:
            return {"error": f"Game with id '{self.game_id}' not found."}

        return ({
            "teams": response.json()['teams'],
            "officials": response.json()['officials']})
    
    def live_feed_all_stats(self):
        """
        Get the live feed data of a given game id.
        """
        response = requests.get(f"{self.game_url}/{self.game_id}/feed/live")

        if response.status_code != 200:
            return {"error": f"Game with id '{self.game_id}' not found."}

        return ({
            "gamePk": response.json()['gamePk'],
            "gameData": response.json()['gameData'],
            "liveData": response.json()['liveData']})

    def highlights_and_media(self):
        """
        Get the highlights and media snippets of a given game id.
        """
        response = requests.get(f"{self.game_url}/{self.game_id}/content")

        if response.status_code != 200:
            return {"error": f"Game with id '{self.game_id}' not found."}

        return ({
            "editorial": response.json()['editorial'],
            "media": response.json()['media'],
            "highlights": response.json()['highlights']})