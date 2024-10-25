from lessons.unit_tests.list_fns import get_first, remove_first


def test_get_first() -> None:
    """get_first should return first elem"""
    dog_breeds: list[str] = ["husky", "golden", "poodle", "lab"]
    assert get_first(dog_breeds) == "husky"  # RV should be husky


def test_remove_first_return_value() -> None:
    """remove_first should return none"""
    dog_breeds: list[str] = ["husky", "golden", "poodle", "lab"]
    assert remove_first(dog_breeds) == ["golden", "poodle", "lab"]


# desired behavior
def test_remove_first_behavior() -> None:
    """remove_first should remove first element from the list"""
    dog_breeds: list[str] = ["husky", "golden", "poodle", "lab"]
    remove_first(dog_breeds)
    assert dog_breeds == ["golden", "poodle", "lab"]
