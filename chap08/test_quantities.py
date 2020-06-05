import unittest
# Now doing some tricks to import the package that we know it is on chap06 
import os, pathlib, sys
cur_dir = pathlib.PurePosixPath( os.path.abspath(os.path.dirname(__file__)) )
par_dir = cur_dir.parent
dir_containing_package = os.path.join(par_dir, "chap06")
sys.path.insert(1, dir_containing_package)
import quantities

class TestQuantities(unittest.TestCase):
    def setUp(self):
        quantities.init("us")

    def test_new(self):
        q = quantities.new(12, "km")
        self.assertEqual(quantities.value(q), 12)
        self.assertEqual(quantities.units(q), "kilometer")

    def test_convert(self):
        q1 = quantities.new(12, "km")
        q2 = quantities.convert(q1, "m")
        self.assertEqual(quantities.value(q2), 12000)
        self.assertEqual(quantities.units(q2), "meter")

        q = quantities.new(12, "km")
        with self.assertRaises(ValueError):
            quantities.convert(q, "kg")

if __name__ == "__main__":
    unittest.main() 
