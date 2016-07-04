# coding: utf-8
from flask import Flask, jsonified, request, current_app
import json


app = Flask(__name__)


@app.route('/hello')
def hello():
    return json.dumps({
        'url': request.full_path,
        'msg': 'hello flask',
        'app': str(current_app)
    }, indent=1, ensure_ascii=True), 200


if __name__ == '__main__':
    app.run(debug=True)
