# Volunteer App

## Initial

### Python

1. Make sure the latest version of Python/pip is installed and up to date.
2. Navigate to the `backend` folder.
3. Create a new virtual environment using `python -m venv env`
4. Activate the virtual environment using `source env/bin/activate`
5. Install all dependencies using `pip install -r requirements.txt`

### Vue/Node

1. If you don't already have it, install the latest version of Node here: https://nodejs.org/en/download.
2. Run `npm install -g @vue/cli` to install the Vue command line tools.
3. Navigate to the `frontend` folder.
4. Run `npm install` to install all dependencies.

## Running the App

1. Open two terminal windows.
2. Navigate to the `backend` folder in one terminal window.
3. Run `source env/bin/activate`, then `python server.py` to start the Flask dev server.
4. In the second terminal window, navigate to the `frontend` folder.
5. Run `npm run serve` to start the Vue dev server.

API: http://localhost:8000

UI: http://localhost:8080

## Running the Docker Image

1. Run `docker-compose up --build`

API: http://localhost:8000

UI: http://localhost:8001
