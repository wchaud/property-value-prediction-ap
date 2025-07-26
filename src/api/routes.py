from flask import Blueprint, request, jsonify
from db.database import get_db_connection
from models.predictor import Predictor

api = Blueprint('api', __name__)

db_session = get_db_connection()
predictor = Predictor(db_session)

@api.route('/predict', methods=['POST'])
def predict_property_value():
    data = request.get_json()
    area = data.get('area')
    dormitorios = data.get('dormitorios')

    if area is None or dormitorios is None:
        return jsonify({'error': 'Area and dormitorios are required'}), 400
    
    predicted_value = predictor.predict_value(area, dormitorios)
    return jsonify({'predicted_value': predicted_value})