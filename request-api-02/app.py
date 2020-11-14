import os

from flask import Flask
import requests

app = Flask(__name__)

BASE_SERVICE_URL = os.getenv('BASE_SERVICE_URL')


@app.route('/<identifier>')
def create_resource(identifier):
    result = requests.get(BASE_SERVICE_URL + "{}".format(identifier))
    return {
        'status_code': 200,
        'message': result.json(),
        'service_called': 'service-02'
    }


if __name__ == '__main__':
    app.run()
