#import db
from math import sqrt

# Dados do Mongo
#dadosMongo = db.lista_filmes()

# Dados estaticos - Apenas para testes
avaliacoes = {'Ana': 
		{'Matrix': 2.5, 
		 'Vingadores': 3.5,
		 'Star Trek': 3.0, 
		 'Exterminador do Futuro': 3.5, 
		 'Norbit': 2.5,
		 'Star Wars': 3.0},
	 
	  'Marcos': 
		{'Matrix': 3.0, 
		 'Vingadores': 3.5, 
		 'Star Trek': 1.5, 
		 'Exterminador do Futuro': 5.0, 
		 'Star Wars': 3.0, 
		 'Norbit': 3.5}, 

	  'Pedro': 
	    {'Matrix': 2.5, 
		 'Vingadores': 3.0,
		 'Exterminador do Futuro': 3.5, 
		 'Star Wars': 4.0},
			 
	  'Claudia': 
		{'Vingadores': 3.5, 
		 'Star Trek': 3.0,
		 'Star Wars': 4.5, 
		 'Exterminador do Futuro': 4.0, 
		 'Norbit': 2.5},
				 
	  'Adriano': 
		{'Matrix': 3.0, 
		 'Vingadores': 4.0, 
		 'Star Trek': 2.0, 
		 'Exterminador do Futuro': 3.0, 
		 'Star Wars': 3.0,
		 'Norbit': 2.0}, 

	  'Janaina': 
	     {'Matrix': 3.0, 
	      'Vingadores': 4.0,
	      'Star Wars': 3.0, 
	      'Exterminador do Futuro': 5.0, 
	      'Norbit': 3.5},
			  
	  'Leonardo': 
	    {'Vingadores':4.5,
             'Norbit':1.0,
	     'Exterminador do Futuro':4.0},
    'Luana':
              {'Divetidamente':4.0}
}

avaliacoesFilme = {'Matrix': 
		{'Ana': 2.5, 
		 'Marcos:': 3.0 ,
		 'Pedro': 2.5, 
		 'Adriano': 3.0, 
		 'Janaina': 3.0 },
	 
	 'Vingadores': 
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

    # Listar todos os usuarios do filme 1
    for item in base[filme1]:

        # Verificar se os usuarios do filme 1 viram o filme 2
        if item in base[filme2]:
            si[item] = 1 # Atribui o valor 1 a nossa lista de similaridades

    if len(si) == 0:
        return 0

    # Retorna a nota
    soma = sum([pow(base[filme1][item] - base[filme2][item], 2)

    # A mesma comparação feita em cima, se o usuario viu o filme1 e o filme2
    for item in base[filme1] if item in base[filme2]])
    return 1/(1+sqrt(soma)) # Retorna o calculo da porcentagem de similaridade entre os 2 filmes

def getSimilares(base, filme):
    # Compara a similaridade do filme com todos os outros
    similaridade = [(euclidiana(base, filme, outro), outro)
                    for outro in base if outro != filme]
    similaridade.reverse() # Ordena decrescente
    return similaridade[0:30] # 30 primeiros registros

# Função Itens similares
def calculaItensSimilares(base=avaliacoesFilme):
    result = {}
    for i in base:
        notas = getSimilares(base,  i)
        result[i] = notas
    return result
    print( )

# Salva os dados na variavel
itensSimilares = calculaItensSimilares(avaliacoesFilme)

# Função recomendar
def getRecomendacoesItens(baseUsuario=avaliacoes, similaridadeItens=itensSimilares, usuario='Leonardo'):
    notasUsuario = baseUsuario[usuario]
    notas = {}
    totalSimilaridades = {}
    
    for (item, nota) in notasUsuario.items():
        for (similaridade, i2) in similaridadeItens[item]:
            if i2 in notasUsuario: continue
            notas.setdefault(i2, 0)
            notas[i2] += similaridade * nota
            totalSimilaridades.setdefault(i2, 0)
            totalSimilaridades[i2] += similaridade
    rankings = [(score/totalSimilaridades[item], item) for item, score in notas.items()]
    rankings.sort()
    rankings.reverse()
    return dict(rankings).values()
