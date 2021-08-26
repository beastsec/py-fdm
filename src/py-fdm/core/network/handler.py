#!/usr/bin/python3
#-*- coding: utf-8 -*-
import requests

class Handler:
    def __init__(self, url):
        self.url = url
        self.filename = url.split("/")[-1]

    def check_host(self):
        """
        check the accepted headers.
        """
        _r = requests.head(self.url)
        return(_r.headers)
        
    def simple_download(self):
        """
        Downloads the file specified in the URL by data streaming to be stored.
        """
        _s = requests.Session()
        with open(self.filename, 'wb') as _output_file:
            with _s.get(self.url, stream=True) as _getting_file:
                for _chunk in _getting_file.iter_content(chunk_size=1024):
                    if _chunk: _output_file.write(_chunk)
