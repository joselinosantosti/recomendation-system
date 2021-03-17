from pymongo import MongoClient

class Conexao:
    def __init__(self):
        self.conexao = MongoClient('mongodb://localhost:27017')

        # Banco recomendacao
        self.db = self.conexao.recomendacao

        # Colecao filmes
        self.col_filmes = self.db.db_filmes

    # Documentos - Sem id
    def lista_filmes(self):
        return self.col_filmes.find({}, {"_id":0})
