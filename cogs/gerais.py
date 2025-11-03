import discord
from discord.ext import commands

class Gerais(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def ajuda(self, ctx):
        embed = discord.Embed(
            title="Ajuda da Cyber",
            description="Lista de comandos disponíveis",
            color=discord.Color.purple()
        )

        embed.add_field(
            name='Status',
            value=(
                "**$criar_status** - cria o status do personagem\n"
                "**$status** - busca o status atual do personagem\n"
                "**$del_status** - deleta o status do personagem\n"
                "**$update_status** - atualiza o valor de algum atributo do personagem\n"
            ),
            inline = False
        )

        embed.add_field(
            name="Rolagem de Dados",
            value=(
                "**$roll xdy** - gira dados de diferentes lados e faces, sendo 'x' a quantidade de dados, e 'y' a quantidade de faces. O 'd' é necessário para o funcionamento do comando"
            ),
            inline = False
        )

        await ctx.send(embed=embed, reference=ctx.message, mention_author=True)