import jwt
import datetime
import os
from flask import Flask, request
from flask_mysqldb import MySQL

server = Flask(__name__)
mysql = MySQL(server)

# config
server.config['MYSQL_SERVER'] = os.environ.get('MYSQL_SERVER')
''''''