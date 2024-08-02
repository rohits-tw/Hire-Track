# Hire-Track

This is a Django application designed to manage hiring processes. It utilizes PostgreSQL as the database and Redis for caching. The application can be run using Docker or without Docker.

**Running with Docker**

1. Ensure Docker and Docker Compose are installed on your system.
2. Clone the repository: `git clone https://github.com/rohits-tw/Hire-Track.git`
3. Navigate to the project directory: `cd hire-track`
4. Build and start the application: `sudo docker-compose up`
5. The application will be available at `http://localhost:8000`

**Running without Docker**

1. Ensure Python 3.8 or higher is installed on your system.
2. Clone the repository: `git clone https://github.com/rohits-tw/Hire-Track.git`
3. Navigate to the project directory: `cd hire-track`
4. Create and activate a virtual environment: `python -m venv venv` and `source venv/bin/activate` (on Linux/Mac) or `python -m venv venv` and `venv\Scripts\activate` (on Windows)
5. Install the required packages: `pip install -r requirements.txt`
6. Apply migrations: `python manage.py migrate`
7. Start the application: `python manage.py runserver`
8. The application will be available at `http://localhost:8000`

**Database and Redis Setup**

For running without Docker, you need to have PostgreSQL and Redis installed on your system. You can install them using your system's package manager or by following the official installation guides.

**Environment Variables**

For running without Docker, you need to set environment variables for the database and Redis. You can do this by creating a `.env` file in the project directory with the following content:
```
DATABASE=postgres
POSTGRES_DB=Hiretrackdb
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
```
Replace the values with your actual database credentials.

**Troubleshooting**

If you encounter any issues during the setup or running of the application, refer to the Docker and Django documentation for troubleshooting guides.
