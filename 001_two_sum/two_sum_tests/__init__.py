import two_sum_src as two_sum


def test_one():
    nums = [2, 7, 11, 15]
    target = 9

    assert [0, 1] == two_sum.two_sum(nums, target)
