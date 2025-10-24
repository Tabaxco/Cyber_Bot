from database import conectar

def create_pericias(discord_id, escolhas):
    """
    Salva as perícias de um jogador com base no Discord ID.
    
    :param discord_id: ID do jogador no Discord (str)
    :param escolhas: lista de tuplas (atributo, nome_pericia) que o jogador escolheu
    """

    conexao = conectar()
    cursor = conexao.cursor()

    # 1️⃣ Pega o status_id pelo discord_id
    cursor.execute("SELECT id FROM status WHERE discord_id = ?", (str(discord_id),))
    resultado = cursor.fetchone()

    if not resultado:
        print("Personagem não encontrado.")
        conexao.close()
        return

    status_id = resultado[0]

    # 2️⃣ Zera todas as perícias desse personagem
    cursor.execute("""
        UPDATE pericias
        SET proficiente = 0
        WHERE status_id = ? AND discord_id = ?
    """, (status_id, str(discord_id)))

    # 3️⃣ Marca só as escolhidas como proficiente = 1
    for atributo, nome_pericia in escolhas:
        cursor.execute("""
            UPDATE pericias
            SET proficiente = 1
            WHERE status_id = ? AND nome = ? AND atributo = ? AND discord_id = ?
        """, (status_id, nome_pericia, atributo, str(discord_id)))

    conexao.commit()
    conexao.close()
    print(f"Suas perícias foram atualizadas com sucesso!")