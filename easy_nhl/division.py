import requests

from .base_url import base_url


class Division:
    """
    Division endpoints of the NHL API.
    """

    def __init__(self):
        self.division_url = f"{base_url}/api/v1/divisions"

    def all_divisions(self):
        """
        Get all division information.
        """
        response = requests.get(self.division_url)
        return response.json()['divisions']

    def details(self, division_id):
        """
        Get details of a given division id.

        Args:
            division_id [int]: The division id
        """
        response = requests.get(f"{self.division_url}/{division_id}")

        if response.status_code != 200 or response.json()['divisions'] == []:
            return {"error": f"Division id {division_id} is not valid."}

        return response.json()['divisions'][0]
