# studious-octo-goggles

## Prerequisites

Before getting started, make sure you have the following installed:

- Docker Desktop: https://www.docker.com/products/docker-desktop/
- Git: https://git-scm.com/downloads
- pre-commit: https://pre-commit.com/#install

If you use Homebrew on macOS, you can install pre-commit with:

```bash
brew install pre-commit
```

## Getting Started

1. Clone the repository:

   ```bash
   git clone https://github.com/klhenams/studious-octo-goggles.git
   cd studious_octo_goggles
   ```

2. Install and set up pre-commit hooks locally:

   ```bash
   pre-commit install
   ```

3. Build the Docker images:

   ```bash
   docker compose -f docker-compose.local.yml build
   ```

4. Start the local environment with Docker:

   ```bash
   docker compose -f docker-compose.local.yml up
   ```

5. Access the application in your browser at http://localhost:8000

6. If you need a superuser account, run:

   ```bash
   docker compose -f docker-compose.local.yml exec django python manage.py createsuperuser
   ```
