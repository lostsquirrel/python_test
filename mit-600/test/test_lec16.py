# encoding: utf-8

import unittest
from lec16 import *


class TestLec16(unittest.TestCase):

    def test_mit_person(self):
        p1 = MITPerson('Smith','Fred')
        self.assertEqual(p1.get_id_num(), 0)
        p2 = MITPerson('Foobar','Jane')
        self.assertEqual(p2.get_id_num(), 1)

    def test_ug(self):
        pr = Person("Grimson", "Eric")
        ug = UG('Doe', 'Jane')
        self.assertTrue(pr > ug)

    def test_prof(self):
        pr = Prof('Grimson', 'Eric', 'Full')
        lectures = {'F08': ['6.00'], 'S09': ['6.00'], 'S0x': ['6.xxx']}
        pr.add_teaching('F08', '6.00')
        pr.add_teaching('S09', '6.00')
        pr.add_teaching('S0x', '6.xxx')
        self.assertEqual(pr.get_teaching('F08'), ['6.00'])
        self.assertEqual(pr.get_teaching('S09'), ['6.00'])
        self.assertEqual(pr.get_teaching('S0x'), ['6.xxx'])
        self.assertEqual(pr.teaching, lectures)