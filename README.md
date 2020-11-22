# Sistema de recomendação de filmes
## Pode ser aplicado a filmes, músicas, produtos e muito mais.

![Sistema de recomendação](https://github.com/joselinosantosti/recomendation-system/blob/master/filmes.png)

## Desenvolvido com Python, Flask e MongoDB

# 1. Estrutura
A pasta principal contém o seguinte:
* Arquivo app.py com métodos Flask para renderização da página Web
O seguinte método recomenda os itens para um usuário passado
```
def recomenda():
	return dict(lista_filmes=recomendacao.getRecomendacoesItens(usuario=_usuario))
```
* Pasta templates: Contém os arquivos html, no caso, só o index.html
* Pasta static: Contém arquivos estáticos como imagens e folhas de estilo css
* pasta lib: é um pacote que criei com classe para conexão com banco e métodos para filtragem e recomendação(A parte principal está neste arquivo).

# 2. Dados
O sistema recebe os dados de um banco MongoDB no seguinte formato de dicionário Python:
```
db.filmes.insert({'Avatar': {'Luiz': 3.0,  'Lucas:': 2.5,  'Aline': 3.8,   'Jessica': 2.0 }})`
```
* Crie um banco de dados com o nome sistema_recomendacao: `use sistema`
* Crie uma coleção com o nome filmes e já adiciona o primeiro filme: `db.filmes.insert('Freddy x Jason': {'Ana':2.5, 'Marcos': 3.0, 'Pedro':2.5,'Adriano':3.0,'Janaina':3})`
* Alimente a base de dados com filmes variados

# 3. Filtragem colaborativa
O sistema possui um algoritmo de recomendação baseado em filtragem colaborativa. Cada usuário dá notas para vários itens e a partir do cálculo da distância euclidiana é possível verificar os usuários similares. As etapas são as seguintes.
* Instanciar a classe Conexao e obter os dados, em seguida transformar os dados do MongoDB do tipo cursor em dicionário (Sem isso o algoritmo não reconhece o formato dos dados corretamente).
* O método da distândia euclidiana realiza os seguintes cálculos: `soma = sum([pow(base[filme1][item] - base[filme2][item], 2)`. Percore as listas de filmes e subtrai as notas, em seguida eleva ao quadrado e depois soma tudo. O valor final é a similaridade entre os filmes.
* Calcular a similaridade de todos os itens e salvar em uma variável. Essa abordagem(por itens) torna o algoritmo mais rápido que por usuários visto que a frequência de dados de itens inseridos na base é muito menor que a frequência de novos usuários.

# 4. Recomendação
getRecomendacoesItens <br/>
Com esses dados a próxima etapa é recomendar os itens. Para isso o algoritmo realiza outros cálculos para dar maior peso aos itens mais relevantes. A recomendação por itens é mais recomendada, pois os dados ficam salvos em uma variável, arquivo ou no banco, agilizando as consultas.

# 5. Exibição dos dados na Web
A App possui uma função para renderizar os dados na interface Web. Para executar acesse o diretório principal através do terminal e execute: `python app.py`
Acesse o navegador e digite o endereço e porta vistos no terminal. O padrão é a própria máquina e porta 5000 http://127.0.0.1:5000/.
