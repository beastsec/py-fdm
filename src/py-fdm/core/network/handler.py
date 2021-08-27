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
        r = requests.head(self.url)
        return(r.headers)
        
    def simple_download(self):
        """
        Reserve file size on disk and then download the file and fill that reserved space.
        """
        s = requests.Session()
        with open(self.filename, 'wb') as output_file:
            with s.get(self.url, stream=True) as getting_file:
                file_size = int(getting_file.headers['content-length'])
                output_file.write(b'\x00' * file_size)
                output_file.seek(0, 0)
                for chunk in getting_file.iter_content(chunk_size=1024):
                    if chunk: output_file.write(chunk)
