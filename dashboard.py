import streamlit as st
from sklearn.neighbors import KNeighborsClassifier
import joblib

# Chargement du modèle entraîné
knn = joblib.load('iris_knn.joblib')
# load model

# Définir les options de sélection de classe
class_options = ["Iris-setosa", "Iris-versicolor", "Iris-virginica"]

# Création d'interface utilisateur
st.title("Iris Classification using KNN")

# entrée de feature de l'iris 
sepal_length = st.number_input("Sepal Length")
sepal_width = st.number_input("Sepal Width")
petal_length = st.number_input("Petal Length")
petal_width = st.number_input("Petal Width")

# Bouton pour soumettre les caractéristiques pour une prédiction
if st.button("Submit"):
    result = knn.predict([[sepal_length, sepal_width, petal_length, petal_width]])
    st.success("Class: {}".format(class_options[result[0]]))
