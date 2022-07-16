import unittest
from tests.filegenerator_tests import TestFileGenerator

if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(TestFileGenerator('test_create'))
    suite.addTest(TestFileGenerator('test_getArg'))
    suite.addTest(TestFileGenerator('test_getArg_missing'))
    suite.addTest(TestFileGenerator('test_getArg_castStr'))
    suite.addTest(TestFileGenerator('test_getArg_castInt'))
    suite.addTest(TestFileGenerator('test_random_1'))
    suite.addTest(TestFileGenerator('test_random_2'))
    suite.addTest(TestFileGenerator('test_makeFileSize'))
    suite.addTest(TestFileGenerator('test_makeFileName'))
    suite.addTest(TestFileGenerator('test_createFile'))
    unittest.TextTestRunner().run(suite)
