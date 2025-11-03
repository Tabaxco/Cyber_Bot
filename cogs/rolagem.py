import discord
from discord.ext import commands
import random


class Rolagem(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

   
    @commands.command()
    async def roll(self, ctx, *, entrada: str = "1d20"):
        partes = entrada.lower().split("d")
        
        qtde = int(partes[0]) if partes[0] else 1
        faces = int(partes[1])

        resultado = [random.randint(1, faces) for i in range(qtde)]
        total = sum(resultado)
        
        await ctx.send(f"` {total} ` ⟵ {resultado} {qtde}d{faces}",
                       reference=ctx.message,
                       mention_author=True)
        