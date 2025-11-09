import json
import os

def ver_inv(discord_id):
    caminho = os.path.join("..", "inventario.json")
    with open(caminho, "r", encoding="utf-8") as f:
        dados = json.load(f)

    usuario_id = discord_id

    if usuario_id not in dados:
        return {"Usuário não encontrado."}
    
    data_usuario = dados[usuario_id]

    resultado = []
    for nome, info in data_usuario["personagens"].items():
        resultado.append("Nome")
