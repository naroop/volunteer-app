from flask import Flask, jsonify
from flask_cors import CORS
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from tables.Users import Users
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

CORS(app)

if (os.environ.get("FLASK_ENVI") == "prod"):
    engine = create_engine(os.environ.get("DATABASE_URL") + "prod")
else:
    engine = create_engine(os.environ.get("DATABASE_URL") + "dev")

Session = sessionmaker(bind=engine)
session = Session()


@app.route('/helloworld')
def hello_world():
    data = "Hello from Flask!"
    response = jsonify(data)
    return response


@app.route('/getUsers')
def get_users():
    # Query the database for all users, results is a list of User objects
    results = session.query(Users).all()
    # Return a new list containing each user object in result converted to a dictionary, and then jsonified
    return jsonify([user.asDict() for user in results])


if __name__ == '__main__':
    app.run(debug=True, port=8000)
