from flask import render_template
from flask import flash
from flask_login import login_user
from app import app
from app import db

from app.models.forms import LoginForm

from app.models.tables import User

@app.route('/')
@app.route('/index/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    # Fazendo validação do form
    if form.validate_on_submit():
        user = User.query.filter_by(username = form.username.data).first()

        if user and user.password == form.password.data:
            login_user(user)
            flash('Login feito com sucesso.')
        else:
            flash('Informações inválidas!')

    return render_template('login.html',
                           form = form)

# @app.route('/test/<info>')
# @app.route('/test/', defaults={'info': None})
# def test(info):
#     # i = User('felipe2', '222', 'pm2', 'email_2')
#     # db.session.add(i)
#     # db.session.commit()
#     r = User.query.filter_by(password="111").all()
#
#     nomes = ['joao', 'pedro', 'maria']
#     for i in range(0, len(r)):
#         r[i].name = nomes[i]
#         db.session.delete(r[i])
#         db.session.commit()
#     return 'oks'

# @app.route('/test/', defaults = {'name': None})
# @app.route('/test/<name>')
# def test(name):
#     if name:
#         return 'Oii, %s' % name
#     else:
#         return 'Olá usuário!'
#
# @app.route('/profile/<int:_id>')
# def profile(_id):
#     return 'Profile ID: ' + str(_id)
