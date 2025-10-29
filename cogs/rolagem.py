import discord
from discord.ext import commands
import random


class Rolagem(commands.cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def roll(self, ctx, *, entrada: str):
        ...