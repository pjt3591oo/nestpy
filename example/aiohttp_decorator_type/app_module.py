from nest import Module

from mung_module import MungModule
from mung_module2 import MungModule2

@Module({
  'import': [
    MungModule,
    MungModule2
  ]
})
class AppModule:

  def middleware(self):
    pass