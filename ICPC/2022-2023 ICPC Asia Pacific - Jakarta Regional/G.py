def find_longest_subarray(nums):
    n = len(nums)
    count = {}
    max_len = 0
    start_index = 0
    distinct_count = 0

    left = 0
    right = 0

    for right in range(n):
        if nums[right] not in count:
            distinct_count += 1
        count[nums[right]] = count.get(nums[right], 0) + 1

        while distinct_count == 4:
            if right - left + 1 > max_len:
                max_len = right - left + 1
                start_index = left

            count[nums[left]] -= 1
            if count[nums[left]] == 0:
                distinct_count -= 1

            left += 1

    if max_len == 0:
        return []  # Không tìm thấy dãy con thỏa mãn

    longest_subarray = nums[start_index:start_index + max_len]
    return longest_subarray

# Thử nghiệm với một mảng ví dụ
nums = [1, 2, 3, 1, 2, 3, 1, 2, 3, 3, 3]
longest_subarray = find_longest_subarray(nums)

print("Dãy con dài nhất thỏa điều kiện:", longest_subarray)
