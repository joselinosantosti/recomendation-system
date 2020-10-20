from flask import Flask, render_template, json, request
from lib import recomendacao
from datetime import datetime

app = Flask(__name__)
_usuario = 'Pedro'

@app.route('/')
def main():
	return render_template('index.html')

@app.context_processor
def recomenda():
	return dict(lista_filmes=recomendacao.getRecomendacoesItens(usuario=_usuario))

@app.context_processor
def retorna_dados():
	_data = str(datetime.today().year)
	return dict(data=_data, usuario=_usuario)

if __name__ == "__main__":
	app.run()
