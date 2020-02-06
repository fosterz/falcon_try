import falcon
from waitress import serve
#ENV = os.environ.get("env", "qa")
class hello:
    def on_get(self, req, resp):
        """Handles GET requests"""
        resp.status = falcon.HTTP_200  # This is the default status
        resp.body = ('\nMy first Falcon fly.\n'
                     '\n'
                     '    ~ PWC\n\n')

APP = falcon.API()
APP.add_route('/bla',hello())
serve(APP, host='127.0.0.1', port=8080)