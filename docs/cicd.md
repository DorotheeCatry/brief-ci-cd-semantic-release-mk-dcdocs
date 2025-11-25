# CI/CD Pipeline

Ce projet utilise GitHub Actions pour l'intégration et le déploiement continus.

## Workflow CI

Le workflow `ci.yml` s'exécute sur chaque push et pull request vers `main` et `develop`.

### Jobs
1. **Lint**: Vérifie le style du code avec Ruff.
2. **Typecheck**: Vérifie les types avec Mypy.
3. **Security**: Scanne les vulnérabilités avec Bandit et Safety.
4. **Tests**: Exécute les tests unitaires avec Pytest.
5. **Docker**: Construit et push l'image Docker sur GHCR (si les tests passent).

## Semantic Release

Le workflow `release.yml` gère automatiquement les versions et les releases GitHub.
Il est déclenché après le succès du workflow CI sur la branche `main`.
