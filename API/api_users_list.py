from flask import Flask, Response
import json

app = Flask(__name__)


@app.route('/users', methods=['GET'])
def get_users():
    user_list = [
        {
            "id": 1,
            "name": "John Doe 1"
        },
        {
            "id": 2,
            "name": "Jane Doe 2"
        },
        {
            "id": 3,
            "name": "Jane Doe 3"
        },
        {
            "id": 4,
            "name": "Jane Doe 4"

        },
        {
            "id": 5,
            "name": "Jane Doe 5"

        }
    ]
    return Response(json.dumps(user_list), mimetype='application/json')


if __name__ == '__main__':
    app.run(debug=True)
