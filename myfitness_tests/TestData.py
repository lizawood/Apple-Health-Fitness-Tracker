import unittest
import pandas as pd

from myfitness.healthdata import data

class TestDataPerson(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        print("Starting TestData")
        cls.p1 = data.Person('Liza', 30, 'F')
        cls.healthdata_p1 = data.healthdata('Liza', 30, 'F', 'Health Data.csv')
        cls.healthdata_p2 = data.healthdata('Liza', 'Y', 'F', '')
        
    def setUp(self):
        super().setUp()
        print(self.__class__())

    def test_data(self): 
        #Tests for data module
        
        #Check that the name is Liza
        self.assertEqual(self.p1.name, 'Liza')
        
        #Check age is 30
        self.assertEqual(self.p1.age, 30)
        
        #Check gender is F
        self.assertEqual(self.p1.gender, 'F')
        
        #Check display
        self.assertEqual(self.p1.display(), 'Name: Liza, Age: 30, Gender: F')
        
        #Check healthdata file
        self.assertEqual(self.healthdata_p1.file, 'Health Data.csv')
        
        #Check data import 
        self.assertIsInstance(self.healthdata_p1.data(), pd.DataFrame)
        
        #Check that the age is an integer
        self.assertEqual(self.healthdata_p2.age, None)
        
        #Check that file exists
        self.assertFalse(self.healthdata_p2.data())
        
    def tearDown(self):
        super().tearDown()
            
    @classmethod
    def tearDownClass(cls):
        del(cls.p1)
        del(cls.healthdata_p1)
        del(cls.healthdata_p2)
        print("Finished TestData")
        