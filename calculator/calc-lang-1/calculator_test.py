#!/usr/bin/env python3
import unittest
import calculator as calc

class TestCases(unittest.TestCase):
    def test_expr_positive(self):
        """
        Test positive test cases for expressions.
        """
        testcases = [
                ("10 + 10", "20.0"),
                ("10.0+.1", "10.1"),
                ("10**2", "100.0"),
                ("10**2**3", "100000000.0"),
                ("9+2*3" , "15.0"),
                ("9+3/2" , "10.5"),
                ("9+10-9-5", "5.0"),
                ("9+10-(9-5)", "15.0"),
                ]

        for key, val in testcases:
            ok, value, err = calc.calculate(key)
            self.assertTrue(err == None)
            self.assertTrue(val == str(value))
            
    def test_stmt_positive(self):
        """
        Test positive test cases for the variable, assignments and their value.
        """
        testcases = [
                ("10", "10.0"),
                ("_", "10.0"),
                ("10 * 3**2", "90.0"),
                ("_", "90.0"),
                ("x=_", "90.0"),
                ("y=2**6", "64.0"),
                ("x+y", "154.0"),
                ]

        for key, val in testcases:
            # print(key, val)
            ok, value, err = calc.calculate(key)
            # print(val, value)
            self.assertTrue(err == None)
            self.assertTrue(val == str(value))


if __name__ == '__main__':
    unittest.main()
