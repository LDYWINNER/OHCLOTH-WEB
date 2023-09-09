from flask import Flask, send_from_directory
from flask_restful import Api, Resource, reqparse
from flask_cors import CORS  # we should comment this on deployment
from api.ApiHandler import ApiHandler

app = Flask(__name__, static_url_path='', static_folder='frontend/build')
CORS(app)  # should comment this on deployment too
api = Api(app)


@app.route("/", defaults={'path': ''})
def serve(path):
    return send_from_directory(app.static_folder, 'index.html')


api.add_resource(ApiHandler, '/flask/hello')

if __name__ == "__main__":
    app.run(host="localhost", port=8000, debug=True)
