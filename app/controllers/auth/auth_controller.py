import json
import hashlib
import os
import uuid
from os import urandom

pjoin = os.path.join
_DIR = os.path.dirname(os.path.abspath(__file__))
_SESSION_DIR = pjoin(_DIR, 'sessions') 


def create_session( user_id, password_hash, custom_salt ):
    '''
    Create and store user session on the server
        Parameters:
            user_name     (str) : user creds username 
            password_hash (str) : user creds password

        Returns:
            session_hash (str) : Encrypted unique session hash-ID

    '''

    session_file = pjoin( _SESSION_DIR, 'user_' + user_id + '.json' )
    session_data = {}
        
    # Save session data to json file
    # ------------------------------
    session_data['user_id'] = user_id
    session_data['password_hash'] = password_hash
    session_data['session_id'] = mkdigest(
          user_id
        , password_hash
        , custom_salt
    )

    with open( session_file, 'w' ) as out:
        json.dump(session_data, out)

    return session_data['session_id']


def mkdigest(user_id, password_hash, custom_salt):
    '''
    Generate session identifier
        Parameters:
            user_id (int): ...
            password_hash (str): user sha256 password digest
            custom_salt (str) : used for tests
        
        Returns:
            session_digest (str) : sha512 digest made from parameters
    '''

    session_salt = uuid.uuid4()

    if custom_salt:
        session_salt = custom_salt

    hash_candidate = (
          user_id + ':'
        + password_hash + ':' 
        + session_salt
    ).encode()

    return hashlib.sha512(hash_candidate).hexdigest()


