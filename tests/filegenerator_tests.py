import os
import unittest
import numpy as np
from filegenerator import FileGenerator
from utils import getArg, randomFromRange

ROOT = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
SOURCE_DIRECTORY = 'in'

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
        np.random.seed()
        file_name = self.gen.makeFileName()
        file_size = self.gen.makeFileSize()
        file_path = os.path.join(ROOT, SOURCE_DIRECTORY, file_name)
        self.assertTrue(type(file_name) == str)
        self.assertFalse(os.path.exists(file_path))
        self.gen.createFile(file_name, file_size)
        self.assertTrue(os.path.exists(file_path))
        self.gen.removeFile(file_name)
        self.assertFalse(os.path.exists(file_path))
