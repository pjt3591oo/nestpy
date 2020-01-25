from aiohttp import web
from functools import wraps 
from utils import log_style
import types, os
from pathlib import Path

PATHS = {}
CONTROLLER_MAPS = {}

def Get(path):
  def params(func):
    class_name = str(func).split('.')[0].split('function ')[1].strip()
    PATHS.setdefault(class_name, [])
    PATHS[class_name].append({
        "path": path if len(path) > 1 else '',
        "handle": func,
        "method": "get"
    })

    @wraps(func)
    def __wrapper(*args, **kwargs):
      this = args[0]
      req = args[1]
      return func(this, req)
    return __wrapper
  return params

def Post(path):
  def params(func):
    class_name = str(func).split('.')[0].split('function ')[1].strip()
    PATHS.setdefault(class_name, [])
    print('Post Class Name', class_name)
    PATHS[class_name].append({
        "path":  path if len(path) > 1 else '',
        "handle": func,
        "method": "post"
    })
    
    @wraps(func)
    def __wrapper(*args, **kwargs):
      this = args[0]
      req = args[1]
      return func(this, req)
    return __wrapper
  return params

def Controller(path):
  def params(func):
    func.path = path
    CONTROLLER_MAPS[func.__name__] = func()
    
    @wraps(func)
    def __wrapper(*args, **kwargs):
      return func(*args, **kwargs)
    return __wrapper

  return params

def Module(option):
  controllers = option.get('controllers', [])
  imports = option.get('imports', [])
  exports = option.get('exports', [])
  providers = option.get('providers', [])
  
  if not type(controllers) == types.FunctionType and not len(controllers):
    def _func(func):
      func.imports = imports
      @wraps(func)
      def __wrapper(*args, **kwargs):
        return func(*args, **kwargs)

      return __wrapper

    return _func

  else:
    def _func(func):
      if not hasattr(func, 'controllers') or not isinstance(func.controllers, list):
        func.controllers =  []

      func.controllers.append(controllers)
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
    
    for root_import_of_module in self.root_module.imports:
      for controller in root_import_of_module.controllers:
        
        paths = PATHS[controller.__name__]
        controller_instance = controller()
        
        for path in paths:
          base_path = controller.path
          method = path['method'].upper()
          handle = path['handle']
          p = os.path.join(base_path, path['path'])
          
          if len(p) > 1:
            if p[-1] == '/':
              p =p[0:-1]
          else:
            p = ''

          print(log_style.GREEN("[Nest] -   ") + log_style.YELLOW("[RouterExplorer] ") + log_style.GREEN("Mapped {%s %s} route (%s)"%(p, method, controller.__name__)))
     
          if method == 'GET':
            self.routes_map.append(web.get(p, getattr(controller_instance, handle.__name__) ))
          elif method == 'POST':
            self.routes_map.append(web.post(p, getattr(controller_instance, handle.__name__)))

    

    print(log_style.WHITE(''))
    return self

  def start(self, port):
    print(log_style.GREEN("[Nest] -   ") + log_style.YELLOW("[NestFactory]    ") + log_style.GREEN("Started Nest Application"))
    print(log_style.WHITE(''))

    self.app.add_routes(self.routes_map)
    web.run_app(self.app, port=port)