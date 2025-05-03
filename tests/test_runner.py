import unittest
from unittest.mock import MagicMock

from ipad_test_framework.interface.ipad_interface import iPadInterface
from ipad_test_framework.core.test_runner import TestRunner
from ipad_test_framework.core.test_case import TestCase


class TestTestRunner(unittest.TestCase):
    """Unit tests for the TestRunner class."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.ipad_interface = MagicMock(spec=iPadInterface)
        self.ipad_interface.connect.return_value = True
        self.ipad_interface.send_command.return_value = {"status": "success"}
        
        self.runner = TestRunner(ipad_interface=self.ipad_interface)
        
    def test_add_test_case(self):
        """Test adding a test case to the runner."""
        test_case = TestCase(name="Test Case 1")
        self.runner.add_test_case(test_case)
        self.assertEqual(len(self.runner.test_cases), 1)
        self.assertEqual(self.runner.test_cases[0].name, "Test Case 1")
        
    def test_run_tests(self):
        """Test running tests with the runner."""
        test_case = TestCase(name="Test Case 1")
        test_case.add_command("test_command")
        
        self.runner.add_test_case(test_case)
        report = self.runner.run_tests()
        
        self.ipad_interface.connect.assert_called_once()
        
        self.ipad_interface.send_command.assert_called_once_with("test_command", {})
        
        self.assertEqual(len(report.results), 1)
