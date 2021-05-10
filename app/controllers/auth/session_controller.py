import json
import hashlib
import os
import uuid
from os     import environ
from dotenv import load_dotenv


conf = load_dotenv()

pjoin = os.path.join
_DIR = os.path.dirname(os.path.abspath(__file__))
_SESSION_DIR = pjoin(_DIR, 'sessions') 

def mkdigest(user_id, password_hash, session_salt):
    '''
    Generate session identifier
        Parameters:
            user_id (int): ...
            password_hash (str): user sha256 password digest
            custom_salt (str) : used for tests
        
        Returns:
            session_digest (str) : sha512 digest made from parameters
    '''


    hash_candidate = (
          user_id + ':'
        + password_hash + ':' 
        + session_salt
    ).encode()

    return hashlib.sha512(hash_candidate).hexdigest()


def get_session_fpath(session_id):
    session_doge = environ.get('SESSION_SHAKAL_PROTECTION')

    hashed_session_id = session_id + '+' + session_doge
    hashed_session_id = hashlib.sha256(hashed_session_id.encode())

    session_file_name = pjoin( 
        _SESSION_DIR, 
        'session_' + hashed_session_id.hexdigest() + '.json' 
    )

    return session_file_name


# /////////////////////////
# /// SESSION CREATION ///
# ///////////////////////

def session_create( user_id, password_hash, custom_salt ):
    '''
    Create and store user session on the server
        Parameters:
            user_name     (str) : user creds username 
            password_hash (str) : user creds password

        Returns:
            session_hash (str) : Encrypted unique session hash-ID

    '''

    session_data = {}
    session_salt = uuid.uuid4()

    if custom_salt:
        session_salt = custom_salt

    # Save session data to json file
    # ------------------------------
    session_data['user_id']       = user_id
    session_data['password_hash'] = password_hash
    session_data['session_salt']  = session_salt
    session_data['session_id']    = mkdigest(
          user_id
        , password_hash
        , session_salt
    )

    session_file_path = get_session_fpath(session_data['session_id'])

    with open( session_file_path, 'w' ) as out:
        json.dump(session_data, out)

    return session_data['session_id']


# /////////////////////////////
# /// SESSION VERIFICATION ///
# ///////////////////////////

def session_validate(session_id):
    
    session_file_path = get_session_fpath(session_id)

    if os.path.exists(session_file_path):
        with open(session_file_path) as f:
            session_data = json.load(f)
    
    hash_check = mkdigest(
          session_data['user_id']
        , session_data['password_hash']
        , session_data['session_salt']
    )

    if hash_check == session_data['session_id']:
        return True
    else:
        return False

    



