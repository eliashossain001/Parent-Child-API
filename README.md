# Parent-Child-API

This is a simple REST API for managing parent and child information. It is built using the Django and Django Rest Framework.

# Installation

1. Clone the repository to your local machine: <br>

```
https://github.com/eliashossain001/Parent-Child-API.git
```

2. Install the dependencies: <br>

```
pip install -r requirements.txt

```

3. Create the database: <br>

```
python manage.py migrate
```

4. Create a superuser account: <br>

```
python manage.py createsuperuser

```

5. Run the development server:: <br>

```
python manage.py runserver

```
The API endpoint will look like this: http://localhost:8000/.

# Endpoints
## Parents

* GET /parents/ - Returns a list of all parents.
* POST /parents/ - Creates a new parent.

## Children

* GET /children/ - Returns a list of all children.
* POST /children/ - Creates a new child.
* GET /children/{id}/ - Returns the details of a specific child.
* PUT /children/{id}/ - Updates the details of a specific child.
* DELETE /children/{id}/ - Deletes a specific child.

# Testing

To run the tests, use the following command:

```
python manage.py test

```

This will run the test suite and output the results in the console.

# Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
