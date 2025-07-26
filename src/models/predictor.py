import pandas as pd
from sklearn.linear_model import LinearRegression
import numpy as np

class Predictor:
    def __init__(self, db_session):
        self.db_session = db_session
        # Carrega os dados do banco
        df = pd.read_sql('SELECT metragem, dormitorios, valor FROM imoveis', self.db_session.bind)
        X = df[['metragem', 'dormitorios']]
        y = df['valor']
        # Treina o modelo
        self.model = LinearRegression()
        self.model.fit(X, y)

    def predict_value(self, area, dormitorios):
        X = np.array([[area, dormitorios]])
        predicted = self.model.predict(X)
        return float(predicted[0])