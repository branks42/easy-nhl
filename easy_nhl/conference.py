import requests

from .base_url import base_url


class Conference:
    """
    Conference endpoints of the NHL API.
    """

    def __init__(self):
        self.conference_url = f"{base_url}/api/v1/conferences"
    
    def all_conferences(self):
        """
        Get all conference information.
        """
        response = requests.get(self.conference_url)
        return response.json()['conferences']
    
    def details(self, conference_id):
        """
        Get details of a given conference id.

        Args:
            conference_id [int]: The conference id
        """
        response = requests.get(f"{self.conference_url}/{conference_id}")

        if response.status_code != 200:
            return {"error": f"Conference id {conference_id} is not valid."}

        return response.json()['conferences'][0]