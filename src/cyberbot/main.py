import discord
from discord.ext import commands
from dotenv import load_dotenv
import os
from itertools import cycle
import asyncio

load_dotenv()
TOKEN = os.getenv("TOKEN")


class MeuBot(commands.Bot):
    def __init__ (self):
        intents = discord.Intents.default()
        intents.message_content = True
        super().__init__(command_prefix='$', intents=intents)


    async def setup_hook(self):
      ...

    async def on_ready(self):
       print(f"{self.user} conectada.")

bot = MeuBot()
bot.run(TOKEN)