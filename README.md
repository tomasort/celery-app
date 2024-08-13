# Flask App with PostgreSQL and Docker

This repository serves as a template for setting up a simple Flask application with a PostgreSQL database using Docker and Docker Compose. It includes the necessary configurations to get you up and running quickly.

## Features

- **Flask:** A lightweight WSGI web application framework in Python.
- **PostgreSQL:** A powerful, open-source relational database system.
- **Docker:** Containerization of the Flask app and PostgreSQL database.
- **Docker Compose:** Simplifies the orchestration of multi-container Docker applications.

## Getting Started

### Prerequisites

Ensure you have the following installed on your machine:

- Docker
- Docker Compose

### Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/flask-postgres-docker.git
   cd flask-postgres-docker
   ```

2. **Build and run the containers**:
   ```bash
   docker-compose up --build
   ```

3. **Access the application**:
   - The Flask app will be accessible at `http://localhost:5000`.
   - PostgreSQL will be running on `localhost:5432`.

### Stopping the Application

To stop the application and remove the containers, run:

```bash
docker-compose down
```

### Database Migrations

If you need to apply database migrations, you can do so by:

1. Accessing the running Flask container:
   ```bash
   docker-compose exec web bash
   ```
2. Running the migration commands inside the container (e.g., using Flask-Migrate or Alembic).

## Customization

Feel free to customize the repository to suit your specific needs. You can add more Flask blueprints, configure environment variables, or integrate other services.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Acknowledgments

- [Flask](https://flask.palletsprojects.com/)
- [PostgreSQL](https://www.postgresql.org/)
- [Docker](https://www.docker.com/)