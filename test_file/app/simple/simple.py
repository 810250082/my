from flask import Blueprint , render_template , abort
from jinja2 import TemplateNotFound

simple_page = Blueprint('simple' , __name__ , template_folder='templates')

#@simple_page.route('/simple' , defaults={'page':'index'})
#@simple_page.route('/simple/<page>')
@simple_page.route('/simple' , defaults={'page':'index'})
@simple_page.route('/simple/<page>')
def show(page):
    try:
        return render_template('pages/%s.html' % page)
    except TemplateNotFound:
        abort(404)