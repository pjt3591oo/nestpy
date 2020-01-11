def Module(*args, **kwargs):
  class Module:
    def __init__(self, original_function):
      self.providers = args[0].get('providers', [])
      self.imports = args[0].get('imports', [])
      self.exports = args[0].get('exports', [])
      self.controllers = args[0].get('controllers', [])

      self.create_providers_instance()

      self.original_function = original_function
    
    def __call__(self, *args, **kwargs):
      return self.original_function(*args, **kwargs)


    def create_providers_instance(self):
      
      return { 
        provider['name']: provider['provider']()
        for provider in self.providers 
      }

  return Module