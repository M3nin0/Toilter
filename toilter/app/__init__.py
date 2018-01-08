from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate
from flask_migrate import MigrateCommand
from flask_login import LoginManager

app = Flask(__name__)
app.config.from_object('config')

db = SQLAlchemy(app)
migrate = Migrate(app, db)

manager = Manager(app)
# Vinculando o comando 'db' aos comandos de migrate
'''
Comandos do migrate

db init -> Cria os diretórios necessários para o uso do migrate
db migrate -> Lista as alterações para dar inicio a criação do banco de dados
db upgrade -> Depois de utilizar o migrate, será necessário fazer o upgrade, para que
as mudanças no banco sejam efetivadas
'''

manager.add_command('db', MigrateCommand)

lm = LoginManager(app)

# Import depois pois o default precisa do app criado
from app.controllers import default
from app.models import tables
from app.models import forms
