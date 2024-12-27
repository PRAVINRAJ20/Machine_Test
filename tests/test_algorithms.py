import pytest
from algorithms import quicksort

def test_quicksort():
    assert quicksort([3, 2, 1]) == [1, 2, 3]
    assert quicksort([]) == []
    assert quicksort([1]) == [1]
