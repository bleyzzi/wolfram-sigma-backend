import os

from dotenv import load_dotenv

load_dotenv()

SECRET = os.environ.get("SECRET")

DB_HOST = os.environ.get("DB_HOST")
DB_PORT = os.environ.get("DB_PORT")
DB_NAME = os.environ.get("DB_NAME")
DB_USER = os.environ.get("DB_USER")
DB_PASS = os.environ.get("DB_PASS")


mail_address = os.environ.get("mail_address")
mail_password = os.environ.get("mail_password")
"""
ADD TEST ENV
"""
