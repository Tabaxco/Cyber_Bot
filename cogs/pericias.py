import discord
from discord.ext import commands
from funções import CRUD_pericias
import asyncio

class Pericias(commands.Cog):
    def __init__ (self, bot):
        self.bot = bot

    @commands.command()
    async def criar_pericias(self, ctx):
        discord_id = ctx.author.id

        def check(m):
            return (
                    m.author == ctx.author and 
                    m.channel == ctx.channel and 
                    m.content.lower() in ["sim", "não"]
                    )

        pericias = {
            "Força" : [
                "Atletismo", "Taijutsu", "Pontaria"
            ],
            "Destreza" : [
                "Acrobacia", "Furtividade", "Pontaria"
            ],
            "Constituição" : [
                "Fortitude"
            ],
            "Sabedoria" : [
                "Intuição", "Medicina", "Perceção", "Ocultismo", "Sobrevivência", "Vontade"
            ],
            "Inteligência" : [
                "Astúcia", "Ninjutsu", "Investigação", "História"
            ],
            "Carsima": [
                "Persuasão", "Enganação", "Intimidação", "Genjutsu"
            ]
        }

        escolhas = []

        for atributo, lista_pericia in pericias.items():
            await ctx.send(f'Perícias de {atributo}:')
            for pericia in lista_pericia:
                await ctx.send(f'Você possui a perícia {pericia}?')

                try:
                    msg = await ctx.bot.wait_for("message", check=check, timeout = 65)
                except asyncio.TimeoutError:
                    await ctx.send("Tempo esgotado! Cancelando a personalização das perícia.")
                    return
                
                if msg.content.lower() == "sim":
                    escolhas.append((atributo, pericia))

        if escolhas:
            resumo = "\n".join([f"{atributo}: {pericia}" for atributo, pericia in escolhas])
            await ctx.send(f"Perícias selecionadas:\n{resumo}")
            resultado = CRUD_pericias.create_pericias (discord_id, escolhas)
            await ctx.send(resultado)