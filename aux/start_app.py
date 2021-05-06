from   dotenv     import load_dotenv
from   app.server import server
import os

def start_app(take_shit):
    load_dotenv()
    server()

