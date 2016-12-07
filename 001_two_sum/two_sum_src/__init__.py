def two_sum(nums=[], target=0):
    answer = None

    for o_index, o_value in enumerate(nums):
        for i_index, i_value in enumerate(nums):
            if (o_value + i_value) == target:
                return [o_index, i_index]

    return answer
