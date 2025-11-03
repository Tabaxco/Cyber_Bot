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
        
        from cogs.status import Status
        await self.add_cog(Status(self))

        from cogs.pericias import Pericias 
        await self.add_cog(Pericias(self))
        
        from cogs.rolagem import Rolagem
        await self.add_cog(Rolagem(self))

        from cogs.gerais import Gerais
        await self.add_cog(Gerais(self))
        
    async def on_ready(self):
        print(f'Conectado com sucesso como {self.user}')
        mensagens = cycle(["Ensinando a Agatha", "Entrando no Shadowverse",
                           "Estourando os balões do Chico"])
        while True:
            await bot.change_presence(activity=discord.Game(next(mensagens)))
            await asyncio.sleep(20)

bot = MeuBot()
bot.run(TOKEN)