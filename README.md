# 🏥 Desert Médicaux Backend

API REST FastAPI pour l'analyse de la démographie médicale en France.

---

## 🚀 Technologies

- **Python 3.9+**
- **FastAPI**
- **psycopg2** (PostgreSQL)
- **dotenv**
- **Uvicorn**

---

## 🤔 Pourquoi ces technologies ?

### Pourquoi avoir choisi **FastAPI** pour le backend ?

- **Performance** : FastAPI est l'un des frameworks Python les plus rapides grâce à son architecture asynchrone basée sur Starlette et Pydantic. Il rivalise avec Node.js et Go en termes de rapidité pour les API web.
- **Simplicité et Productivité** : Sa syntaxe moderne, inspirée de Python 3.6+ (annotations de types), permet d'écrire du code lisible, concis et maintenable.
- **Documentation automatique** : FastAPI génère automatiquement une documentation interactive (Swagger/OpenAPI) pour tous les endpoints, ce qui facilite les tests et la collaboration.
- **Validation des données** : Grâce à Pydantic, FastAPI valide automatiquement les entrées et sorties, réduisant les bugs et les erreurs de saisie.
- **Support natif de l'asynchrone** : Idéal pour gérer de nombreuses requêtes simultanées, ce qui est crucial pour une API exposée à des accès multiples (ex : dashboard, frontend, etc.).
- **Communauté et écosystème** : FastAPI bénéficie d'une communauté active et d'une excellente documentation.

### Pourquoi avoir utilisé les autres technologies/bibliothèques ?

#### **psycopg2**
- **Rôle** : Bibliothèque de connexion à PostgreSQL.
- **Pourquoi ?** : C'est le connecteur Python le plus robuste et performant pour interagir avec une base de données PostgreSQL. Il permet la gestion fine des transactions et la mise en place d'un pool de connexions pour optimiser les performances.

#### **dotenv**
- **Rôle** : Gestion des variables d'environnement.
- **Pourquoi ?** : Permet de stocker les informations sensibles (identifiants, mots de passe, etc.) dans un fichier `.env` non versionné, séparant ainsi la configuration du code source et renforçant la sécurité.

#### **Uvicorn**
- **Rôle** : Serveur ASGI pour exécuter l'application FastAPI.
- **Pourquoi ?** : Uvicorn est léger, rapide et parfaitement adapté à FastAPI. Il gère l'asynchrone et permet le hot-reload en développement.

#### **CORS Middleware**
- **Rôle** : Sécurisation des échanges entre le backend et le frontend.
- **Pourquoi ?** : Permet de contrôler les origines autorisées à accéder à l'API, évitant ainsi les problèmes de sécurité liés au cross-origin.

---

## ⚙️ Installation

1. **Cloner le dépôt**
2. **Créer un fichier `.env`** avec :
   ```env
   user=VOTRE_USER
   password=VOTRE_MDP
   host=VOTRE_HOST
   port=VOTRE_PORT
   dbname=VOTRE_DB
   ```
3. **Installer les dépendances**
   ```bash
   pip install -r requirements.txt
   ```
4. **Lancer le serveur**
   ```bash
   uvicorn main:app --reload
   ```

---

## 📊 Endpoints Principaux

| Métrique                                 | Endpoint                        | Description                                      |
|-------------------------------------------|---------------------------------|--------------------------------------------------|
| Nombre de médecins par département        | `/api/medecins_dep`             | Liste des départements et effectifs               |
| Moyenne des passages par département      | `/api/passages`                 | Activité médicale régionale                       |
| Part des médecins de plus de 55 ans       | `/api/part-medecins-sup-55`     | Vieillissement de la profession                   |
| Médecins retraités encore actifs          | `/api/medecins-retraites-actifs`| Anticipation des besoins de renouvellement        |
| APL par département                       | `/api/apl-dep`                   | Analyse des incitations à l'installation          |
| Test de connexion à la base               | `/api/test-db`                   | Vérification de la connexion et des données       |

---

## 🔒 Sécurité

- Variables sensibles dans `.env`
- CORS configuré pour le frontend
- Pool de connexions PostgreSQL

---

## 📚 Documentation interactive

Une fois le serveur lancé, accédez à la documentation Swagger :

- [http://localhost:8000/docs](http://localhost:8000/docs)

---

## 👨‍💻 Auteur & Contact

- [Votre nom / équipe]
- Projet pédagogique - [Nom de l'enseignant] 