import unittest

from pyscan import scan_source


class ScanTests(unittest.TestCase):
    def test_structure(self):
        source = "import os\n\nclass Demo:\n    def run(self):\n        return os.getcwd()\n"
        result = scan_source(source)
        self.assertEqual(result["imports"], ["os"])
        self.assertEqual(result["classes"], ["Demo"])
        self.assertEqual(result["functions"], ["run"])
        self.assertEqual(result["lines"], 5)

    def test_invalid_source(self):
        with self.assertRaises(SyntaxError):
            scan_source("def broken(")


if __name__ == "__main__":
    unittest.main()
