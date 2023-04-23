from flask import Flask, jsonify, request
from flask_cors import CORS
from sqlalchemy import create_engine
from sqlalchemy.pool import QueuePool
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.exc import IntegrityError
from tables.User import User
from tables.UserDetails import UserDetails
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

CORS(app)

if (os.environ.get("FLASK_ENVI") == "prod"):
    engine = create_engine(os.environ.get("DATABASE_URL") + "prod",
                           poolclass=QueuePool,
                           pool_size=5,
                           max_overflow=10,
                           pool_timeout=30
                           )
else:
    engine = create_engine(os.environ.get("DATABASE_URL") + "loginTest",
                           poolclass=QueuePool,
                           pool_size=5,
                           max_overflow=10,
                           pool_timeout=30
                           )

Session = scoped_session(sessionmaker(bind=engine))


@app.route('/helloworld')
def hello_world():
    data = "Hello from Flask!"
    response = jsonify(data)
    return response


@app.get('/getUsers')
def get_users():
    session = Session()
    # Query the database for all users, results is a list of User objects
    results = session.query(User).all()
    session.close()
    # Return a new list containing each user object in result converted to a dictionary, and then jsonified
    return jsonify([user.asDict() for user in results])


@app.route('/login', methods=['POST'])
def login():
    if request.method == 'POST':
        session = Session()
        data = request.get_json()
        results = session.query(User).filter_by(emailAddress=data['email']).first()
        session.close()
        return jsonify({"password": results.password, "salt": results.salt})


@app.route('/createAccount', methods=['POST'])
def createAccount():
    if request.method == 'POST':
        session = Session()
        data = request.get_json()
        user = User(emailAddress=data['emailAddress'], password=data['passwordInfo']["password"], salt=data["passwordInfo"]["salt"])
        userDetails = UserDetails(emailAddress=data["emailAddress"], firstName=data["firstName"], lastName=data["lastName"],
                                  cellPhone=data["cellPhone"], hoursPerMonth=data["hoursPerMonth"], address=data["address"])
        session.add(user)
        session.add(userDetails)
        try:
            session.commit()
            session.close()
            return jsonify({"status": "OK"})
        except IntegrityError:
            session.rollback()
            session.close()
            return jsonify({"status": "ERROR", "message": "An account already exists with this email."})
        except Exception:
            session.rollback()
            session.close()
            return jsonify({"status": "ERROR", "message": "An error occurred creating your account."})


if __name__ == '__main__':
    app.run(debug=True, port=8000)
