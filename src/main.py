from flask import Flask
from db.populate_db import populate

app = Flask(__name__)

# Popula o banco antes de importar qualquer coisa que use a tabela
populate()

from db.database import get_db_connection
from api.routes import api

# Agora sim, registre o blueprint (que instancia o Predictor)
app.register_blueprint(api)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)