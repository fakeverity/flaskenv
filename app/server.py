from flask import(
      Flask
    , request
    , render_template
)
from os import environ
from db.spinup import ALCDB
from db.models.users   import User

app = Flask(__name__)

def server():
    app.run()

@app.route('/')
def home():
    return "hello"

@app.route('/create_user', methods=['GET', 'POST'])
def create_user():

    # For get request we return the form for user creation
    # ----------------------------------------------------
    if request.method == 'GET':
        return render_template('create_user_frontend.html')

    
    # When the form is send - proccess request from user
    elif request.method == 'POST':
        r_data = request.form
        dbInstance = ALCDB()

        u_name     = r_data['user_name']
        u_fullname = r_data['user_fullname']
        u_alias    = r_data['user_alias']

        new_user_record = User(
              name      = u_name
            , full_name = u_fullname
            , username  = u_alias
        )

        session = dbInstance.Session()
        session.add(new_user_record)
        added_user = session.query(User).filter_by(id=new_user_record.id).first()
        return added_user 
