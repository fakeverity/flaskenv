import pytest
import hashlib
from app.controllers.auth import(
      session_create
    , mkdigest
    , session_validate
)

def test_mkdigest():
    _hash = 'ff071b44365e624d7788c4b6433c163d1070d86050580612a3fbb76165429d6a0556f10c0d15880c6cc3607eaf18f68616a7d8d95b460da62b5f71a522944bc9' 
    _user_id = '12' 
    _pwd_hash = '5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8'
    _salt = 'salt'

    hash_proof = mkdigest(
          _user_id
        , _pwd_hash
        , _salt
    )
    assert hash_proof == _hash

def test_session_create():
    sample_user_id = '12'
    sample_user_pass = '5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8'
    sample_session_salt = 'goldsalt'

    
    session_hash = session_create(
          sample_user_id
        , sample_user_pass
        , sample_session_salt
    )
    proof_session_hash = mkdigest(
          sample_user_id
        , sample_user_pass
        , sample_session_salt
    )
    
    assert session_hash  == proof_session_hash, f"\
            Got: { hash_result }\n\n\
            Should be: {proof_session_hash}"

def test_session_validate():

    session_id = 'faa02ac0babde5dcbcbd16b7011a1c53725c7ec50e7d32dbbc6f9e843ce38d8801ba97b9942b539b550cb1c82f9c5348cf38792d3d624215f91e7590dd6b1f39'

    assert session_validate(session_id) == True
