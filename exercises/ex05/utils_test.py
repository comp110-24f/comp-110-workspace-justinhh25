from exercises.ex05.utils import only_evens, sub, add_at_index
import pytest

"""Tests the util functions in utils.py"""

__author__: str = "730758900"


def test_only_evens_edge_case() -> None:
    """Tests to see if it returns empty list"""
    assert only_evens([]) == []


def test_only_evens_return_value() -> None:
    """Tests to see the only_evens return value"""
    nums: list[int] = [1, 2, 3, 4, 5, 6, 7, 8]
    assert only_evens(nums) == [2, 4, 6, 8]


def test_only_evens_inputList() -> None:
    """Tests to see if input list is mutated or not"""
    nums2: list[int] = [10, 11, 12, 13, 14, 15, 16, 17, 18]
    only_evens(nums2)
    assert nums2 == [10, 11, 12, 13, 14, 15, 16, 17, 18]


def test_sub_edge_case1() -> None:
    """Tests to see if empty list is returned"""
    assert sub([], 1, 3) == []


def test_sub_edge_case2() -> None:
    """Another edge cases for empty list"""
    assert sub([17, 20, 18, 4], 20, 3) == []


def test_sub_edge_case3() -> None:
    """Another edge cases for empty list"""
    assert sub([420, 100, 69, 1738, 1000], 1, -20) == []


def test_sub_return_value() -> None:
    """Tests the return value for sub function"""
    subList: list[int] = [3, 4, 5, 6, 7, 8]
    assert sub(subList, 3, 10) == [6, 7, 8]


def test_sub_inputList() -> None:
    """Tests to see if list is mutated or not"""
    subList2: list[int] = [110, 210, 211, 310, 457, 570]
    sub(subList2, 1, 6)
    assert subList2 == [110, 210, 211, 310, 457, 570]


def test_add_at_index_edge_case() -> None:
    """Tests that add_at_index will raise IndexError for  an invalid index"""
    addIndex: list[int] = [56, 57, 58, 59, 60, 61, 62, 63]
    with pytest.raises(IndexError):
        add_at_index(addIndex, 70, 1000)


def test_add_at_index_edge_case2() -> None:
    """Tests that add_at_index will raise IndexError for  an invalid index"""
    addIndex: list[int] = [56, 57, 58, 59, 60, 61, 62, 63]
    with pytest.raises(IndexError):
        add_at_index(addIndex, 70, -1)


def test_add_at_index_return_value() -> None:
    """Tests to see the return value (function has no return value, thus None)"""
    addAtIdxList: list[int] = [20, 40, 60, 80, 120]
    assert add_at_index(addAtIdxList, 100, 3) == None


def test_add_at_index_inputList() -> None:
    """Tests to see if the list was mutated"""
    addAtIdxList2: list[int] = [20, 40, 60, 80, 120]
    add_at_index(addAtIdxList2, 100, 4)
    assert addAtIdxList2 == [20, 40, 60, 80, 100, 120]
