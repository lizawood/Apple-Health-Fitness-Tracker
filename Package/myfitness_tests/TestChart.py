import unittest
import pandas as pd
import pygal 
from IPython.display import SVG, display


from myfitness.healthdata import chart

class TestChart (unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        print("Starting TestChart")
        cls.columnX = ['A','B','C','D','E']
        cls.columnY = [1,2,3,4,5]
        cls.testchart = chart.chart(cls.columnX, cls.columnY, 'letters', 'numbers', 'my_fitness_chart')

    def setUp(self):
        super().setUp()
        print(self.__class__())

    def test_chart(self): 
        #do chart tests here 
        
        # Checking try and except in chart
        self.assertFalse(chart.chart(self.columnX, self.columnX, 'letters', 'numbers'))
        
        # Check pygal chart
        self.assertIsInstance(self.testchart, pygal.Bar)
        
        # Check title
        self.assertEqual(self.testchart.title, 'My Fitness Chart')
        
        # Check x_title
        self.assertEqual(self.testchart.x_title, 'letters')
        
        # Check y_title
        self.assertEqual(self.testchart.y_title, 'numbers')
        
        # Check x_labels
        self.assertEqual(self.testchart.x_labels, ['A','B','C','D','E'])
        
        # Checking try and except in filename
        self.assertFalse(chart.chart(self.columnX, self.columnY, 'letters', 'numbers'))
        
    def tearDown(self):
        super().tearDown()
            
    @classmethod
    def tearDownClass(cls):
        del(cls.testchart)
        print("Finished TestChart")
