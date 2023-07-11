# fan-api-demo

# Development instructions
## prerequities
* Python 3.9+
* sqlite3
* docker or podman

## Recommended
* IDE such as VS Code or PyCharm


## Getting started
To get started with development, first clone this project to your development computer.

Example:
`git clone https://github.com/vandorjw/fan-api-demo.git`

Next, change into the project's main directory and populate your project's secrets by creating an .env file in the root of the project

The following are the minimum set of configurations that the project will require.
```
ALLOWED_HOSTS=*
SECRET_KEY=abc123
DEBUG=True
DATABASE_URL=sqlite:///db.sqlite
CORS_ALLOWED_ORIGINS=http://localhost:5173
```

### Run using Docker/Podman (Recommended)

Replace `podman` with `docker`, depending on what is installed on your host machine.

#### build the container image

`podman build -t python-app .`

#### run the container image

`podman run -p 8080:8080 --env-file=./.env python-app`

### Run directly on your host (Alternative)

In the project root, create a python virtual environment:

```
python -m venv venv
source venv/bin/activate
pip install -r src/requirements.txt
```

Now that the required packages are installed, you can run the project.

```
cd src
./manage.py runserver
```

To run the unit tests
```
./manage.py test
```

