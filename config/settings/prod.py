from .base import *
import os

DEBUG =True 

ALLOWED_HOSTS = os.getenv("ALLOWED_HOSTS", "").split(",")

# security
SECURE_SSL_REDIRECT =False 
SESSION_COOKIE_SECURE = False 
CSRF_COOKIE_SECURE =False 
