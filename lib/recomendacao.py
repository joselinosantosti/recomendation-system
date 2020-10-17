import db
from math import sqrt

dados = db.documentos()

avaliacoesFilme = {'Freddy x Jason': 
		{'Ana': 2.5, 
		 'Marcos:': 3.0 ,
		 'Pedro': 2.5, 
		 'Adriano': 3.0, 
		 'Janaina': 3.0 },
	 
	 'O Ultimato Bourne': 
		{'Ana': 3.5, 
		 'Marcos': 3.5,
		 'Pedro': 3.0, 
		 'Claudia': 3.5, 
		 'Adriano': 4.0, 
		 'Janaina': 4.0,
		 'Leonardo': 4.5 },
				 
	 'Star Trek': 
		{'Ana': 3.0, 
		 'Marcos:': 1.5,
		 'Claudia': 3.0, 
		 'Adriano': 2.0 },
	
	 'Exterminador do Futuro': 
		{'Ana': 3.5, 
		 'Marcos:': 5.0 ,
		 'Pedro': 3.5, 
		 'Claudia': 4.0, 
		 'Adriano': 3.0, 
		 'Janaina': 5.0,
		 'Leonardo': 4.0},
				 
	 'Norbit': 
		{'Ana': 2.5, 
		 'Marcos:': 3.0 ,
		 'Claudia': 2.5, 
		 'Adriano': 2.0, 
		 'Janaina': 3.5,
		 'Leonardo': 1.0},
				 
	 'Star Wars': 
		{'Ana': 3.0, 
		 'Marcos:': 3.5,
		 'Pedro': 4.0, 
		 'Claudia': 4.5, 
		 'Adriano': 3.0, 
		 'Janaina': 3.0}
}

# Distancia euclidiana
def euclidiana(base, filme1, filme2):
    si = {} # Criando um dicionário vazio para armazenar as similaridades
    
    # Listar todos os filmes que o usuário 1 assistiu
    for item in base[filme1]:
       
        # Verificar se os filmes vistos pelo usuario 1 estão na lista do usuario2
        if item in base[filme2]:
            si[item] = 1 # Atribui o valor 1 a nossa lista de similaridades
            
    if len(si) == 0:
        return 0
    
    # Retorna a nota
    soma = sum([pow(base[filme1][item] - base[filme2][item], 2)
    
    # A mesma comparação feita em cima, se o filme foi visto pelo usu1 e o usu2
    for item in base[filme1] if item in base[filme2]])
    return 1/(1+sqrt(soma)) # retorna o calculo da porcentagem entre os 2 usuarios

euclidiana(avaliacoesFilme, 'Freddy x Jason', 'O Ultimato Bourne')

def getSimilares(base, filme):
    # Compara a similaridade do filme com todos os outros
    similaridade = [(euclidiana(base, filme, outro), outro)
                    for outro in base if outro != filme]
    similaridade.reverse() # Ordena decrescente
    return similaridade[0:30] # 30 primeiros registros

# Função Itens similares
def calculaItensSimilares(base):
    result = {}
    for i in base:
        notas = getSimilares(base,  i)
        result[i] = notas
    return result
    print( )

getSimilares(avaliacoesFilme, 'O Ultimato Bourne')

# Salva os dados na variavel
#itensSimilares = calculaItensSimilares(avaliacoesFilme); itensSimilares
