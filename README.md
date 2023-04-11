# Volunteer App
If using Windows use WSL. The Node stuff works on Windows but there are some issues with Python/Flask's dependencies and Windows but WSL works great.
## Initial Setup

### Python

1. Make sure the latest version of Python/pip is installed. I think I have 3.11.something.
2. Navigate to the `api` folder.
3. Create a new virtual environment using `python -m venv env`
4. Activate the virtual environment using `source env/bin/activate`
5. Install all dependencies using `pip install -r requirements.txt`

### Vue/Node

1. If you don't already have it, install the latest version of Node here: https://nodejs.org/en/download.
2. Run `npm install -g @vue/cli` to install the Vue command line tools.
3. Navigate to the `ui` folder.
4. Run `npm install` to install all dependencies.

### Database

1. Inside the `db` directory, make a folder called `data`. This will hold the data inside of the database.

## Running the App

1. Open two terminal windows.
2. Navigate to the `api` folder in one terminal window.
3. Run `source env/bin/activate`, then `python server.py` to start the Flask dev server.
4. In the second terminal window, navigate to the `ui` folder.
5. Run `npm run serve` to start the Vue dev server.

> View UI:  
> http://localhost:8080

> Only one API endpoint right now:  
> http://localhost:8000/helloworld

## Running the Docker Container
I didn't test if this was actually a problem but I would make sure both dev servers are closed before building the image and running the container.

The docker container will only work on the EC2 instance.

1. In the root of the project, run `docker-compose up --build`

> View UI:  
> http://localhost:8001
