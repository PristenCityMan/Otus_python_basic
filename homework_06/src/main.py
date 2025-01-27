from flask import (
    Flask,
    request,
    render_template,
)
import config


app = Flask(__name__)


app.config.update(
    SQLALCHEMY_DATABASE_URI=config.SQLALCHEMY_DATABASE_URI,
    SQLALCHEMY_ECHO=config.SQLALCHEMY_ECHO,
)
