from models.user import User
from db.database import db_session

class UserRepository:
    @staticmethod
    def get_user_by_email(email):
        return db_session.query(User).filter_by(email=email).first()
    