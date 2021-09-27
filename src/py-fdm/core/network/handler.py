#!/usr/bin/python3
#-*- coding: utf-8 -*-
import threading
import requests
import json

class Handler:
    def __init__(self, url):
        self.url = url
        self.filename = url.split("/")[-1]

    def check_host(self):
        """
        check the accepted headers.
        """
        r = requests.head(self.url)
        return json.dumps(dict(r.headers))
        
    def download_file(self):
        """
        Reserve file size on disk and then download the file and fill that reserved space.
        """
        s = requests.Session()
        with open(self.filename, 'wb') as output_file:
            with s.get(self.url, timeout=30, stream=True) as getting_file:
                file_size = int(getting_file.headers['content-length'])
                output_file.write(b'\x00' * file_size)
                output_file.seek(0, 0)
                for chunk in getting_file.iter_content(chunk_size=1024):
                    if chunk: output_file.write(chunk)
    def threads_download(self, max_threads = 4):
        """
        Perform a multi-part file download using threads.
        """
        s = requests.Session()
        file_size = int(s.head(self.url).headers['content-length'])
        with open(self.filename, 'wb') as create_dummy:
            create_dummy.write(b'\x00' * file_size)
        def _donwload_file(start, end):
            headers = {'Range': 'bytes=%d-%d' % (start, end)}
            with open(self.filename, 'r+b') as output_file:
                with s.get(self.url, headers=headers, timeout=30, stream=True) as getting_file:
                    output_file.seek(start)
                    for chunk in getting_file.iter_content(chunk_size=1024):
                        if chunk: output_file.write(chunk)
        part = file_size // max_threads
        threads = []
        for thread in range(max_threads):
            start = part * thread
            end = start + part
            t = threading.Thread(target=_donwload_file, args=(start, end))
            threads.append(t)
            t.start()
