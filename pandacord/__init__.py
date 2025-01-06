import requests
import json

class Token:
    def __init__(self, token: str):
        """
        Initialize the Token instance with a Discord token.
        """
        self.token = token
        self.base_url = "https://discord.com/api/v9"
        self.headers = {
            "Authorization": self.token,
            "Content-Type": "application/json",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
            "Accept-Language": "en-US",
            "Accept": "*/*",
            "Connection": "keep-alive",
            "Pragma": "no-cache",
            "Cache-Control": "no-cache",
            "TE": "Trailers",
            "Host": "discord.com",
            "Origin": "https://discord.com",
            "Referer": "https://discord.com/channels/@me",
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-origin",
            "Sec-GPC": "1",
            "Accept-Encoding": "gzip, deflate, br",
            "DNT": "1",

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

class other():
    def test_wifi():
        """
        Test if the user is connected to the internet.
        """
        try:
            requests.get("https://www.google.com")
            return True
        except requests.ConnectionError:
            return False

class Webhook:
    def __init__(self, webhook_url: str):
        """
        Initialize the Webhook instance with a Discord webhook URL.
        """
        self.webhook_url = webhook_url
        self.headers = {
            "Content-Type": "application/json"
        }

    def send(self, content: str):
        """
        Sends a message to a Discord webhook.
        Will `return [response.status_code]`
        """
        payload = {
            "content": content
        }
        response = requests.post(self.webhook_url, headers=self.headers, json=payload)
        return [response.status_code]
    
    def send_embed(self, title: str, description: str, color: int):
        """
        Sends an embed to a Discord webhook.
        Will `return [response.status_code]`
        """
        payload = {
            "embeds": [
                {
                    "title": title,
                    "description": description,
                    "color": color
                }
            ]
        }
        response = requests.post(self.webhook_url, headers=self.headers, json=payload)
        return [response.status_code]

class Invite:
    def __init__(self, invite_code: str):
        """
        Initialize the Invite instance with a Discord invite code.
        """
        self.invite_code = invite_code
        self.base_url = "https://discord.com/api/v9"
        self.headers = {
            "Content-Type": "application/json"
        }

    def get_info(self):
        """
        Get information about a Discord invite.
        Will `return [response.status_code, response.json()]`
        """
        url = f"{self.base_url}/invites/{self.invite_code}"
        response = requests.get(url, headers=self.headers)
        self.info = [response.status_code, response.json()]
        return [response.status_code, response.json()]
