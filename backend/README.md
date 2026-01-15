# To run the backend

Ensure you are in the root of the backend directory,
Then run the following commands in the terminal:

### To get a python virtual environment for packages:

python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

### to run postgres inside the Docker container/start the database server:

docker compose up -d

### connect to the database server:

docker compose exec postgres psql -U postgres sproutlog

Once you are logged into psql. Use the following commands to create a database for this project, make it your current database, and then load in our table and sample data:

#### List all databases

postgres=# \l

#### Create a new database for this project

postgres=# create database <database name>;

#### Connect to our database

postgres=# \c <database name>

#### Load the database schema and any sql commands in the file data injection aka seed the database

<database name>=# \i <sql file path>;

#### list all tables

\dt

#### You can log out of your database with

exit

# Run the web server:

fastapi dev main.py

## In your browser, go to

http://localhost:8000/docs
