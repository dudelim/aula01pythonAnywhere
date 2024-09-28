# A very simple Flask Hello World app for you to get started with...
from flask import Flask, Response, request, make_response, redirect, abort

app = Flask(__name__)
@app.route('/')
def hello_world():
    return '<p>Alterações por meio do GitHub</p><table><tr><td><b>Aluno(a):</b></td><td>Maria Eduarda Melim de Oliveira</td></tr><tr><td><b>Prontuário:</b></td><td>PT3025594</td></tr></table>'

@app.route('/user/<name>')
def user(name):
    return '<h1>Hello, {}!</h1>'.format(name)

@app.route('/contextorequisicao')
def contexto_requisicao():
  browser = request.headers.get('User-Agent')
  return '<p>{}</p>'.format(browser)

@app.route('/codigostatusdiferente')
def codigo_status_diferente():
    return 'Bad request', 400

@app.route('/objetoresposta')
def objetoresposta():
  response = make_response('<h1>This document carries a cookie!</h1>')
  response.set_cookie('answer', '42')
  return response

@app.route('/redirecionamento')
def redirecionamento():
  location = "https://ptb.ifsp.edu.br/"
  return redirect (location)

@app.route('/abortar')
def abortar():
  return abort(404)

