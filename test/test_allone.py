import pytest
from AllOne import AllOne


def test_all_one():
    all_one = AllOne()
    all_one.inc("hello")
    all_one.inc("hello")
    actual_max_Key1 = all_one.get_max_key()
    actual_min_Key1 = all_one.get_min_key()

    assert actual_max_Key1 == "hello"
    assert actual_min_Key1 == "hello"

    all_one.inc("leet")
    actual_max_Key2 = all_one.get_max_key()
    actual_min_Key2 = all_one.get_min_key()

    assert actual_max_Key2 == "hello"
    assert actual_min_Key2 == "leet"
