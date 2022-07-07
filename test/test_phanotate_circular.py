#!/usr/bin/env python3

import unittest
import os.path

import extern

path_to_script = os.path.join(os.path.dirname(os.path.realpath(__file__)),'..','bin','phanotate_circular')

class Tests(unittest.TestCase):
    maxDiff = None

    def test_hello_world(self):
        self.assertEqual(1, 1)

if __name__ == "__main__":
    unittest.main()
