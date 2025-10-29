from database import conectar

def create_status(nome, especializacao, nivel, hp, cp, forc, dex, con, inte, sab, car, discord_id):
    '''Cria os status do personagem
    Todos os parâmetros são os atributos do RPG.'''

    parametros = [nome, especializacao, nivel, hp, cp, forc, dex, con, inte, sab, car, discord_id]
    if any(p is None for p in parametros):
        raise TypeError('Todos os parametros devem ser preenchidos.')
      
    try:
        conexao = conectar()
        cursor = conexao.cursor()

        cursor.execute('''
            INSERT INTO status (nome, especializacao, nivel, hp, cp, forca, destreza, constituicao, inteligencia,
                        sabedoria, carisma, discord_id)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (nome, especializacao, nivel, hp, cp, forc, dex, con, inte, sab, car, discord_id))

        conexao.commit()
        conexao.close()

    except Exception as e:
        return f'Ocorreu um erro ao criar o status: {e}'
    else:
        return f'Status de {nome} criado com sucesso!'






def status(nome = None, discord_id = None):
    '''Mostra os status com as informações de atirbutos do personagem'''

    conexao = conectar()
    cursor = conexao.cursor()

    if nome:
        cursor.execute("SELECT * FROM status WHERE nome = ?", (nome,))
    elif discord_id:
       cursor.execute("SELECT * FROM status WHERE discord_id = ?", (discord_id,))
    else:
        return None

    status = cursor.fetchone()
    conexao.close()
    return status







def update_status(discord_id = None, atributo = None, valor = None):
    '''Atualiza os status do personagem.'''

    atributo_escolhido = None

    atributos_validos = {
    "nome" : "Nome",
    "especializacao" : "Especialização",
    "nivel": "Nível",
    "hp" : "Hit Points",
    "cp" : "Chakra Points",
    "forca" : "Força",
    "destreza" : "Destreza",
    "constituicao" : "Constituição",
    "inteligencia" : "Inteligência",
    "sabedoria" : "Sabedoria",
    "carisma" : "Carisma",
    "aparencia" : "Aparência"
    }

    if atributo not in atributos_validos:
        return f'{atributo.capitalize()} é um dado inválido.'
    
    conexao = conectar()
    cursor = conexao.cursor()

    query = f"UPDATE status SET {atributo} = ? WHERE discord_id = ?"
    cursor.execute(query, (valor, discord_id))

    conexao.commit()
    conexao.close()
    
    atributo_escolhido = atributos_validos[atributo]
    return f"{atributo_escolhido} atualizado com sucesso para {valor}"









def del_status(nome = None, discord_id = None):
    '''Deleta os status do personagem.'''

    conexao = conectar()
    cursor = conexao.cursor()

    if nome:
        cursor.execute("DELETE FROM status WHERE nome = ?", (nome,))
    elif discord_id:
        cursor.execute("DELETE FROM status WHERE discord_id = ?", (discord_id,))
    else:
        return 'Nenhum status encontrado.'
    
    conexao.commit()
    conexao.close()
    return 'Status deletado com sucesso.'








def checar_rank (valor):
    '''Checa o rank do personagem.'''

    rankmedia = sum(int(valor[i]) for i in range(6, 12)) / 6

    if rankmedia > 20:
        rank = 'S+'
    elif rankmedia >= 19:
        rank = 'S'
    if rankmedia >= 16:
        rank = 'A'
    elif rankmedia >= 13:
        rank = 'B'
    elif rankmedia >= 10:
        rank = 'C'
    elif rankmedia >= 7:
        rank = 'D'
    elif rankmedia >= 5:
        rank = 'E'
    elif rankmedia >= 3:
        rank = 'F'
    else:
        rank = 'G'

    return f'Rank Total: {rank} - {rankmedia:.2f}'


def rank_atributo (valor):

    if valor > 20:
        rank = 'S+'
    elif valor >= 19:
        rank = 'S'
    elif valor >= 16:
        rank = 'A'
    elif valor >= 13:
        rank = 'B'
    elif valor >= 10:
        rank = 'C'
    elif valor >= 7:
        rank = 'D'
    elif valor >= 5:
        rank = 'E'
    elif valor >= 3:
        rank = 'F'
    else:
        rank = 'G'
    
    return rank

def calcular_bonus(valor):
    bonus = (valor - 10) // 2
    return f"+{bonus}" if bonus >= 0 else str(bonus)
        