#!/usr/bin/env python
#
# runserver.py : run server
#
import multiprocessing, os
from appname.customapplication import MyCustomApplication

DEBUG = int(os.environ["DEBUG"])
port = int(os.environ.get('PORT',5000))
host = '127.0.0.1' if DEBUG else '0.0.0.0'

if __name__ == "__main__":
    options = {
        'bind': '%s:%d' % (host,port),
        'workers': multiprocessing.cpu_count() * 2 + 1
    }

    MyCustomApplication(options).run()
