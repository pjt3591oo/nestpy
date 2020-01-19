from mung_controller2 import MungController2
from nest import Module

@Module({
  'controller': MungController2
})
class MungModule2:
  
  def middleware(self):
    pass