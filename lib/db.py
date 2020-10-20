from pymongo import MongoClient

conexao = MongoClient('mongodb://localhost:27017')

# Banco recomendacao
db = conexao.recomendacao

# Coleção filmes
col_filmes = db.filmes

# Documentos - Sem id
def lista_filmes():
    return col_filmes.find({}, {"_id":0})
