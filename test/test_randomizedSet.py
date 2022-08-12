from RandomizedSet import RandomizedSet

def test_randomize_set():
    randomizedSet  = RandomizedSet()
    assert randomizedSet.insert(1) is True
    assert randomizedSet.remove(2) is False
    assert randomizedSet.insert(2) is True
    assert randomizedSet.get_random() in [1, 2]
    assert randomizedSet.remove(1) is True
    assert randomizedSet.insert(2) is False
    assert randomizedSet.get_random() == 2

