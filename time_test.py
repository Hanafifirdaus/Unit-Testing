import time
import timeout_decorator
import unittest

class timeoutTest(unittest.TestCase):

   @timeout_decorator.timeout(5)
   def testtimeout(self):
      print("Start")
   for i in range(1,4):
      time.sleep(1)
      print("%d seconds have passed" % i)
      
if __name__ == '__main__':
   unittest.main()