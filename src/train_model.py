import pandas as pd
import pickle
from sklearn.linear_model import LinearRegression
from sqlalchemy import create_engine

# Ajuste a string de conexão conforme seu ambiente
engine = create_engine('postgresql://chaud:teste@db:5432/property_db')

# Carrega os dados da tabela
df = pd.read_sql('SELECT metragem, dormitorios, valor FROM imoveis', engine)

X = df[['metragem', 'dormitorios']]
y = df['valor']

model = LinearRegression()
model.fit(X, y)

# Salva o modelo treinado
with open('model.pkl', 'wb') as f:
    pickle.dump(model, f)

print("Modelo treinado e salvo como model.pkl")