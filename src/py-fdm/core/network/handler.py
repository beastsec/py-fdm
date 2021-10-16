#!/usr/bin/python3
#-*- coding: utf-8 -*-
import threading
import requests

class Http:
    def __init__(self):
        self.headers = {'User-Agent': 'py-fdm/0.1'}
    def multi_threads():
        """
        Perform a multi-part file download using threads.
        """
        def levelup(func):
            def wrapper(self, url, threads, mthreads):
                if mthreads == False or mthreads <= 0:
                    func(self, url)
                else:
                    chost = requests.head(url)
                    fsize = int(chost.headers['content-length'])
                    part = fsize // mthreads
                    threads = []
                    for thread in range(mthreads):
                        sbyte = part * thread
                        ebyte = sbyte + part
                        t = threading.Thread(target=func, kwargs={'self': self, 'url': url, 'threads': True, 'mthreads': mthreads, 'start': sbyte, 'end': ebyte})
                        threads.append(t)
                        t.start()
            return wrapper
        return levelup
    @multi_threads()
    def download(self, url, threads = False, mthreads = 0, start = 0, end = 0):
        """
        Reserve file size on disk and then download the file and fill that reserved space.
        """
        fname = url.split("/")[-1]
        if threads == True: self.headers['Range'] = f'bytes={start}-{end}'
        s = requests.Session()
        with open(fname, 'w+b') as ofile:
            with s.get(url, headers=self.headers, timeout=30, stream=True) as gfile:
                fsize = int(gfile.headers['content-length'])
                ofile.write(b'\x00' * fsize)
                ofile.seek(start)
                for chunk in gfile.iter_content(chunk_size=1024):
                    if chunk: ofile.write(chunk)
  