# Studious Octo Goggles

## Overview

Studious Octo Goggles is a Django application that runs locally using Docker.

## Prerequisites

Before getting started, ensure the following tools are installed:

- Docker Desktop: https://www.docker.com/products/docker-desktop/
- Git: https://git-scm.com/downloads
- pre-commit: https://pre-commit.com/#install

### Install pre-commit (macOS)

If you're using Homebrew:

```bash
brew install pre-commit
```

## Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/klhenams/studious-octo-goggles.git
cd studious-octo-goggles
```

### 2. Install Git Hooks

Install the pre-commit hooks used by the project:

```bash
pre-commit install
```

### 3. Build Docker Images

```bash
docker compose -f docker-compose.local.yml build
```

### 4. Start the Development Environment

```bash
docker compose -f docker-compose.local.yml up
```

To run the services in the background:

```bash
docker compose -f docker-compose.local.yml up -d
```

### 5. Apply Database Migrations

In a new terminal window:

```bash
docker compose -f docker-compose.local.yml run --rm django python manage.py migrate
```

### 6. Create a Superuser (Optional)

If you need access to the Django admin site:

```bash
docker compose -f docker-compose.local.yml run --rm django python manage.py createsuperuser
```

### 7. Load Incident Report Fixtures (Optional)

A sample fixture set with 15 incident reports is available for local development:

```bash
docker compose -f docker-compose.local.yml run --rm django python manage.py loaddata incident_reports
```

### 8. Access the Application

Once the containers are running, open:

```
http://localhost:8000
```

## Common Management Commands

### Create New Migrations

```bash
docker compose -f docker-compose.local.yml run --rm django python manage.py makemigrations
```

### Apply Migrations

```bash
docker compose -f docker-compose.local.yml run --rm django python manage.py migrate
```

### Run Tests

```bash
docker compose -f docker-compose.local.yml run --rm django pytest
```

### Open a Django Shell

```bash
docker compose -f docker-compose.local.yml run --rm django python manage.py shell
```

### Stop the Development Environment

```bash
docker compose -f docker-compose.local.yml down
```

## Code Quality

Run all pre-commit checks manually:

```bash
pre-commit run --all-files
```
