# REST API with PostgreSQL

This project implements a REST API that interacts with a PostgreSQL database. It covers the basic functionality of CRUD 
operations along with database migrations, data population, and more.


## Technologies Used

- FastAPI for building the REST API
- SQLAlchemy for ORM and database interaction
- Alembic for database migrations
- PostgreSQL as the database engine


## Setup and Usage

### 1. Install Dependencies
Run the following script to install the required dependencies and set up a virtual environment:

```bash
./scripts/install_deps.sh
```

### 2. Start PostgreSQL
To run the PostgreSQL database in a Docker container, execute:

```bash
./scripts/start_postgres.sh
```

### 3. Load Database Schema
Once the database container is running, load the initial database tables by running:

```bash
path/to/venv/python load_tables.py
```

This will execute the SQL commands in `postgres/tables.sql` to create the necessary tables.

### 4. Run the FastAPI Application
Start the FastAPI application using `uvicorn`:

```bash
uvicorn app.main:app --reload
```

The API will be available at `http://127.0.0.1:8000`.

### 5. Populate the Database
You can populate the database with mock data by running:

```bash
path/to/venv/python populate_tables.py
```

This will make API calls to populate the tables with random data.
