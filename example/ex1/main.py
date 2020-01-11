import sys, os, pprint
sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/../../")

from nestpy.core import NestFactory

from example.ex1.module import AppModule

def bootstrap():
  app = NestFactory.create(AppModule)

if __name__ == '__main__': 
  bootstrap()