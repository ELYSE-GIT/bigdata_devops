Voici les étapes détaillées pour mettre en place le pipeline de déploiement :

######    1. Training du modèle (Iris avec scikit-learn KNN) et export (joblib.dump) :
        Commencez par entraîner votre modèle de classification sur le jeu de données Iris en utilisant scikit-learn et l'algorithme KNN (K Nearest Neighbors).
        Utilisez la fonction joblib.dump de scikit-learn pour exporter votre modèle entraîné au format joblib.

######    2. Intégrer son modèle entrainé dans une API :
        Créez une API Flask qui prend en entrée des données d'Iris et renvoie la prédiction de votre modèle entraîné.
        Utilisez le fichier joblib exporté précédemment pour charger votre modèle dans votre API Flask.

        Pour tester l'API, vous pouvez utiliser Postman ou Curl :
        Pour utiliser cURL pour appeler l'API sur Ubuntu, vous pouvez utiliser la commande suivante :

        >> curl -X POST -H "Content-Type: application/json" -d '{"X": [5.1,3.5,1.4,0.2]}' http://localhost:5000/predict

                Cette commande envoie une requête POST avec les données d'entrée JSON (dans ce cas, {"X": [5.1,3.5,1.4,0.2]}) à l'URL de l'API (http://localhost:5000/predict).

                Explanation:
                -X POST : spécifie que c'est une requête POST
                -H "Content-Type: application/json" : indique que les données dans la requête sont de type JSON
                -d '{"X": [5.1,3.5,1.4,0.2]}' : les données d'entrée sont passées ici
                http://localhost:5000/predict : l'url de l'api

En exécutant cette commande, cURL affichera la réponse de l'API, qui devrait être la prédiction sous forme de chaîne de caractères JSON.

######    3. Packager son API dans une image Docker en local :
        Créez un fichier Dockerfile qui décrit comment construire l'image Docker de votre API.

        Utilisez la commande "docker build" pour construire l'image Docker de votre API en local : 


######    4. Publier son code sur Github :
        Créez un dépôt Github et publiez votre code (API Flask et fichier Dockerfile) dans ce dépôt.

######    5. Configurer la pipeline de déploiement avec les élements suivants :
        Construire l'image Docker : utilisez la commande "docker build" pour construire une nouvelle image Docker de votre API à chaque fois que des modifications sont apportées à votre code sur Github.

                >> docker build -t efreiprediris:latest . 

        Publier l'image Docker sur Azure Container Registry (ACR) : utilisez la commande "docker push" pour publier votre image Docker sur Azure Container Registry (ACR).
                >> connect : az login
                >> connect to ACR : az acr login -n efreiprediction.azurecr.io


        Déployer sur Azure Container App : utilisez Azure Container App pour déployer votre image Docker sur un cluster de conteneurs.
                >> docker tag efreiprediris:latest efreiprediction.azurecr.io/efreiprediris:latest
                >> docker push efreiprediction.azurecr.io/efreiprediris:latest




        Configurer l'autoscaling en utilisant comme paramètre le nombre de requêtes en simultané : utilisez l'outil d'autoscaling d'Azure pour configurer l'ajustement automatique de la taille de votre cluster en fonction du nombre de requêtes simultanées reçues par votre API.

######    6. Test de charge avec l'outil de votre choix et observer l'autoscaling :
        Utilisez un outil de test de charge tel que JMeter pour envoyer des requêtes simulées à votre API déployée sur Azure Container App.
        Observez comment l'autoscaling réagit en ajustant la taille de votre cluster en fonction du nombre de requêtes reçues.

######    7. Ajouter un endpoint /metrics en utilisant la librairie prometheus-client puis mettre a disposition une/des metriques d'utilisation de l'API (exemple: counter avec le nombre de calls) :
        Ajoutez un endpoint /metrics à votre API Flask qui utilise la librairie prometheus-client pour exposer des métriques sur l'utilisation de l'API. Par exemple, vous pouvez utiliser un counter pour enregistrer le nombre de appels à l'API.
        Exposez ces métriques en utilisant l'interface HTTP de prometheus-client.

