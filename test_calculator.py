import unittest
from calculator import StringCalculator

class TestStringCalculator(unittest.TestCase):
    def setUp(self):
        self.calculator = StringCalculator()

    def test_can_call_method_with_an_empty_string(self):
        try:
            self.calculator.add()
        except TypeError:
            pass
        except:
            self.fail('Method should not be callable without an argument')

    def test_when_empty_string_is_passed_it_returns_zero(self):
        self.assertEqual(0, self.calculator.add(''))

    def test_when_zero_is_passed_as_string_it_returns_zero(self):
        self.assertEqual(0, self.calculator.add('0'))

    def test_when_42_is_passed_as_string_it_returns_42(self):
        self.assertEqual(42, self.calculator.add('42'))

    def test_when_99_is_passed_it_returns_99(self):
        self.assertEqual(99, self.calculator.add('99'))

    def test_when_3_and_5_are_passed_it_returns_8(self):
        self.assertEqual(8, self.calculator.add('3,5'))

    def test_when_12_and_99_are_passed_it_returns_11(self):
        self.assertEqual(111, self.calculator.add('12,99'))

    def test_when_3_integers_are_passed_it_returns_their_sum(self):
        self.assertEqual(6, self.calculator.add('1,2,3'))

    def test_when_6_integers_are_passed_it_returns_their_sum(self):
        self.assertEqual(21, self.calculator.add('1,2,3,4,5,6'))

    def test_when_3_and_5_are_passed_separated_by_a_new_line_it_returns_8(self):
        self.assertEqual(8, self.calculator.add('3\n5'))

    def test_when_numbers_with_custom_delimiter_is_provided_then_it_returns_their_sum(self):
        self.assertEqual(12, self.calculator.add('//;\n4,4;2,1\n1'))

    def test_when_negative_numbers_are_passed_it_raises_an_exception_giving_those_numbers(self):
        self.assertRaisesRegex(ValueError, "negatives not allowed: -3, -9", self.calculator.add, '2,-3,6,-9')

    def test_when_numbers_greater_than_1000_are_passed_they_are_ignored(self):
        self.assertEqual(1042, self.calculator.add('42,1000,1001,2000'))

    def test_it_works_with_one_delimiter_between_square_brackets(self):
        self.assertEqual(8, self.calculator.add('//[banana]\n3banana5'))
        self.assertEqual(6, self.calculator.add('//[***]\n1***2***3'))

    def test_it_works_with_several_delimiters_between_square_brackets(self):
        self.assertEqual(21, self.calculator.add('//[;][__]\n7;7__7'))
        self.assertEqual(6, self.calculator.add('//[*][%]\n1*2%3'))

if __name__ == '__main__':
    unittest.main()