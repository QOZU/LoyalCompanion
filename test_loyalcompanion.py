# test_loyalcompanion.py
"""
Tests for LoyalCompanion module.
"""

import unittest
from loyalcompanion import LoyalCompanion

class TestLoyalCompanion(unittest.TestCase):
    """Test cases for LoyalCompanion class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = LoyalCompanion()
        self.assertIsInstance(instance, LoyalCompanion)
        
    def test_run_method(self):
        """Test the run method."""
        instance = LoyalCompanion()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
