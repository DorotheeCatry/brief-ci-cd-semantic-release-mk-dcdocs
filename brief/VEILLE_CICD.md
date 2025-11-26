# Veille Technologique CI/CD

## Mission 1 : Comprendre CI/CD

### 1. Qu'est-ce que la CI (Continuous Integration) ?

La **Continuous Integration (CI)** ou Intégration Continue est une pratique de développement logiciel où les développeurs intègrent leur code dans un dépôt partagé (repository) fréquemment, souvent plusieurs fois par jour. Chaque intégration est vérifiée par une construction automatique (build) et des tests automatisés.

**Quels problèmes résout-elle ?**
- **"Integration Hell"** : Évite les conflits de fusion massifs et douloureux qui surviennent lorsque les développeurs travaillent isolément pendant de longues périodes.
- **Détection tardive des bugs** : Permet d'identifier les erreurs d'intégration et les régressions dès qu'elles sont introduites.
- **Code cassé** : Empêche que le code non fonctionnel ne pollue la branche principale.

**Quels sont les principes clés ?**
- **Dépôt unique** : Tout le code source est centralisé.
- **Automatisation du build** : La compilation et la création des artefacts sont automatisées.
- **Tests automatisés** : Des tests unitaires et d'intégration sont exécutés à chaque changement.
- **Intégration fréquente** : Les développeurs committent leur code au moins une fois par jour.
- **Feedback rapide** : L'équipe est immédiatement notifiée en cas d'échec.

**3 exemples d'outils de CI :**
1. **GitHub Actions**
2. **GitLab CI**
3. **Jenkins**

### 2. Qu'est-ce que le CD (Continuous Deployment/Delivery) ?

Le **CD** fait référence à deux concepts liés mais distincts : le **Continuous Delivery** (Livraison Continue) et le **Continuous Deployment** (Déploiement Continu). C'est l'étape qui suit la CI.

**Différence entre Continuous Delivery et Continuous Deployment ?**
- **Continuous Delivery (Livraison Continue)** : Le code est automatiquement construit, testé et préparé pour être déployé en production. Cependant, le déploiement final vers la production nécessite une **action manuelle** (clic sur un bouton). L'objectif est d'avoir un logiciel toujours "déployable".
- **Continuous Deployment (Déploiement Continu)** : Pousse l'automatisation un cran plus loin. Chaque changement qui passe toutes les étapes de la CI et des tests est **automatiquement déployé** en production, sans intervention humaine.

**Quels sont les risques et bénéfices ?**
- **Bénéfices** :
  - **Time-to-market réduit** : Les nouvelles fonctionnalités arrivent plus vite chez les utilisateurs.
  - **Boucles de feedback plus courtes** : Les retours utilisateurs sont obtenus rapidement.
  - **Réduction du stress** : Les déploiements deviennent des non-événements fréquents et routiniers plutôt que des mises en production massives et risquées.
- **Risques** :
  - **Stabilité** : Un bug non détecté par les tests automatisés peut impacter directement les utilisateurs en production (surtout en Déploiement Continu).
  - **Nécessité de tests robustes** : Exige une couverture de tests excellente et fiable ; sans cela, le risque de casser la production est élevé.

### 3. Pourquoi CI/CD est important ?

**Impact sur la qualité du code**
- La qualité augmente car les tests sont exécutés systématiquement.
- Les règles de linting et de formatage sont appliquées automatiquement, assurant une base de code propre et cohérente.
- Les régressions sont détectées immédiatement.

**Impact sur la vitesse de développement**
- Les développeurs passent moins de temps à débugger des problèmes d'intégration complexes ("merge hell").
- L'automatisation des tâches répétitives (build, tests, déploiement) libère du temps pour le développement de fonctionnalités.

