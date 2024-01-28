from flask import Blueprint, request


prediction_app = Blueprint('prediction_app', __name__)


#@prediction_app.route('/health', methods=['GET'])
@prediction_app.route('/')
def health():
    if request.method == 'GET':
        return 'ok'
