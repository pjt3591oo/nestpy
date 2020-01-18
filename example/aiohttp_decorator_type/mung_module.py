from mung_controller import MungController
from nest import Module

@Module({
  'controller': MungController
})
class MungModule:
  
  def middleware(self):
    pass