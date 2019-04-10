import unittest
from lab1 import *

 # A few test cases.  Add more!!!
class TestLab1(unittest.TestCase):

    def test_max_list_iter(self):
        """add description here"""
        tlist = None
        with self.assertRaises(ValueError):  # used to check for exception
            max_list_iter(tlist)
        self.assertEqual(max_list_iter([2, 4, 6, 9, 1, 3, 7]), 9)
        self.assertEqual(max_list_iter([9,9,9,9,9]), 9)
        self.assertEqual(max_list_iter([]),0)
        longlist = [6, 25, 96, 21, 39, 5, 202, 757, 911, 951, 69, 420]
        self.assertEqual(max_list_iter(longlist),951)
        self.assertEqual(max_list_iter([10,12,9,9,10,10,13,12,13]),13)

    def test_reverse_rec(self):
        self.assertEqual(reverse_rec([1,2,3]),[3,2,1])
        self.assertEqual(reverse_rec([]),[])
        self.assertEqual(reverse_rec([6,1,9,]),[9,1,6])
        longlist = [6, 25, 96, 21, 39, 5, 202, 757, 911, 951, 69, 420]
        revlist = [420, 69, 951, 911, 757, 202, 5, 39, 21, 96, 25, 6]
        self.assertEqual(reverse_rec(longlist),revlist)
        tlist = None
        with self.assertRaises(ValueError):
            reverse_rec(tlist)
        
    def test_bin_search(self):
        list_val =[0,1,2,3,4,7,8,9,10]
        low = 0
        high = len(list_val)-1
        self.assertEqual(bin_search(4, 0, len(list_val)-1, list_val), 4 )
        list_vala = [2,4,6,8,10]
        low = 0
        self.assertEqual(bin_search(6,low, len(list_vala)-1,list_vala),2) 
        listn = [3,5,9,10]
        self.assertEqual(bin_search(7,0,len(listn)-1,listn),None)
        with self.assertRaises(ValueError):
            bin_search(1,0,9,None)
        self.assertEqual(bin_search(1,0,1,[]),None)
if __name__ == "__main__":
        unittest.main()

    
