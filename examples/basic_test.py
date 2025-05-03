"""
Example script demonstrating how to use the iPad Test Framework.
"""

from ipad_test_framework.interface.ipad_interface import iPadInterface
from ipad_test_framework.core.test_runner import TestRunner
from ipad_test_framework.core.test_case import TestCase


def main():
    ipad = iPadInterface(device_id="iPad001")
    
    runner = TestRunner(ipad_interface=ipad)
    
    test_case = TestCase(
        name="Basic Functionality Test",
        description="Tests the basic functionality of the iPad"
    )
    
    test_case.add_command(
        command="launch_app",
        params={"app_id": "com.example.testapp"}
    )
    
    test_case.add_command(
        command="tap",
        params={"x": 100, "y": 200}
    )
    
    test_case.add_command(
        command="verify_element",
        params={"element_id": "login_button"},
        validator=lambda response: response.get("status") == "success"
    )
    
    runner.add_test_case(test_case)
    
    report = runner.run_tests()
    
    print(report.to_json())


if __name__ == "__main__":
    main()
