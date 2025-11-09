import discord
from discord.ext import commands
from funções import CRUD_inventario

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
            dados = CRUD_inventario.ver_inv(ctx.author.id)