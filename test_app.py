# test_app.py

import app

def test_add():
    assert app.add(2, 3) == 5

def test_subtract():
    assert app.subtract(5, 3) == 2
