from models import db, User

def init_db(app):
    db.init_app(app)
    with app.app_context():
        db.create_all()

# User data functions
def create_user(email, password):
    user = User(email=email, password=password)
    db.session.add(user)
    db.session.commit()

def get_user_by_email(email):
    return User.query.filter_by(emailId = email).first()


def get_user_by_apikey(apiKey):
    return User.query.filter_by(apiKey=apiKey).first()


def update_available_api_calls(user):
    user.availableApiCalls -= 1
    db.session.commit()
