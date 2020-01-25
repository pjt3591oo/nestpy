import sys, os, pprint
sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/../../")

from nestpy.common.Injectable import Injectable

@Injectable
class AppService:
  def __init__(self, *args, **kwargs):
    self.a = 1000

  def get_data(self):
    # print(self.a)
    pass