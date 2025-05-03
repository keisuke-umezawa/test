from typing import Dict, Any, Optional, Callable, List
from ..interface.ipad_interface import iPadInterface


class TestCase:
    """
    Represents a single test case to be executed on an iPad device.
    
    Test cases define a sequence of commands to be sent to the device
    and validation functions to verify the responses.
    """
    
    def __init__(self, name: str, description: Optional[str] = None):
        """
        Initialize a test case.
        
        Args:
            name: Name of the test case
            description: Optional description of the test case
        """
        self.name = name
        self.description = description
        self.commands: List[Dict[str, Any]] = []
        self.setup_commands: List[Dict[str, Any]] = []
        self.teardown_commands: List[Dict[str, Any]] = []
        
    def add_command(self, command: str, params: Optional[Dict[str, Any]] = None,
                    validator: Optional[Callable[[Dict[str, Any]], bool]] = None) -> None:
        """Add a command to the test case."""
        self.commands.append({
            "command": command,
            "params": params or {},
            "validator": validator
        })
        
    def execute(self, ipad_interface: iPadInterface) -> Dict[str, Any]:
        """
        Execute the test case on the given iPad interface.
        
        Args:
            ipad_interface: Interface for communicating with the iPad device
            
        Returns:
            Dictionary containing the test results
        """
        results = {"name": self.name, "commands": [], "success": True}
        
        for cmd in self.commands:
            response = ipad_interface.send_command(cmd["command"], cmd["params"])
            validation = True if cmd["validator"] is None else cmd["validator"](response)
            results["commands"].append({"command": cmd["command"], "response": response, "validation": validation})
            if not validation:
                results["success"] = False
                
        return results
