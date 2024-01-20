#include <iostream>
#include <vector>
#include <unordered_map>

using namespace std;

vector<int> findLongestSubarray(vector<int> &nums)
{
    int n = nums.size();
    unordered_map<int, int> count;
    int maxLen = 0, startIndex = 0, distinctCount = 0;
    vector<int> result;

    for (int left = 0, right = 0; right < n; ++right)
    {
        if (count[nums[right]] == 0)
        {
            ++distinctCount;
        }
        ++count[nums[right]];

        while (distinctCount == 4)
        {
            if (right - left + 1 > maxLen)
            {
                maxLen = right - left + 1;
                startIndex = left;
            }

            --count[nums[left]];
            if (count[nums[left]] == 0)
            {
                --distinctCount;
            }

            ++left;
        }
    }

    if (maxLen == 0)
    {
        return result; // Không tìm thấy dãy con thỏa mãn
    }

    for (int i = startIndex; i < startIndex + maxLen; ++i)
    {
        result.push_back(nums[i]);
    }

    return result;
}

int main()
{
    vector<int> nums = {1, 2, 3, 1, 2, 3, 1, 2, 3, 3, 3};
    vector<int> longestSubarray = findLongestSubarray(nums);

    cout << "Dãy con dài nhất thỏa điều kiện: ";
    for (int num : longestSubarray)
    {
        cout << num << " ";
    }

    return 0;
}
