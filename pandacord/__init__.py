import requests

class Token:
    def __init__(self, token: str):
        """
        Initialize the Token instance with a Discord token.
        """
        self.token = token
        self.base_url = "https://discord.com/api/v9"
        self.headers = {
            "Authorization": self.token,
            "Content-Type": "application/json"
        }

    def validate(self):
        """
        Validate the token by making a request to the Discord API.
        If vaild, it will `return [True, <username>, <discriminator>, <id>]` and save it to self.info
        If invald, will `return [False]`
        """
        url = f"{self.base_url}/users/@me"
        response = requests.get(url, headers=self.headers)

        if response.status_code == 200:
            self.info = [True, response.json().get('username'),response.json().get('discriminator') , response.json().get('id')]
            return [True, response.json().get('username'),response.json().get('discriminator') , response.json().get('id')]
        else:
            self.info = [False]
            return [False]
    def message(self, channel_id, content, proxies=None):
        """
        Sends message to a Discord channel via their API.
        Will `return [response.status_code, response.json()]`
        """
        url = f"{self.base_url}/channels/{channel_id}/messages"

        payload = {
            "content": content
        }
        if not proxies:
            response = requests.post(url, headers=self.headers, json=payload)
        if proxies:
            response = requests.post(url, headers=self.headers, json=payload, proxies=proxies)
        
        return [response.status_code, response.json()] 
    