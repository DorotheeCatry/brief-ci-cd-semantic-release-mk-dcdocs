# Démarrage Rapide

## Prérequis

- Python 3.13+
- [uv](https://github.com/astral-sh/uv)
- Docker & Docker Compose (optionnel)

## Installation

1. **Cloner le dépôt**
   ```bash
   git clone https://github.com/DorotheeCatry/brief-ci-cd-semantic-release-mk-dcdocs.git
   cd brief-ci-cd-semantic-release-mk-dcdocs
   ```

2. **Installer les dépendances**
   ```bash
   uv sync
   ```

3. **Lancer l'application**
   ```bash
   uv run fastapi dev app/main.py
   ```
