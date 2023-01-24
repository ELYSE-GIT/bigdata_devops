from flask import Flask, request, jsonify
import joblib

# Charger le modèle entraîné
model = joblib.load("iris_knn.joblib")

# Créer une application Flask
app = Flask(__name__)

# Définir une route qui permet de faire une prédiction en utilisant le modèle
@app.route("/predict", methods=["POST"])
def predict():
    # Récupérer les données envoyées par l'utilisateur
    data = request.get_json(force=True)
    # Utiliser le modèle pour faire une prédiction
    prediction = model.predict([data["X"]])[0]
    # Renvoyer la prédiction sous forme de réponse JSON
    return jsonify(prediction)

# Exécuter l'application Flask
if __name__ == "__main__":
    app.run(debug=True)
