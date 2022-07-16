import os
import unittest
import numpy as np
from filegenerator import FileGenerator, time2ms, getArg, randomFromRange

class TestFileGenerator(unittest.TestCase):
    def setUp(self):
        self.gen = FileGenerator()

    def test_create(self):
        self.assertEqual(time2ms(1234.5678), 1234567)

    def test_getArg(self):
        self.assertEqual(getArg({'foo':1}, 'foo', int, 2), 1)

    def test_getArg_missing(self):
        self.assertEqual(getArg({'bar':1}, 'foo', int, 2), 2)

    def test_getArg_castStr(self):
        self.assertEqual(getArg({'bar':1}, 'foo', str, 2), 2)

    def test_getArg_castInt(self):
        self.assertEqual(getArg({'bar':'1'}, 'foo', int, 2), 2)

    def test_random_1(self):
        np.random.seed(1)
        self.assertEqual(randomFromRange(0, 1), 0.1079211674518371)

    def test_random_2(self):
        np.random.seed(1)
        self.assertEqual(randomFromRange(1, 1000), 108.81324628438526)

    def test_makeFileSize(self):
        np.random.seed(1)
        self.assertEqual(self.gen.makeFileSize(), 114077)

    def test_makeFileName(self):
        # TODO: improve
        self.assertTrue(type(self.gen.makeFileName()) == str)

    def test_createFile(self):
        filename = self.gen.makeFileName()
        filesize = self.gen.makeFileSize()
        self.assertTrue(type(filename) == str)
        self.assertFalse(os.path.exists(filename))
        file = self.gen.createFile(filename, filesize)
        self.assertTrue(os.path.exists(filename))
        self.gen.removeFile(filename)
        self.assertFalse(os.path.exists(filename))
