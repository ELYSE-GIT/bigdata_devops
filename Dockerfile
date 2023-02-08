FROM python:3.8-slim

# Créer un environnement virtuel pour l'application
RUN python -m venv /venv
ENV PATH="/venv/bin:$PATH"

# Installer les dépendances de l'application
COPY requirements.txt .
RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt

# Copier le code de l'application
COPY . .

# Exposer le port sur lequel l'application écoute
EXPOSE 5000

# Définir l'entrypoint de l'application
ENTRYPOINT ["python"]
CMD ["app_iris.py"]
