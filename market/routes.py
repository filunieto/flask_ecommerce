from market import app, form
from flask import render_template, redirect, url_for
from market.models import Item, User
from market.form import RegisterForm  
from market import db

@app.route('/')
@app.route('/home')
def home():
    return render_template("home.html")

@app.route('/market')
def market_page():
    items = Item.query.all()
    
#      [
#     {'id': 1, 'name': 'Phone', 'barcode': '893212299897', 'price': 500},
#     {'id': 2, 'name': 'Laptop', 'barcode': '123985473165', 'price': 900},
#     {'id': 3, 'name': 'Keyboard', 'barcode': '231985128446', 'price': 150}
#      ]
    return render_template("market.html", items=items)


# @app.route('/about/<username>')
# def about_page(username): 
#     return f'about page of {username} '

@app.route('/register', methods=['GET', 'POST'])
def register_page():
    form = RegisterForm()
    if form.validate_on_submit():
        user_to_create  = User(username=form.username.data,
                                email_address=form.email_address.data,
                                password_hash=form.password1.data)
        db.session.add(user_to_create)
        db.session.commit()
        return redirect(url_for('market_page'))
    if form.errors != {}: # En el caso de que no haya erores desde validators
        for err_msg in form.errors.values():
            print(f'ha habido un error en la creación de un usuario: {err_msg} ')

    return render_template('register.html', form=form)

