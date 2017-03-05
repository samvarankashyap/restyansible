import os
import json
from flask import Flask
from flask import render_template
from flask import Flask, request, send_from_directory
from glob import glob

app = Flask(__name__,static_url_path='/static')

def find(name, path):
    for dir in os.listdir(path):
        for file in os.listdir(path+dir+"/"):
            if name == file.strip(".json"):
                return path+dir+"/"+file
    


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/getmoduleschema/<name>')
def get_module_schema(name):
    file_path =  find(name, "./schemas/")
    schema = open(file_path, "r").read()
    return schema

@app.route('/listmodules/')
def list_modules():
    modules_list = {}
    dirs = os.listdir("./schemas")
    for dir in dirs:
        schema_files = os.listdir("./schemas/"+dir)
        schema_files = [x.strip(".json") for x in schema_files]
        modules_list[dir] = schema_files
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
