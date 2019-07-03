import unittest
from maxMinTestModule import TestmaxMin
from tableTestModule import Testtable
from TestChart import TestChart
from TestData import TestDataPerson


def myFitness_suite():
    suite = unittest.TestSuite()
    result = unittest.TestResult()
    suite.addTest(unittest.makeSuite(TestmaxMin))
    suite.addTest(unittest.makeSuite(Testtable))
    suite.addTest(unittest.makeSuite(TestChart))
    suite.addTest(unittest.makeSuite(TestDataPerson))
    runner = unittest.TextTestRunner()
    print(runner.run(suite))

myFitness_suite()
