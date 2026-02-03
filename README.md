# FastAPI Model Server Skeleton

## Overview

This project provides a **production-ready FastAPI skeleton** for serving machine learning models in a fast, secure, and scalable way. It is designed to help developers and teams quickly bootstrap machine learning APIs without having to build common infrastructure from scratch.

Powered by **FastAPI**, created by [Sebastián Ramírez](https://github.com/tiangolo), this skeleton follows modern best practices for backend development, including clean architecture, dependency injection, environment-based configuration, and strong typing.

The repository is suitable for **commercial and enterprise use**, and can be easily adapted for startups, SaaS platforms, internal tools, or customer-facing ML services.

---

## Key Features

-  **High-performance API** based on FastAPI and ASGI
-  **API key authentication** for securing endpoints
-  **Modular project structure** for easy extensibility
-  **Full test coverage** with pytest and tox
-  **Code quality tools**: black, flake8, mypy, bandit, isort
-  **Poetry-based dependency management**
-  **Production-ready structure**, easy to containerize with Docker
-  **Pydantic v2** schemas for data validation
-  Designed for **machine learning model serving**

---

## Included Example Model

To demonstrate how the skeleton can be used in practice, the project includes a **sample regression model for house price prediction**.

This example allows you to:
- Understand how ML models are loaded and used
- Test request/response validation
- Experiment with real API calls
- Extend the example with your own models

The sample model is exposed through a **RESTful API endpoint**, making it easy to integrate with frontend applications, mobile apps, or other backend services.

---

## Project Structure

The repository follows a clean and maintainable structure:



## Requirements

- Python 3.11+
- Poetry

## Installation
Install the required packages in your local environment (ideally virtualenv, conda, etc.).

```bash
poetry install
``` 


## Setup
1. Duplicate the `.env.example` file and rename it to `.env` 


2. In the `.env` file configure the `API_KEY` entry. The key is used for authenticating our API. <br>
   A sample API key can be generated using Python REPL:

```python
import uuid
print(str(uuid.uuid4()))
```

## Run It

1. Start your  app with:

```bash
set -a
source .env
set +a
uvicorn fastapi_skeleton.main:app
```

2. Go to [http://localhost:8000/docs](http://localhost:8000/docs).
3. Click `Authorize` and enter the API key as created in the Setup step.
![Authroization] 
4. You can use the sample payload from the `docs/sample_payload.json` file when trying out the house price prediction model using the API.
   ![Prediction with example payload]

## Linting

This skeleton code uses isort, mypy, flake, black, bandit for linting, formatting and static analysis.

Run linting with:

```bash
./scripts/linting.sh
```

## Run Tests

Run your tests with:

```bash
./scripts/test.sh
```

This runs tests and coverage for Python 3.11 and Flake8, Autopep8, Bandit.


## Changelog

v.1.0.0 - Initial release

- Base functionality for using FastAPI to serve ML models.
- Full test coverage 

v.1.1.0 - Update to Python 3.11, FastAPI 0.108.0

- Updated to Python 3.11
- Added linting script
- Updated to pydantic 2.x
- Added poetry as package manager
