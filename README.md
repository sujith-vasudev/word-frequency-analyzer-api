# 🔧 Application Setup & Configuration Guide

## Environment Configuration

The application relies on several environment variables for database and security configurations. Below are the variables along with their default values (used if not explicitly set):

| Variable         | Description                             | Default Value                                                |
|------------------|-----------------------------------------|--------------------------------------------------------------|
| `DB_CLIENT`      | SQLAlchemy-compatible DB driver         | `postgresql+psycopg2`                                        |
| `DB_USER`        | Database username                       | `root`                                                       |
| `DB_PASS`        | Database password                       | `root`                                                       |
| `DB_HOST`        | Database host (Docker or localhost)     | `localhost`                                                  |
| `DB_PORT`        | Port the database listens on            | `5432`                                                       |
| `DB_NAME`        | Target database name                    | `demo`                                                       |
| `SECRET_KEY`     | Used for JWT token encryption           | `SECRET_KEY`                                                 |
| `PASSWORD_SALT`  | Used to salt hashed passwords securely  | `$2b$12$dETsd4Az4kmHd4Plf8WeLOhHsv5k0ZtVRILphMAv.LArX4tU5H6eK` |

---

## Database Dependencies

Ensure the database name given in the environment variable is created before running the application.


psql -U root


CREATE DATABASE demo;

---

## Library Dependencies

Ensure all required dependencies are installed before running the application.

**Install via pip**:

```bash
pip install -r requirements.txt
