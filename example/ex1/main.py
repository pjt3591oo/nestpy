import sys, os, pprint
sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/../../")

from nestpy.core import NestFactory

def bootstrap():
  appModule = ''
  app = NestFactory.create(appModule)
  print(app)

if __name__ == '__main__': 
  bootstrap()