import db.spinup
import hashlib
from   db.models.User import User

dbSession = db.spinup.Session

def pwd_crypt(pwd):
    return hashlib.sha512(pwd.encode()).hexdigest()

def user_check(username, user_pass):
    user_from_db = dbSession.query(User).filter_by(username).first()
    
    password_hash = pwd_crypt(user_pass)

    if password_hash == user_from_db.password:
        return user_from_db
    else:
        return False


def user_create(
      full_name
    , username
    , password
    , role
):
    new_user = User(
          fullname
        , username
        , pwd_crypt(password)
        , created_time
        , role
    )
    dbSession.add(new_user)
    user_exists = dbSession.query(User).filter_by(username=new_user.username).first()
    dbSession.commit()

    if user_exists:
        return True
    else:
        return False
