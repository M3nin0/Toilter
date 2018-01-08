# Toilter
[![License](https://img.shields.io/badge/License-BSD%203--Clause-blue.svg)](https://opensource.org/licenses/BSD-3-Clause)

Réplica do Twitter criado utilizando o tutorial da @juliarizza

## Executando

### Fazendo download

```shell
git clone https://github.com/M3nin0/Toilter.git
cd Toilter
```

### Instalando as dependências

Para utilizar sem erros o Toilter será criado um ambiente virtual, utilizando o virtualenv.

Caso não tenha instalado, use:
```shell 
apt-get install python3-virtualenv
```

Após instalar o virtualenv

```shell
# Crie o ambiente virtual
virtualenv venv

# Ative o ambiente virtual
source venv/bin/activate
pip install -r requirements.txt
```

### Gerando banco de dados
```shell
cd toilter
# Inicializa os diretórios
python run.py db init
# Faz as mudanças no banco de dados criado
python run.py db migrate
# Salva as alterações
python run.py db upgrade
```

Após realizar estes passos basta executar o server:
```shell
python run.py runserver
```
