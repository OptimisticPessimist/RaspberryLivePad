import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv(verbose=True)
env_path = Path(".") / ".env"

load_dotenv(dotenv_path=env_path)

HOST_NAME = os.getenv('HOST_NAME')
PORT = os.getenv('PORT')
USER = os.getenv('USER')
PASSWORD = os.getenv('PASSWORD')
SECRET_KEY = os.getenv('SECRET_KEY')
