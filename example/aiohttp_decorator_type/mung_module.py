from mung_controller import MungController
from nest import Module

@Module({
  'controllers': MungController
})
class MungModule:
  
  def middleware(self):
    pass