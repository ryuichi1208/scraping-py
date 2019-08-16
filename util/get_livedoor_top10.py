# -*- coding: UTF-8 -*-

import requests
import json
from flask import Flask, render_template, request, \
     redirect, url_for, jsonify, abort
from bs4 import BeautifulSoup as bs

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

@app.route('/api/v1/news')
def index():
    url = "https://news.livedoor.com/"
    s = bs(requests.get(url).text, "lxml").find_all("a", class_="rewrite_ab")
    return jsonify({s[i].getText():s[i].get("href") for i in range(11) if s[i].getText() != ""})


@app.route('/api/v1/test/403')
def test_403():
    abort(403, {'id': 200})


@app.errorhandler(404)
def error_handler(error):
    return "Not Found"


@app.errorhandler(403)
def error_handler(error):
    print(error.code)
    response = jsonify({ 'id': error.description['id'], 'message': 'id is different', 'result': error.code })
    return response, error.code

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=9080)
