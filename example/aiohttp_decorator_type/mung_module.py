from mung_controller import MungController
from nest import Module

def a():
  print('hello world hahahahahahahahahahaha')

@Module({
  'controllers': MungController,
  'providers': [
    {
      'provider': 'test',
      'useValue': 111111111
    }, {
      'provider': 'test1',
      'useClass': a
    } 
  ]
})
class MungModule:
  
  def middleware(self):
    pass