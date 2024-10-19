# Django-machine-test
This project is designed to showcase the completion of the Django machine test. It involves designing REST APIs for managing entities like Users, Clients, and Projects. The system includes many users and clients, where clients can have multiple projects, and projects can be assigned to many users.

## Django Machine Test Project
- How to Run the Machine
- Database Design
- How to Run the Code
- Contributing 


### How to Run the MAchine
To run the Django project locally, follow these steps:
Install Dependencies

##### Step 1: Clone the Repository
First, clone the repository from GitHub to your local system:
git clone https://github.com/nehapatil3071/Django-machine-test.git
Navigate into the project directory:
```python
cd Django-machine-test
```

##### Step 2: Set Up the Virtual Environment
It's recommended to run the project inside a virtual environment. Set up the virtual environment using the following commands:
```python
python -m venv env
.\env\Scripts\activate
```


##### Step 3: Install Dependencies
Install the required dependencies from requirements.txt:
```python
pip install -r requirements.txt
```


##### Step 4: Set Up the Database
Make sure you have MySQL installed and running. Update your database credentials in the Django project’s settings. Then, run the following commands to set up the database:
```python
python manage.py makemigrations
python manage.py migrate
```


##### Step 6: Run the Server
To start the Django development server, use the command:
```python
python manage.py runserver
```

Now, the server should be running at http://127.0.0.1:8000/.

### Database Design
Download from MySQL Official Site
Create a new database for your project
Configure Django to Connect to MySQL: In your settings.py file, add your database configuration
The database design includes three main entities:

1.User: Represents the users of the system. Users are managed via Django's default admin system.
2.Client: Represents the clients in the system. A client can have many projects.
3.Project: Represents the projects associated with a client and assigned to multiple users.

The relationships between the entities:
  A Client can have multiple Projects.
  A Project can be assigned to multiple Users.
  
#### Database Tables
1.User Table:
Managed by Django's default user model.

2.Client Table:
Fields: id, client_name, created_by, created_at, updated_at

3.Project Table:
Fields: id, project_name, client_id, created_by, created_at, updated_at
Foreign keys: client_id (linked to Client), users (many-to-many relationship with User)

#### Migrate the Database
Now, run the migrations to set up your database schema:
#### Apply Django migrations
```python
python manage.py makemigrations
python manage.py migrate
```

### How to Run the Code
##### Testing the API Endpoints
Here’s how you can interact with the API endpoints.

1. Register a Client:
Endpoint: POST /clients/

3. Fetch Client Info:
Endpoint: GET /clients/

5. Edit/Delete Client Info:
Edit:
Endpoint: PUT /clients/{id}/

4.Delete:
Endpoint: DELETE /clients/{id}/
Response: HTTP 204 No Content

7. Add New Project for a Client:
Endpoint: POST /clients/{id}/projects/

9. Retrieve Assigned Projects for Logged-In User:
Endpoint: GET /projects/

#### Contributing
Feel free to fork this repository, make any changes, and submit a pull request. Make sure to pull the latest changes from the main branch before submitting any updates to avoid conflicts.

