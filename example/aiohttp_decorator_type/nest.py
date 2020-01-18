from aiohttp import web
from functools import wraps 
from utils import log_style

PATHS = []

def Get(path):
  def params(func):
    PATHS.append({
        "path": path,
        "handle": func,
        "method": "get"
    })
    
    @wraps(func)
    def __wrapper(self, *args, **kwargs):
      return func(self, *args, **kwargs)
    return __wrapper
  return params

def Post(path):
  def params(func):
    PATHS.append({
        "path": path,
        "handle": func,
        "method": "post"
    })
    
    @wraps(func)
    def __wrapper(self, *args, **kwargs):
      return func(self, *args, **kwargs)
    return __wrapper
  return params

def Controller(func):
  @wraps(func)
  def __wrapper(*args, **kwargs):
    return func(*args, **kwargs)
  return __wrapper

def Module(option):
  controller = option['controller']()
  def _func(func):
    func.controller = controller
    @wraps(func)
    def __wrapper(*args, **kwargs):
      return func(*args, **kwargs)

    return __wrapper
  return _func

class NestFactory:
  def __init__(self, root_module):
    print(log_style.GREEN("[Nest] -   ") + log_style.YELLOW("[NestFactory]    ") + log_style.GREEN("Starting Nest Application"))
    self.root_module = root_module
    self.app = web.Application()
    self.routes_map = []

  def create(self):
    self.root_module = self.root_module()

    for path in PATHS:
      p = path['path']
      handle = path['handle']
      method = path['method'].upper()

      print(log_style.GREEN("[Nest] -   ") + log_style.YELLOW("[RouterExplorer] ") + log_style.GREEN("Mapped {%s %s} route"%(p, method, )))

      if method == 'GET':
        self.routes_map.append(web.get(p, getattr(self.root_module.controller, handle.__name__)))
      elif method == 'POST':
        self.routes_map.append(web.post(p, getattr(self.root_module.controller, handle.__name__)))
    return self

  def start(self, port):
    web.run_app(self.app)