from flask_sqlalchemy import SQLAlchemy
from flask import Flask


app = Flask(__name__)
# Para que no aparezca mensaje de error
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'
app.config['SECRET_KEY'] = '213f11f2cba0de8fb3f31595'
db = SQLAlchemy(app)


from market import routes

# if __name__ == '__main__':
#     app.run()