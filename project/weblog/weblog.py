from flask import Flask, session, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
import os

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:luciferpapa1@localhost/weblog'
app.config['SECRET_KEY'] = 'secret'     # must to be change

app.debug = True

db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), unique=True)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        session['user'] = request.form['username']
    return render_template('index.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return 'You are logout'

@app.route('/home')
@login_required
def home():
    return 'The current user is ' + current_user.username

if __name__ == '__main__':
    app.run()
