from   dotenv     import load_dotenv
from   app.server import server
import os

def start_app():
    load_dotenv()
    server()

    
