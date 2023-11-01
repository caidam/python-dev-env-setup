from decouple import config

DEBUG = config('DEBUG', default=False)
SECRET_KEY = config('SECRET_KEY')
DATABASE_URL = config('DATABASE_URL')
EMAIL_HOST = config('EMAIL_HOST')
EMAIL_PORT = config('EMAIL_PORT')
API_KEY = config('API_KEY')

print(API_KEY)