import requests
from dotenv import load_dotenv
import os


load_dotenv()
class NotificationManager:
    def __init__(self, message: str):
        self.bot_token = os.getenv("BOT_TOKEN35")
        self.bot_chat_id = os.getenv("BOT_CHAT_35_ID")
        self.message = message
        self.bot_endpoint = 'https://api.telegram.org/bot'
    def send_text(self):
        send_text = self.bot_endpoint + self.bot_token + '/sendMessage?chat_id=' + self.bot_chat_id + '&parse_mode=Markdown&text=' + self.message
        bot_response = requests.get(send_text)
        bot_response.raise_for_status()

