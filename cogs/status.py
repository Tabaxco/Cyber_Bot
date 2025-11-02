import discord
from discord.ext import commands
from funções import CRUD_status
import asyncio

class Status(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


# criar status
    @commands.command()
    async def criar_status(self, ctx):
        def check(m):
            return m.author == ctx.author and m.channel == ctx.channel

        try:
            perguntas = [
                    ('Qual o nome do personagem?', 'nome'),
                    ('Qual a especialização do personagem?', 'espe'),
                    ('Qual o nível do personagem?', 'lvl'),
                    ('Quanto de HP o personagem possui?', 'hp'),
                    ('Quanto de CP o personagem possui? (Chakra Points)', 'cp'),
                    ('Quanto de Força o personagem tem?', 'forc'),
                    ('Quanto de Destreza o personagem tem?', 'dex'),
                    ('Quanto de Constituição o personagem tem?', 'con'),
                    ('Quanto de inteligência o personagem tem?', 'inte'),
                    ('Quanto de sabedoria o personagem tem?', 'sab'),
                    ('Quanto de carisma o personagem tem?', 'car')
                ]

            respostas = {}

            for pergunta, chave in perguntas:
                    await ctx.send(pergunta, reference=ctx.message, mention_author=True)
                    resposta = await self.bot.wait_for('message', check=check)
                    respostas[chave] = resposta.content
                    print(f"{resposta.content}")

        
            resultado = CRUD_status.create_status(
                        respostas['nome'], respostas['espe'], respostas['lvl'], respostas['hp'], respostas['cp'],
                        respostas['forc'], respostas['dex'], respostas['con'], respostas['inte'],
                        respostas['sab'], respostas['car'], ctx.author.id
                    )
            await ctx.send(resultado)


        except Exception as e:
                await ctx.send(f"Ocorreu um erro inesperado.")
                print(e)
                






        
    # ver status
    @commands.command()
    async def status(self, ctx, nome: str = None):
        status = CRUD_status.status(nome=nome, discord_id=ctx.author.id)

        if status:
            dados_status = status
            media = CRUD_status.checar_rank(dados_status)
            dumbell = self.bot.get_emoji(1349403661729796216)

            embed = discord.Embed(
                title=f"Status de {dados_status[1]}",
                color=discord.Color.purple()
            )

            campos = [ 
                ("Especialização", dados_status[2]),
                ("Nível", dados_status[3]),
                ("", ""),
                ("Hit Points", dados_status[4]),
                ("Chakra Points", dados_status[5]),
                ("", "") ]
                
            
            for campo, valor in campos:
                embed.add_field(
                    name=f"{campo}",
                    value=f"{valor}",
                    inline= True 
                )

            atributos = [
                ("Força", dados_status[6], dumbell),
                ("Destreza", dados_status[7], "🏃"),
                ("Constituição", dados_status[8], "🛡️"),
                ("Inteligência", dados_status[9], "🧠"),
                ("Sabedoria", dados_status[10], "👁️"),
                ("Carisma", dados_status[11], "🗣️")
            ]

            for nome_attr, valor, emoji in atributos:
                rank = CRUD_status.rank_atributo(valor)
                bonus = CRUD_status.calcular_bonus(valor)
                embed.add_field(
                    name=f"{emoji} {nome_attr}",
                    value=f"{valor} ({bonus}) | {rank}",
                    inline=True
                )

            if dados_status[13]:  # Se existir imagem
                embed.set_image(url=dados_status[13])
            embed.set_footer(text=media)

            await ctx.send(embed=embed, reference=ctx.message, mention_author=True)
        else:
            await ctx.send("❌ Nenhum status encontrado!", reference=ctx.message, mention_author=True)





# Deletar Status
    @commands.command()
    async def del_status(self, ctx, nome: str = None):
        try:
            resultado = CRUD_status.del_status(nome=nome, discord_id=ctx.author.id)
            await ctx.send(resultado, refences=ctx.message, mention_author=True)
        except Exception as e:
             await ctx.send("Ocorreu um erro inesperado.", refence=ctx.message, mention_author=True)
             print(e)



#Atualizar Status
    @commands.command()
    async def update_status(self, ctx, atributo: str = None, valor=None):
        try:
            uptade_status = CRUD_status.update_status(discord_id=ctx.author.id, atributo=atributo, valor=valor)
            await ctx.send(uptade_status)
        except Exception as e:
             await ctx.send("Ocorreu um erro inesperado.", reference=ctx.message, mention_author=True)
             print(e)