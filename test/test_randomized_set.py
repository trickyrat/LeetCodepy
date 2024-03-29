from src.leetcode.randomized_set import RandomizedSet


class TestRandomizedSet:
    def test_randomized_set(self):
        randomized_set = RandomizedSet()
        assert randomized_set.insert(1) is True
        assert randomized_set.remove(2) is False
        assert randomized_set.insert(2) is True
        assert randomized_set.get_random() in [1, 2]
        assert randomized_set.remove(1) is True
        assert randomized_set.insert(2) is False
        assert randomized_set.get_random() == 2
