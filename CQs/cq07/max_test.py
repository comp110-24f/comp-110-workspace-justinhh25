from CQs.cq07.find_max import find_and_remove_max

__author__: str = "730758900"


def test_find_and_remove_max_return() -> None:
    """Tests to see if the return value is correct"""
    a: list[int] = [109, 99, 82, 71, 10]
    assert find_and_remove_max(a) == 109


def test_find_and_remove_max_mutation() -> None:
    """Tests to see if the list is mutilated correctly"""
    b: list[int] = [109, 99, 82, 71, 10]
    find_and_remove_max(b)
    assert b == [99, 82, 71, 10]


def test_find_and_remove_max_edge_case() -> None:
    """Tests to see the return for a special case where list is empty"""
    assert find_and_remove_max([]) == -1
