import os
from dotenv import load_dotenv


class Setting:
    def __init__(self):
        load_dotenv()
        self.bot_token = os.getenv('BOT_TOKEN')
        self.start_date = '11.08.2024'


config = Setting()
