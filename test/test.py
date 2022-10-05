
from scripts.add import load_json
import sys
import os
sys.path.insert(0, os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..')))


def test_load_json():
    response = load_json()
    assert isinstance(response, dict)
    assert response.get("Data Glacier") == "Cricket"
