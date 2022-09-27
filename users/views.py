from flask import Blueprint, render_template

users_blueprint = Blueprint('users', __name__, template_folder='templates')


@users_blueprint.route('/')
def index():
    return render_template('main/index.html')


def register():
    return render_template('users/register.html')


def login():
    return render_template('users/login.html')