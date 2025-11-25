# Problèmes Détectés

Ce document recense les problèmes de qualité, de sécurité et de configuration identifiés lors de l'audit du code source.

## 🎨 Formatage et Style

- **Lignes trop longues** :
  - `app/main.py` : La variable `very_long_variable_name_that_exceeds_line_length` dépasse la limite standard de 88/79 caractères.
- **Imports non utilisés** :
  - `app/main.py` : `sys`, `json`, `Dict`, `Any` sont importés mais jamais utilisés.
- **Variables inutilisées** :
  - `app/main.py` : `UNUSED_VAR` est définie mais jamais utilisée.

## 🔒 Sécurité

- **Secrets en dur (Hardcoded Secrets)** :
  - `app/main.py` : Variable `secret` contient une clé secrète en clair.
  - `app/main.py` : Variable `API_KEY` contient une clé API en clair.
  - `app/database.py` : L'URL de connexion par défaut contient un mot de passe (`postgres:postgres`).
- **Dépendances** :
  - Pas de vérification de vulnérabilités des dépendances configurée.

## 🏷️ Typage (Type Hints)

- **Manque de types explicites** :
  - `app/routes/items.py` :
    - Fonction `get_item` : paramètre `item_id` non typé.
    - Fonction `create_item` : paramètres `item_data` et `db` non typés.

## 📝 Documentation

- **Docstrings manquantes** :
  - `app/main.py` : Pas de docstring de module.
  - `app/models/item.py` : Pas de docstring pour la classe `Item`.
  - `app/schemas/item.py` : Pas de docstring pour les classes `ItemBase`, `ItemCreate`, `ItemUpdate`, `ItemResponse`.

## ♻️ Code Mort (Dead Code)

- **Fonctions inutilisées** :
  - `app/routes/items.py` : Fonction `_old_helper_function` n'est jamais appelée.
  - `app/models/item.py` : Méthode `_legacy_method` n'est jamais utilisée.

## 🏗️ CI/CD et Configuration

- **Absence de Pipeline CI/CD** :
  - Le dossier `.github/workflows` est manquant. Aucune automatisation pour les tests, le linting ou le déploiement.
- **Tests manquants** :
  - Le dossier `tests/` est vide (contient uniquement `.gitkeep`). Aucun test unitaire ou d'intégration n'est présent.
- **Configuration des outils manquante** :
  - `pyproject.toml` ne contient pas de configuration pour les outils de qualité (Ruff, Mypy, Pytest).

---

## ❓ Questions de réflexion

### 1. Le code fonctionne, mais...

- **Est-il maintenable ?**
  - **Non.** L'absence de tests automatisés rend toute modification périlleuse (risque de régression non détecté). La présence de code mort et de variables inutilisées complexifie la lecture et la compréhension du code. Le manque de typage strict (type hints) empêche de comprendre rapidement les structures de données attendues.

- **Est-il sécurisé ?**
  - **Non.** La présence de secrets en dur (clés API, mots de passe) dans le code source est une faille critique (risque de fuite si le code est partagé). L'absence de scan de vulnérabilités sur les dépendances expose le projet à des failles connues.

- **Est-il bien documenté ?**
  - **Non.** De nombreuses classes et fonctions manquent de docstrings. Il est difficile pour un nouveau développeur de comprendre l'intention du code sans devoir lire l'implémentation en détail.

### 2. Comment détecter ces problèmes automatiquement ?

- **Quels outils utiliser ?**
  - **Linting & Formatage** : `Ruff` (pour remplacer Flake8, Black, Isort) afin d'assurer un style de code cohérent et nettoyer les imports/variables inutilisés.
  - **Typage** : `Mypy` pour vérifier la cohérence des types et éviter les erreurs à l'exécution.
  - **Sécurité** : `Bandit` (analyse statique du code) et `Safety` (analyse des dépendances).
  - **Tests** : `Pytest` pour exécuter les tests unitaires et d'intégration.

- **À quel moment les exécuter ?**
  - **En local (Pre-commit)** : Utiliser des `pre-commit hooks` pour empêcher le commit de code ne respectant pas les standards.
  - **Dans la CI (Continuous Integration)** : À chaque `push` et chaque `Pull Request`, une pipeline (GitHub Actions) doit exécuter tous ces outils. Si une étape échoue, la PR ne doit pas pouvoir être mergée.

### 3. Comment empêcher ces problèmes à l'avenir ?

- **Automatisation (CI/CD)** : Mettre en place un pipeline CI complet qui joue le rôle de "gardien" de la qualité.
- **Protection des branches** : Configurer GitHub pour interdire le push direct sur `main` et `develop`, et obliger le passage par des Pull Requests validées par la CI.
- **Revue de code (Code Review)** : Instaurer une culture de relecture obligatoire où les pairs valident la pertinence fonctionnelle et la clarté du code.
- **Standardisation** : Utiliser des outils comme `uv` et `semantic-release` pour standardiser la gestion des dépendances et le versionnage.
