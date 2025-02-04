# Statement for enabling the development environment
import os


class ConfigBase(object):
    """docstring for ConfigBase"""
    DEBUG = True
    # Define the application directory
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))
    PROJECT_DIR = os.path.join(BASE_DIR, 'app')
    # Define the database - we are working with
    # SQLite for this example
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'app.db')
    DATABASE_CONNECT_OPTIONS = {}
    FLASK_ADMIN_SWATCH = 'cerulean'

    # Application threads. A common general assumption is
    # using 2 per available processor cores - to handle
    # incoming requests using one and performing background
    # operations using the other.
    THREADS_PER_PAGE = 2

    # Enable protection agains *Cross-site Request Forgery (CSRF)*
    CSRF_ENABLED = True

    # Use a secure, unique and absolutely secret key for
    # signing the data.
    CSRF_SESSION_KEY = "secret"

    # Secret key for signing cookies
    SECRET_KEY = "secret"


class ConfigDevelop(ConfigBase):
    pass


class ConfigProduct(ConfigBase):
    pass