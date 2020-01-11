import sys, os, pprint
sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/../../")

from nestpy.common.Module import Module
from example.ex1.service import AppService

@Module({
  "imports": [],
  "providers": [{
    "name": "AppService",
    "provider": AppService
  }],
  "exports": [],
  "controllers": []
})
class AppModule :
  def __init__(self):
    pass