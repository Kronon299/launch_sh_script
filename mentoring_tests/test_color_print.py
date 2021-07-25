from unittest import TestCase

from decorators.color_print import color_print_method


class TestColorPrintMethod(TestCase):

    def test_wrapper_name(self):
        @color_print_method('blue')
        def test_func():
            pass

        expected_result = "test_func"
        actual_result = test_func.__name__
        self.assertEqual(expected_result, actual_result)

    def test_return_coloring_right_color_lower_case(self):
        @color_print_method('magenta')
        def test_func():
            return 'magenta'

        expected_result = "\x1b[35mmagenta\x1b[0m"
        actual_result = test_func()
        self.assertEqual(expected_result, actual_result)

    def test_return_coloring_wrong_color(self):
        @color_print_method('wrong_color')
        def test_func():
            return 'default'

        expected_result = "\x1b[39mdefault\x1b[0m"
        actual_result = test_func()
        self.assertEqual(expected_result, actual_result)
