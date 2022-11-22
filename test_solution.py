import pytest
from solution import solution

# input 1, input 2, return longest string
test_table = [
    ("ABCDGH","ACDGH","CDGH"),
    ("a","abcd", "a"),
    ("abcde", "mnbcdke", "bcd"),
    ("a", "a", "a"),
    ("","a","")
]

def test_solution():
    for test in test_table:
        print(test)
        assert(solution(test[0], test[1])) == test[2]