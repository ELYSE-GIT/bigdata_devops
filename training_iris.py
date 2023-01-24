# Charger les données Iris
from sklearn.datasets import load_iris
X, y = load_iris(return_X_y=True)

# Séparer les données en un jeu d'entraînement et de test
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)

# Entraîner un modèle KNN
from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X_train, y_train)

# Évaluer le modèle sur le jeu de test
accuracy = knn.score(X_test, y_test)
print("Accuracy : {:.2f}".format(accuracy))

# Exporter le modèle entraîné en utilisant joblib
import joblib
joblib.dump(knn, "iris_knn.joblib.h5")
