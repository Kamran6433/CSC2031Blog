from flask import Blueprint, render_template

blog_blueprint = Blueprint('blog', __name__, template_folder='templates')


@blog_blueprint.route('/')
def index():
    return render_template('main/index.html')


def blog():
    return render_template('blog/blog.html')