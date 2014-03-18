#!/usr/bin/python3

import unittest

all_tests = unittest.TestLoader().discover('unit_tests', pattern='test_*.py')
unittest.TextTestRunner().run(all_tests)
