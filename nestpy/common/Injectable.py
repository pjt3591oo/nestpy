def Injectable(class_):
  ''' 
  service로 사용되는 Injectable 데코레이터를 이용하여 싱글톤 객체를 생성한다
  '''


  class class_w(class_):
    _instance = None
    _sealed = False  # TODO: 데코레이터에 전달되는 클래스별로 싱글톤 관리할 수 있도록 처리한다 _sealed = {class_.__name__: True, False}로 처리하면 됨.
  
    def __new__(class_, *args, **kwargs):
      
      if class_w._instance is None:
          class_w._instance = super(class_w, class_).__new__(class_)
          class_w._instance._sealed = False
      return class_w._instance
  
    def __init__(self, *args, **kwargs):
      if self._sealed:
        return
      super(class_w, self).__init__(*args, **kwargs)
      self._sealed = True
  
  class_w.__name__ = class_.__name__

  return class_w