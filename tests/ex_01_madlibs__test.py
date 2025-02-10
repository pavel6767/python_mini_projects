import unittest
from unittest.mock import patch, MagicMock
import sys
import os

# Add the src directory to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))

from ex_01_madlibs import Madlibs

class TestMadlibs(unittest.TestCase):

    @patch('builtins.input', lambda *args: 'test')  # Mock input function
    def setUp(self):
        self.number = 4
        self.madlibs = Madlibs(self.number)

    # def test_init(self):
    #     self.assertEqual(self.madlibs.number, self.number)
    #     self.assertEqual(self.madlibs.list, ['verbs', 'adjectives', 'nouns'])
    #     self.assertEqual(self.madlibs.verbs, [])
    #     self.assertEqual(self.madlibs.adjectives, [])
    #     self.assertEqual(self.madlibs.nouns, [])

    @patch('random.randrange', return_value=0)
    def test_get_inputs_verbs(self, mock_randrange):
        self.madlibs.get_inputs('verbs')
        self.assertEqual(self.madlibs.verbs, ['flew', 'drew', 'flew', 'flew'])

    @patch('random.randrange', return_value=0)
    def test_get_inputs_adjectives(self, mock_randrange):
        self.madlibs.get_inputs('adjectives')
        self.assertEqual(self.madlibs.adjectives, ['pretty', 'tired', 'pretty', 'pretty'])

    @patch('random.randrange', return_value=0)
    def test_get_inputs_nouns(self, mock_randrange):
        self.madlibs.get_inputs('nouns')
        self.assertEqual(self.madlibs.nouns, ['house', 'car', 'house', 'house'])

    @patch('Madlibs.get_inputs')
    def test_get_all_inputs(self, mock_get_inputs):
        self.madlibs.get_all_inputs()
        self.assertEqual(mock_get_inputs.call_count, 3)
        mock_get_inputs.assert_any_call('verbs')
        mock_get_inputs.assert_any_call('adjectives')
        mock_get_inputs.assert_any_call('nouns')

    def test_generate_lib(self):
        self.madlibs.nouns = ['house', 'car', 'banana', 'phone']
        self.madlibs.verbs = ['flew', 'drew', 'fainted', 'drove']
        self.madlibs.adjectives = ['pretty', 'tired', 'joyful', 'fast']
        expected_output = [
            "One house flew quite pretty",
            "One car drew quite tired",
            "One banana fainted quite joyful",
            "One phone drove quite fast"
        ]
        self.assertEqual(self.madlibs.generate_lib(), expected_output)

if __name__ == '__main__':
    unittest.main()
