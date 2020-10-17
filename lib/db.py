from pymongo import MongoClient

conexao = MongoClient('mongodb://localhost:27017')

# Banco recomendacao
db = conexao.recomendacao

# Coleção filmes
col_filmes = db.filmes

# Documentos
def documentos():
    lista = col_filmes.find({'_id': 0}, {})
    return lista