from typing import Dict, Any, Optional
import json
import os


def load_config(config_file: str) -> Dict[str, Any]:
    """
    Load configuration from a JSON file.
    
    Args:
        config_file: Path to the configuration file
        
    Returns:
        Dictionary containing configuration parameters
    """
    if not os.path.exists(config_file):
        raise FileNotFoundError(f"Configuration file not found: {config_file}")
        
    with open(config_file, "r") as f:
        return json.load(f)
        
def create_sample_config(output_file: str) -> None:
    """
    Create a sample configuration file.
    
    Args:
        output_file: Path where the sample configuration will be saved
    """
    sample_config = {
        "device_id": "sample_ipad_001",
        "host": "localhost",
        "port": 8080,
        "timeout": 30
    }
    
    with open(output_file, "w") as f:
        json.dump(sample_config, f, indent=2)
