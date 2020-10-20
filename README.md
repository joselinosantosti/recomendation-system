# Sistema de recomendação de filmes
Pode ser aplicado a filmes, músicas, produtos e muito mais.

Desenvolvido com Python, Flask e MongoDB

# 1. Dados
O sistema recebe os dados de um banco MongoDB.

# 1. Filtragem colaborativa
O sistema possui um algoritmo de recomendação baseado em filtragem colaborativa. Cada usuário dá notas para vários itens e a partir do cálculo da distância euclidiana é possível verificar os usuários similares.

# 2. Recomendação
Com esses dados a próxima etapa é recomendar os itens. Para isso o algoritmo realiza outros cálculos para dar maior peso aos itens mais relevantes. A recomendação por itens é mais recomendada, pois os dados ficam salvos em uma variável, arquivo ou no banco, agilizando as consultas.

# 3. Exibição dos dados
A App possui uma função para renderizar os dados na interface Web.
