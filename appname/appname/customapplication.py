# customapplication
#
# wrapper class for running app through Gunicorn
#
from gunicorn.app.base import Application
from gunicorn import util

class MyCustomApplication(Application):
    '''
    Custom Gunicorn Application
    '''

    def __init__(self, options={}):
        '''__init__ method

        Load the base config and assign some core attributes.
        '''
        self.usage = None
        self.callable = None
        self.options = options
        self.do_load_config()

    def init(self, *args):
        '''init method

        Takes our custom options from self.options and creates a config
        dict which specifies custom settings.
        '''
        cfg = {}
        for k, v in self.options.items():
            if k.lower() in self.cfg.settings and v is not None:
                cfg[k.lower()] = v
        return cfg

    def load(self):
        '''load method

        Imports our application and returns it to be run.
        
        FORMAT: <module>:<WSGI object>
        
        If the WSGI object is not named 'application', it must
        be included in the function parameter.
        '''        
        return util.import_app("appname.main:app")
