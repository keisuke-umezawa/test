from typing import List, Optional, Dict, Any

from ..interface.ipad_interface import iPadInterface
from .test_case import TestCase
from ..reporting.test_report import TestReport


class TestRunner:
    """
    Main class for executing tests on iPad devices.
    
    This class orchestrates the test execution process, including device connection,
    test execution, and result collection.
    """
    
    def __init__(self, ipad_interface: iPadInterface):
        """
        Initialize the TestRunner with an iPad interface.
        
        Args:
            ipad_interface: Interface for communicating with iPad devices
        """
        self.ipad_interface = ipad_interface
        self.test_cases: List[TestCase] = []
        
    def add_test_case(self, test_case: TestCase) -> None:
        """Add a test case to the runner."""
        self.test_cases.append(test_case)
        
    def run_tests(self, config: Optional[Dict[str, Any]] = None) -> TestReport:
        """
        Execute all registered test cases on the connected iPad device.
        
        Args:
            config: Optional configuration parameters for test execution
            
        Returns:
            TestReport containing the results of all executed tests
        """
        config = config or {}
        
        self.ipad_interface.connect()
        
        results = [test_case.execute(self.ipad_interface) for test_case in self.test_cases]
        
        return TestReport(results=results)
