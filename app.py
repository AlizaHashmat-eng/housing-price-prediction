from flask import Flask, request, jsonify
import joblib

app = Flask(__name__)

# Load the trained model
model = joblib.load('housing_price_model.pkl')

@app.route('/predict', methods=['POST'])
def predict():
    # Get the features from the request
    features = request.json['features']
    prediction = model.predict([features])
    return jsonify({'prediction': prediction[0]})

if __name__ == '__main__':
    app.run(debug=True)

