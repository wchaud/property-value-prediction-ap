# Property Value Prediction API

This project is a Flask-based API that predicts property values based on the area (`metragem`) and number of bedrooms (`dormitorios`) of the property. It connects to a PostgreSQL database to retrieve historical data for training the prediction model.

## Project Structure

```
property-value-prediction-api
├── src
│   ├── main.py           # Entry point of the application
│   ├── api
│   │   └── routes.py     # API route definitions
│   ├── models
│   │   └── predictor.py  # AI model for predicting property values
│   ├── db
│   │   ├── database.py   # Database connection management
│   │   └── populate_db.py# Script to create and populate the table
│   └── utils
│       └── __init__.py   # Utility functions
│   └── train_model.py    # Script to train and save the ML model
├── requirements.txt      # Project dependencies
├── Dockerfile            # Docker image instructions
├── docker-compose.yml    # Docker Compose configuration
└── README.md             # Project documentation
```

## Setup Instructions

1. **Clone the repository:**
   ```
   git clone property-value-prediction-api
   cd property-value-prediction-api
   ```

2. **Install dependencies:**
   You can install the required Python packages using pip:
   ```
   pip install -r requirements.txt
   ```

3. **Set up the PostgreSQL database:**
   Ensure you have PostgreSQL installed and running. The application will automatically create and populate the `imoveis` table with the columns `metragem` (area), `valor` (value), and `dormitorios` (number of bedrooms) when started.

4. **Run the application using Docker:**
   Build and run the application with Docker Compose:
   ```
   docker-compose up --build
   ```

## Usage

Once the application is running, you can make a POST request to the `/predict` endpoint with the area and number of bedrooms of the property to receive a predicted value.

Example request:
```
POST /predict
Content-Type: application/json

{
    "area": 100,
    "dormitorios": 3
}
```

Example response:
```json
{
    "predicted_value": 350000.0
}
```

## Treinando o modelo de IA

Após garantir que a tabela `imoveis` está criada e populada, você pode treinar o modelo de IA com os dados atuais do banco.

**Passos:**

1. Acesse o terminal do container web:
   ```
   docker-compose exec web bash
   ```

2. Execute o script de treinamento:
   ```
   python train_model.py
   ```

Isso irá treinar o modelo com os dados da tabela `imoveis` e salvar o arquivo `model.pkl` para ser utilizado pela API.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.