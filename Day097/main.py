# This a a copy of https://github.com/RajaShirjeel/Online-Shop

from flask import Flask, render_template, request, redirect, url_for, flash, abort
from flask_login import UserMixin, login_user, logout_user, current_user, LoginManager
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import  generate_password_hash, check_password_hash
from functools import wraps
from datetime import datetime
import secrets
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("DB_URI", "sqlite:///covers.db")
db = SQLAlchemy()
db.init_app(app)
app.config['SECRET_KEY'] = 'secret-key-goes-here'
secret_key = secrets.token_hex(16)
app.secret_key = secret_key

login_manager = LoginManager()
login_manager.init_app(app)

# Association Table
cart_items = db.Table(
    'cart_items',
    db.Column('cart_id', db.Integer, db.ForeignKey('cart.id'), primary_key=True),
    db.Column('cover_id', db.Integer, db.ForeignKey('covers.id'), primary_key=True),
    db.Column('cover_quantity', db.Integer, nullable=False, default=1)
)

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    email = db.Column(db.String(250), nullable=False)
    password = db.Column(db.String(250), nullable=False)
    comments = db.relationship('Comment', backref='user')
    orders = db.relationship('Order', backref='user')
    cart = db.relationship('Cart', backref='user', uselist=False)
    
class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    covers = db.relationship('Covers', backref='order')
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    date = db.Column(db.String(250), nullable=False)

