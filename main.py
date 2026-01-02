import discord
from discord.ext import commands
from dotenv import load_dotenv
import os

load_dotenv()
TOKEN = os.getenv('TOKEN')

class CyberBot(commands.Bot):
    def __init__ (self):
        intents = discord.Intents.default()
        intents.message_content = True
        super().__init__(command_prefix='$', intents=intents)

    async def on_ready(self):
        print(f'{self.user} is online, babe!')

bot = CyberBot()
bot.run(TOKEN)