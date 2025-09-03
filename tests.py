from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content
from functions.write_file import write_file
from functions.run_python import run_python_file
# tests.py

import unittest

class TestGetFileInfo(unittest.TestCase):
    # Test cases for get_files_info function
    # def test_001(self):
    #     result = get_files_info("calculator", ".")
    #     print(result)
    #     self.assertEqual(result, 'Result for current directory:\n- main.py: file_size=575 bytes, is_dir=False\n- pkg: file_size=4096 bytes, is_dir=True\n- tests.py: file_size=1342 bytes, is_dir=False\n')

    # def test_002(self):
    #     result = get_files_info("calculator", "pkg")
    #     print(result)
    #     self.assertEqual(result, 'Result for pkg directory:\n- calculator.py: file_size=1737 bytes, is_dir=False\n- render.py: file_size=766 bytes, is_dir=False\n')

    # def test_003(self):
    #     result = get_files_info("calculator", "/bin")
    #     print(result)
    #     self.assertEqual(result, 'Error: Cannot list "/bin" as it is outside the permitted working directory.')

    # def test_004(self):
    #     result = get_files_info("calculator", "../")
    #     print(result)
    #     self.assertEqual(result, 'Error: Cannot list "../" as it is outside the permitted working directory.')

    # Test cases for get_files_content function
    # def test_005(self):
    #     result = get_file_content("calculator", "lorem.txt")
    #     print(result)
    #     self.assertEqual(result, result)

    # def test_006(self):
    #     result = get_file_content("calculator", "main.py")
    #     print(result)
    #     self.assertTrue(result.startswith("# main.py"))

    # def test_007(self):
    #     result = get_file_content("calculator", "pkg/calculator.py")
    #     print(result)
    #     self.assertTrue(result.startswith("# calculator.py"))

    # def test_008(self):
    #     result = get_file_content("calculator", "/bin/cat")
    #     print(result)
    #     self.assertEqual(result, 'Error: Cannot read "/bin/cat" as it is outside the permitted working directory.')

    # def test_009(self):
    #     result = get_file_content("calculator", "../main.py")
    #     print(result)
    #     self.assertEqual(result, 'Error: Cannot read "../main.py" as it is outside the permitted working directory.')

    # def test_010(self):
    #     result = get_file_content("calculator", "pkg/does_not_exist.py")
    #     print(result)
    #     self.assertEqual(result, 'Error: "pkg/does_not_exist.py" does not exist or is not a file.')

    # Test case for writing into files and creating files
    # def test_011(self):
    #     result = write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum")
    #     print(result)
    #     self.assertEqual(result, 'Successfully wrote to "lorem.txt" (28 characters written)')

    # def test_012(self):
    #     result = write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet")
    #     print(result)
    #     self.assertEqual(result, 'Successfully wrote to "pkg/morelorem.txt" (26 characters written)')

    # def test_013(self):
    #     result = write_file("calculator", "/tmp/temp.txt", "this should not be allowed")
    #     print(result)
    #     self.assertEqual(result, 'Error: Cannot write to "/tmp/temp.txt" as it is outside the permitted working directory.')

    #Test cases for running python files
    def test_014(self):
        result = run_python_file("calculator", "main.py")
        print(result)
        
    def test_015(self):
        result = run_python_file("calculator", "main.py", ["3 + 5"])
        print(result)

    def test_016(self):
        result = run_python_file("calculator", "tests.py")
        print(result)

    def test_017(self):
        result = run_python_file("calculator", "../main.py")
        print(result)

    def test_018(self):
        result = run_python_file("calculator", "nonexistent.py")
        print(result)

if __name__ == "__main__":
    unittest.main()