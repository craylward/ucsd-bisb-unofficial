#===============================================================================
# lab.py
#===============================================================================

"""Lab blueprint

Attributes
----------
bp : Blueprint
    blueprint object, see the flask tutorial/documentation:

    http://flask.pocoo.org/docs/1.0/tutorial/views/

    http://flask.pocoo.org/docs/1.0/blueprints/
"""




# Imports ======================================================================

from flask import Blueprint, render_template
from flask_login import login_required

from ucsd_bisb_unofficial.principals import named_permission




# Blueprint assignment =========================================================

bp = Blueprint('lab', __name__, url_prefix='/lab')




# Functions ====================================================================

@bp.route('/index')
@login_required
@named_permission.require(http_exception=403)
def index():
    """Render the lab index"""
    
    db = get_db()
    posts = Post.query.all()
    return render_template('lab/index.html', posts=posts)

