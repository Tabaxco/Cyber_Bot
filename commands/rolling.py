import discord
from discord.ext import commands
from random import randint
from functions.roll import rolling

class Roll(commands.Cog):
    def _init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def roll(self, ctx, *,  input='1d20'):
        result = rolling(input)
        
        await ctx.send(result,
                       reference=ctx.message,
                       mention_author=True)