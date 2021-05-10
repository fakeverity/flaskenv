from flask import (
      Blueprint
    , request
    , render_template
    , abort
)
from app.controllers.auth import auth_controller, session_controller

rt_auth = Blueprint('admin', __name__, template_folder='admin')

@rt_auth.route('/', methods=['POST', 'GET'])
def authorize():
   
    if request.method == 'POST':

        username = request.form['username']
        user_pwd = request.form['password']
        
        auth_ctrl = auth_controller
        sess_ctrl = session_controller

        user = auth.ctrl.user_check(username, password)
      
        '''
        if user:
            sess_ctrl.session_create(

        authenticate user with session
        '''
        return 'Hello from authentication page'