######    8. Utiliser un linter pour Dockerfile dans la pipeline de déploiement pour s'assurer de sa cohérence :
        Utilisez un linter pour Dockerfile (par exemple, hadolint) pour vérifier la syntaxe et la qualité de votre fichier Dockerfile.
        Intégrez ce linter dans votre pipeline de déploiement afin de vérifier la cohérence de votre fichier Dockerfile avant chaque déploiement.

######    9. Mettre en place une stack prometheus local pour scraper et stocker vos metriques exposées :
        Installez une stack Prometheus (prometheus-server, node-exporter, etc.) en local.
        Configurez Prometheus pour scraper les métriques exposées par votre API via l'endpoint /metrics.
        Stockez ces métriques dans Prometheus afin de pouvoir les afficher et les analyser ultérieurement.




## RESUME:

Voici un résumé des étapes de votre pipeline de déploiement :

    1. Entraîner un modèle de classification sur le jeu de données Iris et l'exporter au format joblib.
    2. Créer une API Flask qui utilise ce modèle pour prédire des valeurs d'Iris.
    3. Packager l'API dans une image Docker en utilisant un fichier Dockerfile.
    4. Publier le code de l'API sur Github.
    5. Configurer une pipeline de déploiement qui construit une nouvelle image Docker à chaque modification du * 6. code, la publie sur Azure Container Registry, et la déploie sur Azure Container App.
    7. Configurer l'autoscaling de votre cluster sur Azure Container App en fonction du nombre de requêtes simultanées reçues par l'API.
    8. Tester la charge sur l'API en utilisant JMeter et observer comment l'autoscaling réagit.
    9. Ajouter un endpoint /metrics à l'API pour exposer des métriques sur son utilisation.
    10. Utiliser un linter pour Dockerfile pour vérifier la cohérence de votre fichier Dockerfile avant chaque déploiement.
    11. Mettre en place une stack Prometheus en local pour scraper et stocker les métriques exposées par l'API.







## RESUME avant les Bonus 

Voici un résumé des étapes et du but de ces étapes pour entraîner un modèle (Iris avec scikit-learn KNN), l'intégrer dans une API, l'empaqueter dans une image Docker, le déployer sur Azure Container App et configurer l'autoscaling avec Prometheus :

    Entraîner le modèle : Nous avons utilisé scikit-learn et le jeu de données Iris pour entraîner un modèle de classification KNN.

    Intégrer le modèle dans une API : Nous avons utilisé Flask pour créer une API qui prend en entrée des données de mesure de fleurs et qui renvoie une prédiction de la espèce de fleur.

    Empaqueter l'API dans une image Docker : Nous avons utilisé Docker pour empaqueter notre API et ses dépendances dans une image facilement déployable.

    Déployer l'image sur Azure Container App : Nous avons utilisé Azure DevOps et Azure Container App pour déployer notre image sur le cloud de manière automatisée.

    Configurer l'autoscaling : Nous avons utilisé Prometheus pour configurer l'autoscaling de notre API en fonction du nombre de requêtes en simultané.


Le but de ces étapes est de créer une API qui peut être facilement déployée et mise à l'échelle en fonction de la charge, en utilisant les outils et services Azure. Cette API peut être utilisée pour prédire la espèce de fleur en utilisant un modèle de classification KNN entraîné avec scikit-learn et le jeu de données Iris.

Pour tester la performance et l'évolutivité de l'API, nous avons utilisé un outil de test de charge tel que Apache JMeter ou Loader.io. Nous avons également ajouté un endpoint /metrics à l'API en utilisant la librairie prometheus-client, afin de mettre à disposition des métriques d'utilisation de l'API. Ces métriques peuvent être utilisées pour surveiller et optimiser la performance et l'évolutivité de l'API.

Ceci est la fin du résumé des étapes et du but de ces étapes pour entraîner un modèle, l'intégrer dans une API, l'empaqueter dans une image Docker, le déployer sur Azure Container App et configurer l'autoscaling avec Prometheus.