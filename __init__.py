from flask import Blueprint


application__blueprint = Blueprint('test_app', __name__, url_prefix='/test_app')



@application__blueprint.route('/')
def index():
    return 'success'