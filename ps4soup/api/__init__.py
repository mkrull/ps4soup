import json

from flask import Flask, Response

from ps4soup.client import fetch_list

app = Flask(__name__)


@app.route('/games')
def games():
    return json.dumps(fetch_list())


@app.route('/games/<title>')
def show_game(title):
    for item in fetch_list():
        if item['title'] == title:
            return json.dumps(item)

    return Response('{}', status=404, mimetype='application/json')


def run():
    app.run(host='localhost', port=1337, debug=False)
