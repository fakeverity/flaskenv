from flask import(
      Flask
    , request
    , render_template
    , Blueprint
)
from   os         import environ
import app.routes as routes
import db.spinup

# APP INITIALIZATION
# -----------------------------------
app = Flask(__name__, template_folder='views')

rt_auth = routes.auth.rt_auth
# ROUTES DECLARATION
# -----------------------------------
#app.register_blueprint(routes.rt_home)
#app.register_blueprint(routes.rt_user, url_prefix='/user')
app.register_blueprint(rt_auth, url_prefix='/auth')


def server():
    app.run()
'''
@app.route('/')
def home():
    return "hello"

@app.route('/list_users', methods=['GET', 'POST'])
def list_users():
    session = db.spinup.Session()
    user_list = session.query(User).all()
    return render_template('user_list.html', data=user_list) 
'''
'''
@app.route('/create_user', methods=['GET', 'POST'])
def create_user():

    # For get request we return the form for user creation
    # ----------------------------------------------------
    if request.method == 'GET':
        return render_template('create_user_frontend.html')

    
    # When the form is send - proccess request from user
    elif request.method == 'POST':
        r_data = request.form

        u_name     = r_data['user_name']
        u_fullname = r_data['user_fullname']
        u_alias    = r_data['user_alias']

        new_user_record = User(
              name      = u_name
            , full_name = u_fullname
            , username  = u_alias
        )

        session = db.spinup.Session()
        session.add(new_user_record)
        added_user = session.query(User).filter_by(name=new_user_record.name).first()
        session.commit()
'''        
#        return render_template('create_result.html'
#            , name     = added_user.name
#            , fullname = added_user.full_name
#            , username = added_user.username
#            , created  = added_user.created)
