import os
import json
from flask import Flask
from flask import render_template
from flask import Flask, request, send_from_directory

app = Flask(__name__,static_url_path='/static')

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/getmoduleschema/<name>')
def get_module_schema(name):
    schema = {}
    s = {}
    schema['name'] = {}
    schema['age'] = {}
    schema['name']['type'] = 'string'
    schema['name']['title'] = 'Name'
    schema['name']['required'] = True
    schema['age']['type'] = 'number'
    schema['age']['title'] = 'Age'
    s['schema'] = schema
    """
    schema =  {
        "schema": {
          "name": {
            "type": 'string',
            "title": 'Name',
            "required": True
          },
          "age": {
            "type": 'number',
            "title": 'Age'
          }
        }
    """
    return json.dumps(s)

@app.route('/listmodules/')
def list_modules():
    modules_list = {}
    dirs = os.listdir("./schemas")
    for dir in dirs:
        modules_list[dir] = os.listdir("./schemas/"+dir)
    return json.dumps(modules_list)


@app.route('/js/<path:path>')
def send_js(path):
    return send_from_directory('./static/js', path)


@app.route('/css/<path:path>')
def send_css(path):
    return send_from_directory('./static/css', path)


@app.route('/deps/<path:path>')
def send_deps(path):
    return send_from_directory('./static/deps', path)


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')
