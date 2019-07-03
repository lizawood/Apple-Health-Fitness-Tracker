import unittest
import pandas as pd
from myfitness.summary import maxmin
 
class TestmaxMin(unittest.TestCase):
   
    @classmethod                            
    def setUpClass(cls):
        print("Starting TestmaxMin")
      
    def setUp(self):
        super().setUp()
        testdata = {'Start': ['2017-02-12 0:00', '2017-02-13 0:00', '2017-02-14 0:00', '2017-03-05 0:00', '2017-03-06 0:00', '2017-03-07 0:00', '2017-04-20 0:00', '2017-04-21 0:00', '2017-04-22 0:00', '2017-04-23 0:00'],
                    'Finish': ['2017-02-13 0:00', '2017-02-14 0:00' , '2017-02-15 0:00', '2017-03-06 0:00', '2017-03-07 0:00', '2017-03-08 0:00', '2017-04-21 0:00', '2017-04-22 0:00', '2017-04-23 0:00', '2017-04-24 0:00'],
                    'Distance (mi)': [0.559,2.591,1.422,1.0797,2.614,2.225,3.295,2.276,3.995,2.611],
                    'Steps (count)': [1180, 5353, 3055, 2365, 5270, 4673, 6820, 4751, 9647, 6806]}
        self.testdf = pd.DataFrame(testdata)
        print(self.__class__())

    def test_getMax(self):
        maxref = pd.Series({'Start': '2017-04-22 0:00', 'Finish': '2017-04-23 0:00', 'Distance (mi)': 3.995, 'Steps (count)': 9647})
        # Verify the datatype 'object' is returned
        self.assertEqual(maxmin.getMax(self.testdf).dtypes, 'O' ) 
        # Verify Start value for index with max steps
        self.assertEqual(maxmin.getMax(self.testdf).loc['Start'],maxref.loc['Start'])
        # Verify Finish value for index with max steps
        self.assertEqual(maxmin.getMax(self.testdf).loc['Finish'],maxref.loc['Finish'])
        # Verify Distance value for index with max steps
        self.assertEqual(maxmin.getMax(self.testdf).loc['Distance (mi)'],maxref.loc['Distance (mi)'])
        # Verifty maximum steps were correctly found
        self.assertEqual(maxmin.getMax(self.testdf).loc['Steps (count)'],maxref.loc['Steps (count)'])
        # Verify Except statement by changing one of the values for Steps to a string:
        self.testdf.loc[3, 'Steps (count)'] = '2365'
        self.assertEqual(maxmin.getMax(self.testdf).loc['Steps (count)'],maxref.loc['Steps (count)'])
        
    def test_getMin(self):
        minref = pd.Series({'Start': '2017-02-12 0:00', 'Finish': '2017-02-13 0:00', 'Distance (mi)': 0.559,'Steps (count)': 1180})
        # Verify the datatype 'object' is returned
        self.assertEqual(maxmin.getMin(self.testdf).dtypes, 'O') 
        # Verify Start value for index with max steps
        self.assertEqual(maxmin.getMin(self.testdf).loc['Start'],minref.loc['Start'])
        # Verify Finish value for index with max steps
        self.assertEqual(maxmin.getMin(self.testdf).loc['Finish'],minref.loc['Finish'])
        # Verify Distance value for index with max steps
        self.assertEqual(maxmin.getMin(self.testdf).loc['Distance (mi)'],minref.loc['Distance (mi)'])
        # Verifty maximum steps were correctly found
        self.assertEqual(maxmin.getMin(self.testdf).loc['Steps (count)'],minref.loc['Steps (count)'])
        # Verify Except statement by changing one of the values for Steps to a string:
        self.testdf.loc[4, 'Steps (count)'] = '5270'
        self.assertEqual(maxmin.getMin(self.testdf).loc['Steps (count)'],minref.loc['Steps (count)'])
    
    def tearDown(self):
        del self.testdf
        super().tearDown
    
    @classmethod
    def tearDownClass(cls):
        print ("TestmaxMin completed")

# For Jupyter notebook and checking Coverage on the module only:
# unittest.main(argv=[''], verbosity=2, exit=False)