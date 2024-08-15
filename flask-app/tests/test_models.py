import pytest
from app.auth.models import User
from app import db


@pytest.fixture
def new_user(username, email, password):
    user = User(username=username, email=email)
    user.set_password(password)
    return user

@pytest.mark.parametrize('new_user', [['testuser', 'test@gmail.com', '12345678']])
def test_new_user(new_user, username, email, password):
    assert new_user.username == username
    assert new_user.email == email
    assert new_user.password_hash is not None
    assert new_user.check_password(password)
    assert not new_user.check_password("wrongpassword")

def test_user_representation(new_user):
    assert str(new_user) == "<User (None): testuser>"

def test_user_id(new_user):
    assert new_user.id is None  # ID should be None before adding to database

def test_user_password_hashing(new_user):
    assert new_user.password_hash != "testpassword"

def test_invalid_username_format():
    with pytest.raises(ValueError):  # Assuming you have validation in place
        User(username="user@123", email="user@example.com")

def test_invalid_email_format():
    with pytest.raises(ValueError):  # Assuming you have validation in place
        User(username="validuser", email="invalid-email")

@pytest.mark.parametrize("attribute", ["username", "email"])
def test_unique_constraint(new_user, attribute):
    # This test requires database interaction
    db.session.add(new_user)
    db.session.commit()

    duplicate_user = User(username=new_user.username, email=new_user.email)
    db.session.add(duplicate_user)
    
    with pytest.raises(Exception):  # Could be IntegrityError or similar
        db.session.commit()

    db.session.rollback()

def test_user_loader(new_user):
    # This test requires database interaction
    db.session.add(new_user)
    db.session.commit()

    from app.auth.models import load_user  # Import the user_loader function
    loaded_user = load_user(new_user.id)
    assert loaded_user == new_user

    db.session.delete(new_user)
    db.session.commit()