from .base import *
import dj_database_url
import os

DEBUG = True  # Les tests passent mieux avec DEBUG True
ALLOWED_HOSTS = ["localhost", "127.0.0.1"]

DATABASE_URL = os.environ.get(
    "DATABASE_URL",
    "postgres://postgres:0000@localhost:5432/test_db"
)

DATABASES = {
    "default": dj_database_url.parse(DATABASE_URL)
}

DATABASES["default"]["TEST"] = {
    "NAME": "test_db"
}
