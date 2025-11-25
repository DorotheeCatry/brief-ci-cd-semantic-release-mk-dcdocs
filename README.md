# Items CRUD API

![CI Status](https://github.com/DorotheeCatry/brief-ci-cd-semantic-release-mk-dcdocs/actions/workflows/ci.yml/badge.svg)
![Python Version](https://img.shields.io/badge/python-3.13-blue.svg)
![Code Style](https://img.shields.io/badge/code%20style-ruff-000000.svg)

A robust REST API for managing items, built with **FastAPI**, **SQLModel**, and **PostgreSQL**. This project demonstrates a professional CI/CD pipeline using GitHub Actions, Semantic Release, and Docker.

## Features

- **CRUD Operations**: Create, Read, Update, Delete items.
- **Database**: PostgreSQL integration using SQLModel (SQLAlchemy + Pydantic).
- **CI/CD**: Automated testing, linting, security checks, and release management.
- **Quality**: Type checking (Mypy), Linting/Formatting (Ruff), Security (Bandit, Safety).
- **Containerization**: Docker and Docker Compose support.

## Prerequisites

- Python 3.13+
- [uv](https://github.com/astral-sh/uv) (for dependency management)
- Docker & Docker Compose (optional, for containerized run)

## Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/DorotheeCatry/brief-ci-cd-semantic-release-mk-dcdocs.git
   cd brief-ci-cd-semantic-release-mk-dcdocs
   ```

2. **Install dependencies**
   ```bash
   uv sync
   ```

3. **Set up pre-commit hooks**
   ```bash
   uv run pre-commit install
   ```

## Usage

### Running Locally

1. **Start the database** (if using local Postgres) or use Docker Compose (see below).

2. **Run the application**
   ```bash
   uv run fastapi dev app/main.py
   ```
   The API will be available at `http://127.0.0.1:8000`.
   Interactive docs: `http://127.0.0.1:8000/docs`.

### Running with Docker Compose

```bash
docker-compose up --build
```

### Running Tests

```bash
uv run pytest
```

## CI/CD Pipeline

The project uses GitHub Actions for Continuous Integration:
- **Linting**: Ruff
- **Type Checking**: Mypy
- **Security**: Bandit, Safety
- **Tests**: Pytest

Releases are managed automatically by **Semantic Release** based on commit messages.

## License

This project is licensed under the MIT License.
