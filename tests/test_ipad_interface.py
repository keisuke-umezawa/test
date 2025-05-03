import unittest
from ipad_test_framework.interface.ipad_interface import iPadInterface


class TestiPadInterface(unittest.TestCase):
    """Unit tests for the iPadInterface class."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.ipad = iPadInterface(device_id="test_device")
        
    def test_connect(self):
        """Test connecting to the iPad device."""
        result = self.ipad.connect()
        self.assertTrue(result)
        self.assertTrue(self.ipad.connected)
        
    def test_send_command(self):
        """Test sending a command to the iPad device."""
        self.ipad.connect()
        response = self.ipad.send_command("test_command", {"param1": "value1"})
        self.assertEqual(response["status"], "success")
        self.assertEqual(response["command"], "test_command")
        self.assertEqual(response["params"]["param1"], "value1")
        
    def test_disconnect(self):
        """Test disconnecting from the iPad device."""
        self.ipad.connect()
        self.ipad.disconnect()
        self.assertFalse(self.ipad.connected)
