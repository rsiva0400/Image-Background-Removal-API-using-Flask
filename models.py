import secrets
import bcrypt
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    emailId = db.Column(db.String(80), primary_key=True)
    password = db.Column(db.String(120), nullable=False)
    apiKey = db.Column(db.String(16), unique=True, nullable = False, default = secrets.token_hex(16))
    availableApiCalls = db.Column(db.Integer, default = 5)

    def __init__(self,email,password):
        self.emailId = email
        self.password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
    
    def check_password(self,password):
        return bcrypt.checkpw(password.encode('utf-8'),self.password.encode('utf-8'))