from typing import List, Dict, Any
import json
from datetime import datetime


class TestReport:
    """
    Generates and manages test execution reports.
    
    This class compiles the results of test execution and provides
    methods for formatting and exporting the results.
    """
    
    def __init__(self, results: List[Dict[str, Any]]):
        """
        Initialize a test report with test results.
        
        Args:
            results: List of test case execution results
        """
        self.results = results
        self.timestamp = datetime.now().isoformat()
        
    def summary(self) -> Dict[str, Any]:
        """
        Generate a summary of the test execution.
        
        Returns:
            Dictionary containing summary statistics
        """
        total_tests = len(self.results)
        passed_tests = sum(1 for result in self.results if result.get("success", False))
        
        return {
            "timestamp": self.timestamp,
            "total_tests": total_tests,
            "passed_tests": passed_tests,
            "failed_tests": total_tests - passed_tests,
            "success_rate": passed_tests / total_tests if total_tests > 0 else 0
        }
        
    def to_json(self) -> str:
        """Convert the report to a JSON string."""
        report_data = {
            "summary": self.summary(),
            "results": self.results
        }
        return json.dumps(report_data, indent=2)
        
    def save_to_file(self, filename: str) -> None:
        """Save the report to a file."""
        with open(filename, "w") as f:
            f.write(self.to_json())
