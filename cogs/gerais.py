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
            color=discord.Color.dark_red()
        )

        embed.add_field(
            name='Status',
            value=(
                "**$criar_status** - *Cria o status do personagem*\n"
                "**$status** - *Busca o status atual do personagem*\n"
                "**$del_status** - *Deleta o status do personagem*\n"
                "**$update_status** - *Atualiza o valor de algum atributo do personagem*\n"
            ),
            inline = False
        )

        embed.add_field(
            name="Rolagem de Dados",
            value=(
                "**$roll** - *Rola os dados*"
            ),
            inline = False
        )

        await ctx.send(embed=embed, reference=ctx.message, mention_author=True)