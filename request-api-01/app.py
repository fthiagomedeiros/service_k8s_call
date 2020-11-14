from flask import Flask

app = Flask(__name__)


@app.route('/<identifier>')
def create_resource(identifier):
    return {
        'status_code': 201,
        'message': 'Service {} called'.format(identifier)
    }


if __name__ == '__main__':
    app.run()
