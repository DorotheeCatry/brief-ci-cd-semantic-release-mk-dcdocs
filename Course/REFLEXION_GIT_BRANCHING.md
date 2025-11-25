# Réflexion : Stratégie de Branches et Conventional Commits

## 1. Pourquoi protéger les branches ?

La protection des branches (Branch Protection Rules) est un mécanisme de sécurité essentiel dans les plateformes comme GitHub ou GitLab.

**Que se passerait-il sans protection ?**
- **Code cassé en production** : N'importe qui pourrait pousser du code non testé ou buggé directement sur `main`, brisant potentiellement l'application pour tous les utilisateurs.
- **Historique chaotique** : Des `git push --force` accidentels pourraient réécrire l'historique, supprimant des commits importants et désynchronisant l'équipe.
- **Perte de traçabilité** : Sans obligation de passer par une Pull Request (PR), il n'y a pas de trace de "qui a validé quoi et pourquoi", rendant les audits impossibles.
- **Échec des standards** : Le code pourrait être mergé sans passer les tests (CI), sans linting, ou sans revue de code, accumulant ainsi de la dette technique.

## 2. Pourquoi Conventional Commits ?

**Conventional Commits** impose une structure stricte aux messages de commit (ex: `feat(api): add user login`).

**Avantages pour l'équipe**
- **Lisibilité** : L'historique Git devient un document lisible. On comprend instantanément la nature d'un changement (`fix`, `feat`, `chore`) sans lire le code.
- **Navigation** : Il est plus facile de filtrer l'historique pour retrouver quand une fonctionnalité a été ajoutée ou un bug corrigé.
- **Discipline** : Encourage les développeurs à faire des commits atomiques (un commit = une tâche précise) pour respecter le format.

**Avantages pour le versionnage automatique**
- **Automatisation totale** : C'est la clé de voûte du déploiement continu. Des outils comme `semantic-release` analysent les types de commits pour déterminer automatiquement le prochain numéro de version :
  - `fix` → Patch (1.0.0 → 1.0.1)
  - `feat` → Minor (1.0.0 → 1.1.0)
  - `BREAKING CHANGE` → Major (1.0.0 → 2.0.0)
- **Génération de Changelog** : Le changelog est généré automatiquement en regroupant les commits par catégorie, épargnant une tâche fastidieuse et sujette aux erreurs humaines.

## 3. Différence entre develop et main ?

Dans une stratégie GitFlow (ou simplifiée) :

- **main (ou master)** :
  - Représente l'état **stable** et **déployable** de la production.
  - On ne merge dessus que lorsque le code a été validé et qu'on est prêt à livrer une nouvelle version aux utilisateurs.
  - C'est la source de vérité pour les releases.

- **develop** :
  - Est la branche d'**intégration**. C'est le "brouillon avancé" de la prochaine version.
  - Elle contient les dernières fonctionnalités terminées par les développeurs, mais qui n'ont pas encore été releasées en production.
  - C'est ici que les développeurs mergent leurs `feature branches`.

**Quand merger dans develop ?**
- Dès qu'une fonctionnalité (`feature`) ou un correctif (`fix`) est terminé, testé localement, et que la Pull Request a été validée par les pairs et la CI.
- Cela permet de vérifier que la nouvelle fonctionnalité s'intègre bien avec le travail des autres.

**Quand merger dans main ?**
- Lorsqu'on décide de **publier une nouvelle version** (Release).
- Une fois que `develop` contient un ensemble cohérent de fonctionnalités et a passé tous les tests de non-régression (parfois via une branche `release/*`), on merge `develop` vers `main`.
- Ce merge déclenche généralement le pipeline de déploiement en production.
