import unittest
from src.bitwise.operators import *

truths_2 = [[0,0],[1,0],[0,1],[1,1]]
truths_2_list1 = [0,0,1,1]
truths_2_list2 = [0, 1,0,1]
truths_3 = [[0,0,0],[0,0,1],[0,1,1],[1,1,1], [1,1,0], [1,0,0]]
truths_3_list_1 = [0,0,0,1,1,1]
truths_3_list_2 = [0,0,1,1,1,0]
truths_3_list_3 = [0,1,1,1,0,0]

class TestOperators(unittest.TestCase):
    
    #utils
    def test_isTrue(self):
        """
        returns true or false
        """
        data = [0,1]
        result = [isTrue(d) for d in data]
        self.assertEqual(result, [False, True])
        
    def test_if_(self):
        """
        returns correct value
        """
        data =[[0,0,1], [1,1,0]]
        result = [if_(a,b,c) for a,b,c in data]
        self.assertEqual(result, [1, 1])
    
    def test_and_(self):
        """
        returns correct truthtable
        """
        result = [and_(a,b) for a,b in truths_2]
        self.assertEqual(result, [0,0,0,1])

    def test_AND(self):
        """
        returns correct truthtable
        """
        result = zand(truths_2_list1, truths_2_list2)
        self.assertEqual(result, [0,0,0,1])

    def test_not_(self):
        """returns inverted value"""
        data = [1,0]
        result = [not_(i) for i in data]
        self.assertEqual(result, [0,1])

    def test_NOT(self):
        """returns correct values"""
        data = [1,0,1,0]
        result = not_map(data)
        self.assertEqual(result, [0,1,0,1])

    def test_xor(self):
        """returns correct truthtable"""
        result = [xor(a, b) for a,b in truths_2]
        self.assertEqual(result, [0,1,1,0])

    def test_XOR(self):
        """returns correct truthtable"""
        result = zexor(truths_2_list1, truths_2_list2)
        self.assertEqual(result, [0,1,1,0])

    def test_xorxor(self):
        """returns correct truthtable"""
        result = [xorxor(a,b,c) for a,b,c in truths_3]
        self.assertEqual(result, [0, 1, 0, 1, 0, 1])

    def test_XORXOR(self):
        """returns correct truthtable"""
        result = zxx(truths_3_list_1, truths_3_list_2, truths_3_list_3)
        self.assertEqual(result, [0, 1, 0, 1, 0, 1])
        
    def test_maj(self):
        """get the majority"""
        result = [majority_value(a,b,c) for a,c,b in truths_3]
        self.assertEqual(result, [0,0,1,1,1,0])
        
    def test_rotr(self):
        """rotates right in the correct way"""
        data = [1,2,3,4,5,6]
        result = crs(data, 2)
        self.assertEqual(result, [5,6,1,2,3,4])
        
    def test_shr(self):
        """shifts right in the correct way"""
        data = [1,2,3,4,5,6]
        result = lrs(data, 2)
        self.assertEqual(result, [0,0,1,2,3,4])
        
    def test_add(self):
        data_1 = [1,1,0,1]
        data_2 = [1,0,1,1]
        result = add(data_1, data_2)
        self.assertEqual(result, [1,0,0,0])