import unittest
import pandas as pd
from myfitness.summary import table
 
class Testtable(unittest.TestCase):
    
    @classmethod                            
    def setUpClass(cls):
        print("Starting Testtable")
    
    def setUp(self):
        super().setUp()
        testdata2 = {'Start': ['2017-02-12 0:00','2017-03-07 0:00' , '2017-02-14 0:00', '2017-03-05 0:00', '2017-03-06 0:00', '2017-04-20 0:00', '2017-04-21 0:00', '2017-02-13 0:00','2017-04-22 0:00', '2017-04-23 0:00'],
            'Finish': ['2017-02-13 0:00','2017-03-08 0:00', '2017-02-15 0:00', '2017-03-06 0:00', '2017-03-07 0:00', '2017-04-21 0:00', '2017-04-22 0:00', '2017-02-14 0:00', '2017-04-23 0:00', '2017-04-24 0:00'],
            'Distance (mi)': [0.559,2.225,1.422,1.0797,2.614,3.295,2.276,2.591,3.995,2.611],
            'Steps (count)': [1180, 4673, 3055, 2365, 5270, 6820, 4751, 5353, 9647, 6806]}
        self.testdf2 = pd.DataFrame(testdata2)
        print(self.__class__())

    def test_table(self):
        febsteps = (1180+5353+3055)/3
        marsteps = (2365+5270+4673)/3
        aprsteps = (6820+4751+9647+6806)/4
        testtable = table.summary_data(self.testdf2)
        # Validate the date string was changed to datetime
        self.assertEqual(testtable.index.dtype, 'datetime64[ns]')
        # Verify the shape of the table
        self.assertEqual(testtable.shape, (3,1))
        # Verify the dates are sorted
        self.assertTrue(testtable.index[0]<testtable.index[1])
        self.assertTrue(testtable.index[1]<testtable.index[2])
        # Verify the values were calculated correctly
        self.assertEqual(testtable.steps.values[0], febsteps)
        self.assertEqual(testtable.steps.values[1], marsteps)
        self.assertEqual(testtable.steps.values[2], aprsteps)
        # Verify Except statement by changing one of the values for Steps to a string:
        self.testdf2.loc[4, 'Steps (count)'] = '5270'
        testtable = table.summary_data(self.testdf2)
        self.assertEqual(testtable.steps.values[2], aprsteps)
        
    def tearDown(self):
        del self.testdf2
        super().tearDown()        
    
    @classmethod
    def tearDownClass(cls):
        print("Testtable completed")   

# For Jupyter notebook and Coverage on the module only:
# unittest.main(argv=[''], verbosity=2, exit=False)