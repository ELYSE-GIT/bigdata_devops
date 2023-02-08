from flask import Flask, request, jsonify
import joblib
from jsonschema import validate, ValidationError

# Charger le modèle entraîné
model = joblib.load("iris_knn.joblib")

# Créer une application Flask
app = Flask(__name__)

# Définir un schéma de validation pour les données d'entrée
input_schema = {
    "type": "array",
    "items": {
        "type": "number"
    },
    "minItems": 4,
    "maxItems": 4
}

# Définir une route qui permet de faire une prédiction en utilisant le modèle
@app.route("/predict", methods=["POST"])
def predict():
    # Récupérer les données envoyées par l'utilisateur
    data = request.get_json(force=True)
    try:
        # Valider les données d'entrée
        validate(data["X"], input_schema)
        # Utiliser le modèle pour faire une prédiction
        prediction = str(model.predict([data["X"]])[0])
        # Renvoyer la prédiction sous forme de réponse JSON
        return jsonify(prediction=prediction, valid_input=True)
    except ValidationError as e:
           # Si les données d'entrée sont invalides, renvoyer une réponse JSON indiquant l'erreur
             return jsonify(valid_input=False, error=e.message)
    except KeyError:
             return jsonify(valid_input=False, error="No input data provided")


# Exécuter l'application Flask
if __name__ == "__main__":
    app.run(debug=True)
