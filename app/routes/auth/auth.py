from flask import (
      Blueprint
    , request
    , render_template
    , abort
)
from hashlib import md5

rt_auth = Blueprint('authorize', __name__, template_folder='auth')

@rt_auth.route('/', methods=['POST', 'GET'])
def authorize():
    
    return 'Hello from authentication page'


