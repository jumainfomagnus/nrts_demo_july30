#!/usr/bin/env python3
"""
Test script for the calculator app
"""

import sys
import os

# Add the parent directory to the path to import calculator
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from calculator import add, subtract, multiply, divide

def test_arithmetic_operations():
    """Test all arithmetic operations."""
    print("Testing calculator operations...")
    
    # Test addition
    assert add(5, 3) == 8, "Addition test failed"
    assert add(-2, 4) == 2, "Addition with negative number failed"
    assert add(0, 0) == 0, "Addition with zeros failed"
    print("✓ Addition tests passed")
    
    # Test subtraction
    assert subtract(10, 3) == 7, "Subtraction test failed"
    assert subtract(-5, -3) == -2, "Subtraction with negative numbers failed"
    assert subtract(0, 5) == -5, "Subtraction from zero failed"
    print("✓ Subtraction tests passed")
    
    # Test multiplication
    assert multiply(4, 3) == 12, "Multiplication test failed"
    assert multiply(-2, 3) == -6, "Multiplication with negative number failed"
    assert multiply(0, 100) == 0, "Multiplication by zero failed"
    print("✓ Multiplication tests passed")
    
    # Test division
    assert divide(10, 2) == 5, "Division test failed"
    assert divide(-6, 3) == -2, "Division with negative number failed"
    assert divide(1, 4) == 0.25, "Division resulting in decimal failed"
    print("✓ Division tests passed")
    
    # Test division by zero
    try:
        divide(5, 0)
        assert False, "Division by zero should raise ValueError"
    except ValueError as e:
        assert str(e) == "Cannot divide by zero!", "Wrong error message for division by zero"
    print("✓ Division by zero error handling passed")
    
    print("\nAll tests passed! ✅")

if __name__ == "__main__":
    test_arithmetic_operations()