# iPad Test Framework

A Python framework for running automated tests on iPad devices.

## Overview

This framework allows you to automate testing on iPad devices by providing:

- A core test runner that manages test execution
- A standardized interface for communicating with iPad devices
- A flexible test case structure
- Comprehensive reporting capabilities

## Installation

```bash
# Clone the repository
git clone https://github.com/keisuke-umezawa/test.git
cd test

# Install the package
pip install -e .
```

## Usage

### Basic Example

```python
from ipad_test_framework.interface.ipad_interface import iPadInterface
from ipad_test_framework.core.test_runner import TestRunner
from ipad_test_framework.core.test_case import TestCase

# Initialize the iPad interface
ipad = iPadInterface(device_id="iPad001")

# Create a test runner
runner = TestRunner(ipad_interface=ipad)

# Create and configure a test case
test_case = TestCase(
    name="Basic Functionality Test",
    description="Tests the basic functionality of the iPad"
)

# Add commands to the test case
test_case.add_command(
    command="launch_app",
    params={"app_id": "com.example.testapp"}
)

# Add the test case to the runner
runner.add_test_case(test_case)

# Run the tests
report = runner.run_tests()

# Print test results
print(report.to_json())
```

## Development

### Running Tests

```bash
# Install development dependencies
pip install -r requirements-dev.txt

# Run tests
pytest
```

## License

MIT
