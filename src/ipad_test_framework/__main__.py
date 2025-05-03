import argparse
import sys
from typing import List

from .interface.ipad_interface import iPadInterface
from .core.test_runner import TestRunner
from .core.test_case import TestCase
from .utils.helpers import load_config, create_sample_config


def main(args: List[str] = None) -> int:
    """
    Main entry point for the command line interface.
    
    Args:
        args: Command line arguments
        
    Returns:
        Exit code
    """
    parser = argparse.ArgumentParser(description="iPad Test Framework")
    parser.add_argument("--config", help="Path to configuration file")
    parser.add_argument("--create-config", help="Create a sample configuration file at the specified path")
    
    parsed_args = parser.parse_args(args)
    
    if parsed_args.create_config:
        create_sample_config(parsed_args.create_config)
        print(f"Sample configuration created at: {parsed_args.create_config}")
        return 0
        
    if not parsed_args.config:
        print("Error: Please provide a configuration file with --config")
        return 1
        
    try:
        config = load_config(parsed_args.config)
        print(f"Loaded configuration from: {parsed_args.config}")
        return 0
    except Exception as e:
        print(f"Error: {e}")
        return 1


if __name__ == "__main__":
    sys.exit(main())
