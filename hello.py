from flask import Flask, request, render_template
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from datetime import datetime
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
bootstrap = Bootstrap(app)
moment = Moment(app)
app.config['SECRET_KEY'] = 'Chave Secreta'

class NameForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    submit = SubmitField('Submit')

@app.route('/', methods=['GET', 'POST'])
def form():
    name = None
    form = NameForm()
    if form.validate_on_submit():
        name = form.name.data
        form.name.data = ''
    return render_template('index.html', form=form, name=name)
    
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.route('/user/<name>/<register>/<institution>')
def user(name, register, institution):
    return render_template('user.html', name=name, register=register, institution=institution)

@app.route('/contextorequisicao/<name>')
def contexto_requisicao(name):
    browser = request.headers.get('User-Agent')
    ip = request.remote_addr
    host = request.host
    return render_template('contexto_requisicao.html',name=name, browser=browser, ip=ip, host=host)

@app.errorhandler(500)
def page_internal_server_error(e):
    return render_template('500.html'), 500