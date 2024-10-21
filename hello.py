from flask import Flask, request, render_template
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from datetime import datetime

app = Flask(__name__)
bootstrap = Bootstrap(app)
moment = Moment(app)

@app.route('/')
def hello_world():
   now = datetime.utcnow()
   return render_template('index.html', current_time=now)


@app.route('/user/<name>/<register>/<institution>')
def user(name, register, institution):
    return render_template('user.html', name=name, register=register, institution=institution)

@app.route('/contextorequisicao/<name>')
def contexto_requisicao(name):
    browser = request.headers.get('User-Agent')
    ip = request.remote_addr
    host = request.host
    return render_template('contexto_requisicao.html',name=name, browser=browser, ip=ip, host=host)
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def page_internal_server_error(e):
    return render_template('500.html'), 500