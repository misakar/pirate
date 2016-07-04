# coding: utf-8

from src.pirate import Pirate
from src.route import green_route, current_app, request


app = Pirate()


@green_route(app, '/hello')
@app.tojson
def hello():
    return {
        'url': request.full_path,
        'msg': 'hello pirate',
        'app': str(current_app)
    }, {'Status Code': '200 OK'}


    # @green_route(app, '/test/')
    # @app.tojson
    # def test():
    #     return {
    #         'url': request.full_path,
    #         'msg': 'test pirate',
    #         'app': str(current_app)
    #     }, {'Status Code': '200 OK'}


if __name__ == '__main__':
    app.firing(debug=True)
