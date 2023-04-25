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
    engine = create_engine(os.environ.get("DATABASE_URL") + "dev",
                           poolclass=QueuePool,
                           pool_size=5,
                           max_overflow=10,
                           pool_timeout=30
                           )

Session = scoped_session(sessionmaker(bind=engine))


@app.get('/getUsers')
def getUsers():
    session = Session()
    # Query the database for all users, results is a list of User objects
    results = session.query(User).all()
    session.close()
    # Return a new list containing each user object in result converted to a dictionary, and then jsonified
    return jsonify([user.asDict() for user in results])


@app.get('/getUserDetails/<string:emailAddress>')
def getUserDetailsByEmail(emailAddress):
    session = Session()
    result = session.query(UserDetails).filter_by(emailAddress=emailAddress).first()
    session.close()
    if result:
        return jsonify({"error": False, "userDetails": result.asDict()})
    else:
        return jsonify({"error": True, "message": "An error occurred trying to find your account."})


@app.route('/login', methods=['POST'])
def login():
    if request.method == 'POST':
        session = Session()
        data = request.get_json()
        result = session.query(User).filter_by(emailAddress=data['emailAddress']).first()
        session.close()
        if result:
            return jsonify({"password": result.password, "salt": result.salt})
        else:
            return jsonify({"error": True, "message": "No account was found with that email address."})


@app.route('/createAccount', methods=['POST'])
def createAccount():
    if request.method == 'POST':
        try:
            session = Session()
            data = request.get_json()
            user = User(emailAddress=data['emailAddress'], password=data['passwordInfo']["password"], salt=data["passwordInfo"]["salt"])
            userDetails = UserDetails(emailAddress=data["emailAddress"], firstName=data["firstName"], lastName=data["lastName"],
                                      cellPhone=data["cellPhone"], hoursPerMonth=data["hoursPerMonth"], address=data["address"])
            session.add(user)
            session.add(userDetails)
            session.commit()
            session.close()
            return jsonify({"error": False})
        except IntegrityError:
            session.rollback()
            session.close()
            return jsonify({"error": True, "message": "An account already exists with the given email address."})
        except Exception as e:
            print(type(e), e)
            session.rollback()
            session.close()
            return jsonify({"error": True, "message": "An error occurred creating your account."})


@app.route("/updateAccount", methods=['PATCH'])
def edit():
    if request.method == 'PATCH':
        try:
            session = Session()
            data = request.get_json()
            userInfo = session.query(UserDetails).filter_by(emailAddress=data['emailAddress']).first()
            for key, value in data.items():
                if (key == 'emailAddress'):
                    continue
                setattr(userInfo, key, value)
            session.commit()
            session.close()
            return jsonify({"error": False})
        except Exception as e:
            print(e)
            session.rollback()
            session.close()
            return jsonify({"error": True, "message": "An error occurred updating your account."})


if __name__ == '__main__':
    app.run(debug=True, port=8000)
