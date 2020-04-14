import os
from pathlib import Path
from dotenv import load_dotenv

DEVELOP_MODE = True

load_dotenv(verbose=True)
root_path = Path(".")

if DEVELOP_MODE:
    env_path = root_path / ".dev.env"
else:
    env_path = root_path / ".env"

load_dotenv(dotenv_path=env_path)

HOST_NAME = os.getenv('HOST_NAME')
PORT = os.getenv('PORT')
USER = os.getenv('USER')
PASSWORD = os.getenv('PASSWORD')
SECRET_KEY = os.getenv('SECRET_KEY')
