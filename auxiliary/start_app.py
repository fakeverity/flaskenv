from   dotenv     import load_dotenv
from   app.server import server
from   db.spinup  import db_init
import os

def start_app(take_shit):
    load_dotenv()
    db_init()
    server()

    
