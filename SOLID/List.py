from typing import List
from collections import defaultdict


def window_mode(inp: List[int], window: int) -> List[List[int]]:
    """Given a list of integers and a sliding window of size k, write a function that returns the "mode" or most frequent number in each window from left to right. If there are multiple numbers that have the highest frequency, list them in sorted order."""

    res = []

    n = len(inp)

    dic = defaultdict(int)
    for i in range(window - 1):
        dic[inp[i]] += 1

    print(dic, "may")
    left = 0

    for right in range(window - 1, n):
        print(right, "right", inp)
        cur_num = inp[right]
        print(cur_num, "i", n)
        if cur_num not in dic:
            dic[cur_num] = 1
        print(dic, type(dic), "final")
        if left > 0:
            prev_num = inp[left]
            dic[prev_num] -= 1
            if dic[prev_num] == 0:
                del dic[prev_num]
            left += 1

        dic = sorted(dic.items(), key=lambda x: -x[1])

        max_occurence = dic[0][1]
        cur_window_max_occur_nums = []
        for num, num_count in dic:
            if num_count < max_occurence:
                break
            else:
                cur_window_max_occur_nums.append(num)
        res.append(cur_window_max_occur_nums)

    return res


result = window_mode([2, 2, 3, 4, 3, 5, 6, 7, 6, 7, 6], 4)

# [[2],[3],[3],[4,3,5,6],[3, 5, 6, 7],[6],[6,7],[6,7]]
print(result)
