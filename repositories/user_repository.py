from models.user import User
from db.database import db_session

class UserRepository:
    @staticmethod
    def get_user_by_email(email):
        return db_session.query(User).filter_by(email=email).first()
    
    @staticmethod
    def update_password(email, nova_senha):
        user = db_session.query(User).filter_by(email=email).first()

        if user:
            user.senha = nova_senha
            db_session.commit()
        return user
        
