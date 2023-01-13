from flask import Flask, Response
import json

app = Flask(__name__)


@app.route('/county', methods=['GET'])
def get_county():
    country_list = [
        {
            "name": "Bangladesh"
        }

    ]
    return Response(json.dumps(country_list), mimetype='application/json')


if __name__ == '__main__':
    app.run(debug=True)
