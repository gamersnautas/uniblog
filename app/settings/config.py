import os

bddPath = os.path.abspath('app.db')

class Ajustes(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'flask-course'
    SQLALCHEMY_DATABASE_URI = 'postgres://qejzqjpgmauvxj:052b26bf64cb13fa0e2b1af40823d8e94f24d1df696f3cb6ef461bcd09f9c527@ec2-18-213-176-229.compute-1.amazonaws.com:5432/dd679vcg6hrutv'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    POSTS_PER_PAGE = 3

class ConexionMail(object):

    MAIL_SERVER= 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'peraltamfps@gmail.com'
    MAIL_PASSWORD = '23566727'
    ADMINS = 'peraltamfps@gmail.com'