import unittest

from src.MapMgr.GenerateMap import GenerateMap

from src.MapMgr.ProcessMap import ProcessMap



class Test(unittest.TestCase):


    def setUp(self):
        self.graph = GenerateMap().generateMap('Amherst', 'MA')


    def tearDown(self):
        pass

# 
    def testInValidLocation(self):
        self.assertFalse(ProcessMap().isLocationValid(self.graph, float('inf'), float('inf')))
          
    def testIsValidLocation(self):
        location = 'umass,amherst,ma'
        params = ProcessMap().getLocationParams(location)
        self.assertTrue(ProcessMap().isLocationValid(self.graph, params['latitude'], params['longitude']))
         
    def testIsPathValid(self):
        pass 
    
    def testDjstkraValidPath(self):
        pass 
    
    def testName(self):
        pass


if __name__ == "__main__":
    unittest.main()