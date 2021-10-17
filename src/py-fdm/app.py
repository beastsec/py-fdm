#!/usr/bin/python3
#-*- coding: utf-8 -*-
from flask import Flask, request, jsonify
from core.http import Http

app = Flask(__name__)
fdm_http = Http()

@app.route('/api/v1')
def documentation():
    return 'Documentation.'

@app.route('/api/v1/download-http', methods=['POST'])
def download_http():
    rdata = request.get_json()
    r_url = rdata['url']
    r_threads = rdata['threads']
    r_mthreads = rdata['mthreads']
    fdm_http.download(url=r_url, threads=r_threads, mthreads=r_mthreads)
    data = {'action': 'downloading', 'url': r_url, 'status': 'ok'}
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
  