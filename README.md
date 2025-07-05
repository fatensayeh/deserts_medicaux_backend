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

Pour configurer un environnement virtuel Python pour ce projet, vous pouvez suivre ce tutoriel (en anglais) :

[Setting up Python project with venv (virtual environment)](https://medium.com/@yashpatel007/setting-up-python-project-with-venv-virtual-environment-3a6a8575170c)

### Démarrage rapide

1. **Se déplacer dans le dépot**
   ```bash
   cd <path-to-folder>
   ```
2. **Créer un environnement virtuel :**
   ```bash
   python3 -m venv venv
   ```
3. **Activer l'environnement virtuel :**
   - Sur macOS/Linux :
     ```bash
     source venv/bin/activate
     ```
   - Sur Windows :
     ```cmd
     venv\Scripts\activate
     ```
4. **Créer un fichier `.env`** avec :
   ```env
   user=VOTRE_USER
   password=VOTRE_MDP
   host=VOTRE_HOST
   port=VOTRE_PORT
   dbname=VOTRE_DB
   ```
5. **Installer les dépendances :**
   ```bash
   pip install -r requirements.txt
   ```
6. **Lancer le serveur :**
   ```bash
   uvicorn main:app --reload
   ```

Pour plus de détails, consultez le tutoriel ci-dessus.

---

## 🗄️ Base de données : deux options possibles

Vous pouvez choisir entre :

- **Utiliser une base de données MySQL hébergée** : renseignez les informations de connexion dans le fichier `.env`. Vous pouvez demander aux étudiants les identifiants nécessaires pour accéder à leur base déjà hébergée.
- **Ou importer le fichier d'export SQL fourni** `mysql_export.sql` dans votre propre instance MySQL, puis compléter le fichier `.env` avec vos paramètres locaux (utilisateur, mot de passe, etc.).

Assurez-vous que le schéma de la base correspond bien à celui attendu par l'application.

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

- Faten Ikram Sayeh, Meriem Zoughbi , Dieu-Donné Fianko
- Projet pédagogique - Mélanie COURTINE