**Impact sur la collaboration en équipe**
- Encourage la communication et la transparence (tout le monde voit l'état du projet).
- Responsabilise les développeurs (si le build casse, on le répare tout de suite).
- Facilite l'intégration des nouveaux arrivants grâce à des processus documentés et automatisés.

---

## Mission 2 : Maîtriser uv

### 1. Qu'est-ce que uv ?

**uv** est un gestionnaire de paquets et de projets Python extrêmement rapide, écrit en Rust. Il vise à remplacer `pip`, `pip-tools`, `poetry`, `pyenv`, `virtualenv`, et plus encore, en un seul outil unifié.

**En quoi est-ce différent de pip/poetry/pipenv ?**
- **Vitesse** : uv est conçu pour être 10 à 100 fois plus rapide que pip et poetry grâce à son implémentation en Rust et à son système de cache global intelligent.
- **Tout-en-un** : Contrairement à pip qui ne gère que l'installation, ou pyenv qui ne gère que les versions de Python, uv gère tout : l'installation de Python, la création d'environnements virtuels, la résolution de dépendances, et l'exécution de scripts.
- **Compatibilité** : Il utilise des standards modernes (pyproject.toml) mais reste compatible avec les workflows existants.

**Quels sont les avantages ?**
- **Performance** : Les temps d'installation et de résolution sont drastiquement réduits.
- **Déterminisme** : Utilise un fichier de verrouillage (`uv.lock`) universel pour garantir des installations reproductibles sur toutes les plateformes.
- **Espace disque** : Utilise un cache global avec hardlinks, réduisant l'espace disque utilisé par les environnements virtuels multiples.

### 2. Comment uv fonctionne avec pyproject.toml ?

**Structure du fichier**
Le fichier `pyproject.toml` est le standard pour la configuration des projets Python. uv l'utilise pour définir les métadonnées du projet et ses dépendances.

```toml
[project]
name = "mon-projet"
version = "0.1.0"
requires-python = ">=3.12"
dependencies = [
    "fastapi>=0.109.0",
]

[tool.uv]
dev-dependencies = [
    "pytest>=8.0.0",
    "ruff>=0.3.0",
]
```

**Gestion des dépendances (séparé par sections)**
- **[project.dependencies]** : Contient les dépendances de production nécessaires pour exécuter l'application.
- **[tool.uv.dev-dependencies]** (ou `dependency-groups` dans les versions récentes) : Contient les outils de développement (tests, linter, formatage) qui ne sont pas nécessaires en production.

**Build backend**
uv supporte les standards de build (PEP 517). Il peut utiliser `hatchling`, `setuptools` ou d'autres backends pour construire le paquet distribuable (wheel/sdist).

### 3. Comment utiliser uv dans GitHub Actions ?

**Installation**
L'action officielle `astral-sh/setup-uv` facilite l'installation dans la CI.

```yaml
- name: Install uv
  uses: astral-sh/setup-uv@v3
```

**Cache des dépendances**
L'action gère automatiquement le cache pour accélérer les builds suivants.

```yaml
- name: Install uv
  uses: astral-sh/setup-uv@v3
  with:
    enable-cache: true
```

**Exécution de commandes**
Au lieu d'activer manuellement un environnement virtuel, on utilise `uv run` pour exécuter des commandes dans l'environnement du projet.

```yaml
- name: Run tests
  run: uv run pytest

- name: Lint code
  run: uv run ruff check .
```

---

## Mission 3 : Comprendre Semantic Release

### 1. Qu'est-ce que le versionnage sémantique (SemVer) ?

Le **Semantic Versioning (SemVer)** est une convention de gestion des numéros de version logicielle qui donne du sens aux numéros de version.

**Format MAJOR.MINOR.PATCH**
Un numéro de version est composé de trois nombres séparés par des points : `X.Y.Z` (ex: `1.2.3`).
- **MAJOR (X)** : Version majeure.
- **MINOR (Y)** : Version mineure.
- **PATCH (Z)** : Version de correctif.

**Quand bumper chaque niveau ?**
- **MAJOR** : Quand vous faites des changements **incompatibles** avec l'API précédente (Breaking Changes).
- **MINOR** : Quand vous ajoutez des fonctionnalités de manière **rétro-compatible** (nouvelles features).
- **PATCH** : Quand vous faites des corrections de bugs **rétro-compatibles** (bug fixes).

### 2. Qu'est-ce que Conventional Commits ?

**Conventional Commits** est une spécification pour formater les messages de commit de manière standardisée et lisible par les machines. Cela permet d'automatiser la génération de changelogs et le versionnage sémantique.

**Format des messages**
```
<type>(<scope>): <description>

[corps optionnel]

[footer optionnel]
```
Exemple : `feat(auth): add login endpoint`

**Types de commits (feat, fix, etc.)**
- `feat` : Nouvelle fonctionnalité (déclenche un bump **MINOR**).
- `fix` : Correction de bug (déclenche un bump **PATCH**).
- `BREAKING CHANGE` (dans le footer ou avec `!`) : Changement majeur (déclenche un bump **MAJOR**).
- Autres types (ne déclenchent généralement pas de release) : `docs`, `style`, `refactor`, `perf`, `test`, `chore`, `ci`.

**Impact sur le versionnage**
Les outils d'analyse (comme semantic-release) lisent l'historique des commits depuis la dernière version.
- S'il y a au moins un `BREAKING CHANGE` → Nouvelle version **MAJOR**.
- Sinon, s'il y a au moins un `feat` → Nouvelle version **MINOR**.
- Sinon, s'il y a au moins un `fix` → Nouvelle version **PATCH**.

### 3. Comment python-semantic-release fonctionne ?

**Configuration dans pyproject.toml**
On configure l'outil pour qu'il sache où trouver la version actuelle (souvent dans `pyproject.toml` ou `__init__.py`) et comment commiter les changements.

```toml
[tool.semantic_release]
version_variable = [
    "app/__init__.py:__version__",
    "pyproject.toml:version"
]
branch = "main"
upload_to_pypi = false
upload_to_release = true
build_command = "uv build"
```

**Génération du CHANGELOG**
L'outil analyse tous les commits depuis la dernière release. Il groupe les commits par type (`Features`, `Bug Fixes`, etc.) et génère un fichier `CHANGELOG.md` (ou met à jour l'existant) avec la liste des changements, les auteurs et les liens vers les commits.

