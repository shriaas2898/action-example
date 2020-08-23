import unittest
from AddName import test

'''
Input example
"shriaas2898" "https://github.com/shriaas2898/Julia-Learning-Notes/pull/2
https://github.com/shriaas2898/Julia-Learning-Notes/pull/1  
 https://github.com/shriaas2898/Lekhni/pull/8"

'''
class AddNameTest(unittest.TestCase):
    # Checking link is valid or not
    def test_reachable_link(self):
        username = "shriaas2898"
        links = """https://github.com/shriaas2898/Julia-Learning-Notes/pull/2
https://github.com/shriaas2898/Julia-Learning-Notes/pull/112  
 https://github.com/shriaas2898/Lekhni/pull/8"""
        self.assertNotEqual("Successfully added your contribution",test(username,links))
    
    # Checking if link is in valid format
    def test_valid_pr_link(self):
        username = "shriaas2898"
        links = """https://github.com/shriaas2898/Julia-Learning-Notes/pull/2
https://github.com/shriaas2898/ 
 https://github.com/shriaas2898/Lekhni/pull/8"""
        self.assertNotEqual("Successfully added your contribution",test(username,links))
    
    def test_valid_user(self):
        username = "shriaas2"
        links = """https://github.com/shriaas2898/Julia-Learning-Notes/pull/2
https://github.com/shriaas2898/Julia-Learning-Notes/pull/1 
 https://github.com/shriaas2898/Lekhni/pull/8"""
        self.assertNotEqual("Successfully added your contribution",test(username,links))

    def test_valid_date(self):
        username = "shriaas2898"
        links = """https://github.com/shriaas2898/Julia-Learning-Notes/pull/2
https://github.com/shriaas2898/Julia-Learning-Notes/pull/1  
 https://github.com/astrosonic/Image-Augmentation-OCR/pull/7"""
        self.assertEqual("Successfully added your contribution",test(username,links))

    