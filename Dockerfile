FROM python:3.8-slim

# Installer les dépendances de l'application
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copier le code de l'application
COPY . .

# Exposer le port sur lequel l'application écoute
EXPOSE 5000

# Définir l'entrypoint de l'application
ENTRYPOINT ["python"]
CMD ["app_iris.py"]
