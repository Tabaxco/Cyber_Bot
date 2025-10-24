import discord
from discord.ext import commands
from dotenv import load_dotenv
import os

load_dotenv()
TOKEN = os.getenv("TOKEN")

class MeuBot(commands.Bot):
    def __init__ (self):
        intents = discord.Intents.default()
        intents.message_content = True
        super().__init__(command_prefix='$', intents=intents)

    async def setup_hook(self):
        # Carrega os módulos (cogs)
        from cogs.status import Status
        await self.add_cog(Status(self))

        from cogs.pericias import Pericias 
        await self.add_cog(Pericias(self))
        
    async def on_ready(self):
        print(f'Conectado com sucesso como {self.user}')
        

bot = MeuBot()
bot.run(TOKEN)