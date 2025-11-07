import discord
from discord.ext import commands

class Inventario(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

        @commands.command()
        async def update_inv(self, ctx):
            ...
        
        @commands.command()
        async def del_inv(self, ctx):
            ...
        
        @commands.command()
        async def inv(self, ctx):
            ...