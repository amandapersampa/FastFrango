from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

from fastFrango.controllers import default