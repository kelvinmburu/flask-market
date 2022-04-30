from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__) #Built-in variable that can be called for any variable file; can be called for any python file
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'
db = SQLAlchemy(app)