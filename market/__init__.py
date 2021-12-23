from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template


app = Flask(__name__)
# Para que no aparezca mensaje de error
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'
db = SQLAlchemy(app)

from market import routes

# if __name__ == '__main__':
#     app.run()