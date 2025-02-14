import unittest
from unittest.mock import patch
import sys, os
from colorama import init, Fore, Style

init(autoreset=True)
# Add the src directory to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../")))

from src.ex_01_madlibs import Madlibs, GetUserInputs

sample_data = {
    "nouns": ["dog", "cat", "bird", "fish"],
    "verbs": ["run", "jump", "swim", "dance"],
    "adjectives": ["happy", "sad", "angry", "excited"],
}


class TestMadlibs(unittest.TestCase):
    def setUp(self):
        self.sample_data = sample_data
        self.number = 4
        self.madlibs = Madlibs(self.number)

        # Append sample data to the madlibs instance
        for cat in self.sample_data:
            for word in self.sample_data[cat]:
                self.madlibs.append_to_data(cat, word)

    def test_append_to_data(self):
        """Test that data is appended correctly to each category."""
        for cat in self.sample_data:
            self.assertEqual(
                self.madlibs.data[cat],
                self.sample_data[cat],
                f"{Fore.RED}Data mismatch in category '{cat}'{Style.RESET_ALL}",
            )

    @patch("random.randrange", side_effect=lambda start, end: start)
    def test_generate_lib_no_shuffle(self, mock_randrange):
        """Test generate_lib method when random shuffle is disabled."""
        expected_sentences = [
            f"One {self.sample_data['nouns'][i]} {self.sample_data['verbs'][i]} quite {self.sample_data['adjectives'][i]}"
            for i in range(self.number)
        ]
        result = self.madlibs.generate_lib()
        self.assertEqual(
            result,
            expected_sentences,
            f"{Fore.RED}Generated sentences do not match expected output without shuffle.{Style.RESET_ALL}",
        )

    def test_generate_lib_with_shuffle(self):
        with patch(
            "random.randrange",
            side_effect=[
                0,
                0,
                0,
                1,
                1,
                1,
                2,
                2,
                2,
                3,
                3,
                3,
            ],
        ) as mock_randrange:
            """Test generate_lib method with a predefined shuffle."""
            shuffled_data = {
                "nouns": ["dog", "cat", "bird", "fish"],
                "verbs": ["run", "jump", "swim", "dance"],
                "adjectives": ["happy", "sad", "angry", "excited"],
            }
            expected_sentences = [
                f"One {shuffled_data['nouns'][i]} {shuffled_data['verbs'][i]} quite {shuffled_data['adjectives'][i]}"
                for i in range(self.madlibs.number)
            ]
            result = self.madlibs.generate_lib()
            self.assertEqual(
                result,
                expected_sentences,
                f"{Fore.RED}Generated sentences do not match expected output with shuffle.{Style.RESET_ALL}",
            )


class TestGetUserInputs(unittest.TestCase):
    def setUp(self):
        self.static_list = sample_data
        self.auto = True

    @patch("builtins.input", return_value="4")
    def test_init_with_auto(self, mock_input):
        """Test initialization with AUTO=True"""
        gui = GetUserInputs(self.auto, self.static_list)
        self.assertEqual(
            gui.madlibs.number,
            4,
            "Number of sentences should be 4 as specified by AUTO.",
        )
        self.assertEqual(
            gui.static_list,
            self.static_list,
            "Static list does not match expected value.",
        )
        self.assertTrue(gui.auto, "AUTO should be True.")

    @patch("builtins.input", return_value="3")
    def test_init_without_auto(self, mock_input):
        """Test initialization with AUTO=False"""
        gui = GetUserInputs(False, self.static_list)
        self.assertEqual(
            gui.madlibs.number, 3, "Number of sentences should be 3 as inputted."
        )
        self.assertEqual(
            gui.static_list,
            self.static_list,
            "Static list does not match expected value.",
        )
        self.assertFalse(gui.auto, "AUTO should be False.")

    @patch(
        "builtins.input",
        side_effect=[
            4,
            "dog",
            "cat",
            "bird",
            "fish",  # nouns
            "run",
            "jump",
            "swim",
            "dance",  # verbs
            "happy",
            "sad",
            "angry",
            "excited",  # adjectives
        ],
    )
    def test_get_inputs_without_auto(self, mock_input):
        """Test get_inputs method with AUTO=False"""
        gui = GetUserInputs(False, self.static_list)
        gui.get_inputs()
        expected_data = {
            "nouns": ["dog", "cat", "bird", "fish"],
            "verbs": ["run", "jump", "swim", "dance"],
            "adjectives": ["happy", "sad", "angry", "excited"],
        }
        self.assertEqual(
            gui.madlibs.data,
            expected_data,
            "Madlibs data does not match expected user inputs.",
        )

    def test_get_inputs_with_auto(self):
        """Test get_inputs method with AUTO=True"""
        gui = GetUserInputs(self.auto, self.static_list)
        gui.get_inputs()
        self.assertEqual(
            gui.madlibs.data,
            self.static_list,
            "Madlibs data should match STATIC_LIST when AUTO is True.",
        )

    @patch("builtins.input", return_value="3")
    def test_print_madlib(self, mock_input):
        """Test print_madlib method"""
        gui = GetUserInputs(self.auto, self.static_list)
        gui.get_inputs()
        with patch("builtins.print") as mock_print:
            gui.print_madlib()
            self.assertTrue(mock_print.called, "print_madlib should call print.")


if __name__ == "__main__":
    unittest.main()
