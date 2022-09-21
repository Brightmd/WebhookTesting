from webhooktesting.utils.lru_list import LRUList


def test_lru_list():
    list = LRUList(3)
    list.set("avocado")
    list.set("banana")
    list.set("cherry")
    list.set("durian")

    # State is ["banana", "cherry", "durian"]
    assert not list.contains_substring("avocado")  # Test cache bust
    assert list.contains_substring("banana")
    assert list.contains_substring("cherry")
    assert list.contains_substring("durian")

    list.set("elderberry")
    list.set("fig")

    # State is ["durian", "elderberry", "fig"]
    assert not list.contains_substring("banana")
    assert not list.contains_substring("cherry")
    assert list.contains_substring("eld")  # Test substring
    assert list.contains_substring("berry")
    assert list.contains_substring("f")
    assert list.contains_substring("ig")

    list.set("elderberry")
    list.set("grape")
    list.set("honeydew")

    # State is ["elderberry", "grape", "honeydew"]
    assert not list.contains_substring("fig")
    assert list.contains_substring("elderberry")  # Tests cache moves item to latest
    assert list.contains_substring("grape")
    assert list.contains_substring("honeydew")
    assert list.as_json() == '["elderberry", "grape", "honeydew"]'
