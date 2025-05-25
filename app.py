from flask import Flask, request, jsonify, send_from_directory
import pickle
import numpy as np

app = Flask(__name__, static_folder='static')

# Carrega o modelo
with open("model_xgb.pkl", "rb") as f:
    model = pickle.load(f)

@app.route('/')
def index():
    return send_from_directory('static', 'index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()

    features = np.array([
        data['age'],
        data['sex'],
        data['bmi'],
        data['children'],
        data['smoker'],
        data['region_northwest'],
        data['region_southeast'],
        data['region_southwest']
    ]).reshape(1, -1)

    prediction = model.predict(features)[0]
    return jsonify({'previsao_custo': float(round(prediction, 2))})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)