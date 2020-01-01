import unittest
import sys, os, pprint
sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/../../")

from nestpy.common.Injectable import Injectable

@Injectable
class Test:
  def __init__(self):
    pass


class InjectableTestCase1(unittest.TestCase):

  def test_instance_check_case(self):
    t1 = Test()
    t2 = Test()
    
    self.assertEqual(id(t1), id(t2))

if __name__ == "__main__":
  unittest.main()