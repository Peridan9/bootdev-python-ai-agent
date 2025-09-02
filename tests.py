from functions.get_files_info import get_files_info

# tests.py

import unittest

class TestGetFileInfo(unittest.TestCase):
    def test_001(self):
        result = get_files_info("calculator", ".")
        print(result)
        self.assertEqual(result, 'Result for current directory:\n- main.py: file_size=575 bytes, is_dir=False\n- pkg: file_size=4096 bytes, is_dir=True\n- tests.py: file_size=1342 bytes, is_dir=False\n')

    def test_002(self):
        result = get_files_info("calculator", "pkg")
        print(result)
        self.assertEqual(result, 'Result for pkg directory:\n- calculator.py: file_size=1737 bytes, is_dir=False\n- render.py: file_size=766 bytes, is_dir=False\n')

    def test_003(self):
        result = get_files_info("calculator", "/bin")
        print(result)
        self.assertEqual(result, 'Error: Cannot list "/bin" as it is outside the permitted working directory.')

    def test_004(self):
        result = get_files_info("calculator", "../")
        print(result)
        self.assertEqual(result, 'Error: Cannot list "../" as it is outside the permitted working directory.')

if __name__ == "__main__":
    unittest.main()