**Création des releases GitHub**
Une fois la nouvelle version déterminée et le changelog généré :
1. Il met à jour le fichier de version.
2. Il commite ces changements.
3. Il crée un tag Git (ex: `v1.2.0`).
4. Il pousse le tout sur GitHub.
5. Il crée une **Release GitHub** officielle contenant le changelog et les artefacts de build (si configuré).

---

## Mission 5 : MkDocs & GitHub Pages (Bonus)

### 1. Comment MkDocs génère de la documentation ?

**MkDocs** est un générateur de site statique rapide et simple, orienté vers la documentation de projet.
- **Source** : Il prend en entrée des fichiers Markdown (`.md`) situés généralement dans un dossier `docs/`.
- **Configuration** : Un fichier `mkdocs.yml` définit la structure du site (navigation), le thème, et les plugins.
- **Build** : Il convertit ces fichiers Markdown en fichiers HTML/CSS/JS statiques, prêts à être hébergés sur n'importe quel serveur web.

### 2. Comment déployer sur GitHub Pages ?

GitHub Pages est un service d'hébergement de sites statiques directement depuis un dépôt GitHub.
- **Branche `gh-pages`** : Traditionnellement, MkDocs construit le site et pousse les fichiers HTML générés sur une branche orpheline nommée `gh-pages`.
- **Automatisation** : Avec GitHub Actions, on peut automatiser ce processus à chaque push sur `main`.
  ```yaml
  - name: Deploy to GitHub Pages
    run: mkdocs gh-deploy --force
  ```
- **Configuration GitHub** : Dans les paramètres du dépôt (Pages), on indique que la source est la branche `gh-pages`.

### 3. Qu'est-ce que mkdocstrings ?

**mkdocstrings** est un plugin pour MkDocs qui permet de générer automatiquement de la documentation API à partir du code source (docstrings).
- **Auto-documentation** : Il lit les docstrings Python (Google style, NumPy style, etc.) directement dans le code.
- **Intégration** : Il injecte cette documentation dans les pages MkDocs.
- **Avantage** : Évite la duplication. La documentation du code reste dans le code, et le site de documentation est toujours à jour avec le code source.
