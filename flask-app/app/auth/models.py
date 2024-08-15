from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from typing import Optional
import sqlalchemy as sa
import sqlalchemy.orm as so
from app import db, login 

class User(UserMixin, db.Model):
    """
    User model for storing user-related data.
    
    This class inherits from UserMixin (Flask-Login) and db.Model (SQLAlchemy).
    It represents the 'user' table in the database.
    """

    id: so.Mapped[int] = so.mapped_column(primary_key=True)
    username: so.Mapped[str] = so.mapped_column(sa.String(64), index=True, unique=True)
    email: so.Mapped[str] = so.mapped_column(sa.String(120), index=True, unique=True)
    password_hash: so.Mapped[Optional[str]] = so.mapped_column(sa.String(256))

    def __repr__(self):
        """
        Provide a string representation of the User instance.
        
        Returns:
            str: A string containing the user's ID and username.
        """
        return f"<User ({self.id}): {self.username}>"

    def set_password(self, password):
        """
        Set the password for the user.
        
        Args:
            password (str): The plaintext password to be hashed and stored.
        """
        self.password_hash = generate_password_hash(password)
    
    def check_password(self, password):
        """
        Check if the provided password matches the stored hash.
        
        Args:
            password (str): The plaintext password to be checked.
        
        Returns:
            bool: True if the password is correct, False otherwise.
        """
        return check_password_hash(self.password_hash, password)

@login.user_loader
def load_user(id):
    """
    Flask-Login user loader function.
    
    This function is used by Flask-Login to load a user from the database
    given the user ID stored in the session.
    
    Args:
        id (str): The user ID as a string.
    
    Returns:
        User: The User object if found, None otherwise.
    """
    return db.session.get(User, int(id))