#!/usr/bin/python3
#-*- coding: utf-8 -*-
from flask import Flask
from core.network.handler import Handler

app = Flask(__name__)
fdm_handler = Handler(url='https://www.w3.org/WAI/ER/tests/xhtml/testfiles/resources/pdf/dummy.pdf')

@app.route('/api/v1')
def documentation():
    return 'Documentation.'

@app.route('/api/v1/check-host')
def check_host():
    return fdm_handler.check_host()

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