class Covers(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), nullable=False)
    model = db.Column(db.String(250), nullable=False)
    price = db.Column(db.String(250), nullable=False)
    image =  db.Column(db.String(250), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    order_id = db.Column(db.Integer, db.ForeignKey('order.id'), nullable=True)
    carts = db.relationship('Cart', secondary=cart_items, backref='covers', overlaps="carts,covers")

class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(250), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

class Cart(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    items = db.relationship('Covers', secondary=cart_items, backref='cart', overlaps="carts,covers")
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

      
with app.app_context():
    db.create_all()


@login_manager.user_loader
def load_user(user_id):
    return db.session.get(User, int(user_id))


def admin_only(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not current_user.is_authenticated or current_user.id !=1:
            return abort(403)
        return f(*args, **kwargs)
    return decorated_function

@app.route("/", methods=['POST', 'GET'])
def home():
    if request.method == "POST":
        new_comment = Comment(
            user_id = current_user.id,
            text = request.form.get('userComment')
        )
        db.session.add(new_comment)
        db.session.commit()
    page = request.args.get('page', 1, type=int)
    per_page = 12
    covers = Covers.query.paginate(page=page, per_page=per_page, error_out=False)
    results = db.session.execute(db.select(User).order_by(User.name))
    users = results.scalars().all()
    return render_template("home.html", covers=covers, users=users)


@app.route('/add_cover', methods=['POST', 'GET'])
@admin_only
def add_cover():
    if request.method == "POST":
        new_cover = Covers(
            model = request.form.get('phoneName'),
            price = request.form.get('price'),
            image = request.form.get('image'),
            quantity = request.form.get('quantity'),
            title = request.form.get('title')
        )

        db.session.add(new_cover)
        db.session.commit()
        return(redirect(url_for('home')))
    return render_template("covers_add_form.html")


@app.route('/cover_details/<cover_id>', methods=['POST', 'GET'])
def cover_detais(cover_id):
    if request.method == "POST":
        new_comment = Comment(
            user_id = current_user.id,
            text = request.form.get('userComment')
        )
        db.session.add(new_comment)
        db.session.commit()
    results = db.session.execute(db.select(User).order_by(User.name))
    users = results.scalars().all()
    cover = db.get_or_404(Covers, cover_id)
    return render_template("cover_details.html", cover=cover, users=users)


@app.route('/login', methods=['POST','GET'])
def login():
    if request.method == 'POST':
        results = db.session.execute(db.select(User).where(User.email == request.form.get('email')))
        user = results.scalar()
        if user:
            password = request.form.get('password')
            if (check_password_hash(user.password, password)):
                login_user(user)
                return redirect(url_for('home'))
            else:
                flash("Incorrect password!")
        else:
            flash('No  account found with that email address. Please register or check your entry.')
    return render_template("login-form.html")


@app.route('/signup', methods=['POST', 'GET'])
def signup():
    if request.method == 'POST':
        results = db.session.execute(db.select(User).where(User.email == request.form.get('email')))
        user = results.scalar()
        if not user:
            new_user = User(
                name = request.form.get('username'),
                email = request.form.get('email'),
                password = generate_password_hash(request.form.get('password'))
            )
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user)
            return redirect(url_for('home'))
        else:
            flash(f"An account is already registered to this email.")
    return render_template('signup-form.html')


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route("/add-to-cart/<int:cover_id>")
def add_to_cart(cover_id):
    if not current_user.is_authenticated:
        return render_template('not_log_in.html', message="You need to be logged in to add items to your cart")

    user = current_user
    cover = db.get_or_404(Covers, cover_id)

    if user.cart is None:
        user.cart = Cart()
        db.session.commit()

    user_cart = user.cart
    cart_item = db.session.query(cart_items).filter_by(cart_id=user_cart.id, cover_id=cover.id).first()

    if cart_item is None:
        # Create a new entry in the association table
        db.session.execute(cart_items.insert().values(cart_id=user_cart.id, cover_id=cover.id, cover_quantity=1))
    else:
        # Update the cover_quantity column in the cart_items table
        db.session.execute(cart_items.update().where(cart_items.c.cart_id == user_cart.id, cart_items.c.cover_id == cover.id).values(cover_quantity=cart_item.cover_quantity + 1))

    # Check if the cover is not already in user_cart.items
    if cover not in user_cart.items:
        # Directly append the cover to user_cart.items
        user_cart.items.append(cover)

    db.session.commit()

    return redirect(url_for('view_cart'))


@app.route("/view_cart")
def view_cart():
    if not current_user.is_authenticated:
        return render_template('not_log_in.html', message="You need to be logged in to access your cart")

    user = current_user
    user_cart = user.cart

    if user_cart is None:
        user_cart = Cart(user_id=user.id)
        db.session.add(user_cart)
        db.session.commit()

    user_cart_items = user_cart.items
    total = 0
    items = []

    for item in user_cart_items:
        # Use db.session.query(cart_items) to get the cover_quantity
        cart_item = db.session.query(cart_items).filter_by(cart_id=user_cart.id, cover_id=item.id).first()
        cover_item = {
            'cover': item,
            'cover_quantity': cart_item.cover_quantity if cart_item else 0,  # Default to 0 if cart_item is None
            'image': item.image,
            'price': item.price,
            'title': item.title,
            'model': item.model,
            'id': item.id
        }
        items.append(cover_item)
        total += int(item.price.split('.')[1]) * cover_item['cover_quantity']

    return render_template("cart.html", items=items, total=total)


@app.route("/delete_item/<int:cover_id>")
def delete_cover(cover_id):
    user = current_user
    user_cart = user.cart
    cover_to_remove = db.get_or_404(Covers, cover_id)
    cart_item = db.session.query(cart_items).filter_by(cart_id=user_cart.id, cover_id=cover_to_remove.id).first()
    if cart_item:
        db.session.execute(cart_items.delete().where(cart_items.c.cart_id==user_cart.id, cart_items.c.cover_id==cover_to_remove.id))
        db.session.commit()
            
    return redirect(url_for('view_cart'))


@app.route('/search_covers/')
def search_covers():
    s = request.args.get('query', '')
    results = Covers.query.filter(Covers.title.ilike(f"%{s}%")).all()
    return render_template('results.html', results=results, query=s)


@app.route('/account')
def account():
    if current_user.is_authenticated:
        orders = Order.query.filter_by(user_id=current_user.id).all()
        return render_template("account.html", user=current_user, items=orders)
    else:
       return render_template("not_log_in.html", message="You need to be logged in to check your account")
    
@app.route('/checkout', methods=['POST', 'GET'])
def checkout():
    if request.method == 'POST':
        user = current_user
        new_order = Order(
            user_id = user.id,
            date = str(datetime.today().date())
        )
        db.session.add(new_order)
        db.session.commit()

        for item in user.cart.items:
            cart_it = db.session.query(cart_items).filter_by(cart_id=user.cart.id, cover_id=item.id).first()
            if cart_it:
                item.order_id = new_order.id
                cover = db.session.get(Covers, item.id)
                cover.quantity -= cart_it.cover_quantity
                db.session.query(cart_items).filter_by(cart_id=user.cart.id, cover_id=item.id).delete()
                db.session.commit()

        user.cart.items = []
        db.session.commit()
        return render_template("order_sucess.html")

    user = current_user
    if not current_user.is_authenticated or user.cart is None:
         return render_template("not_log_in.html", message='Session Expired! Please Log In Again')
    
    user_cart = user.cart
    user_cart_items = user_cart.items
    total = 0
    items = []

    for item in user_cart_items:
        # Use db.session.query(cart_items) to get the cover_quantity
        cart_item = db.session.query(cart_items).filter_by(cart_id=user_cart.id, cover_id=item.id).first()
        cover_item = {
            'cover': item,
            'cover_quantity': cart_item.cover_quantity,
            'image': item.image,
            'price': item.price,
            'title': item.title,
            'model': item.model,
            'id': item.id
        }
        items.append(cover_item)
        total += int(item.price.split('.')[1]) * cover_item['cover_quantity']
    return render_template("checkout.html", items=items, total=total)

if __name__ == "__main__":
    app.run(debug=False)