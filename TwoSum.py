#https://leetcode.com/problems/two-sum/

#Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
#You may assume that each input would have exactly one solution, and you may not use the same element twice.

# An naive appoarch is loop through the list twice and check for the match
# This will result in time complexity of O(n**2) and space complexity O(1)
# However, we can trace space for time with hashmap implementation


def twoSum(nums: List[int], target: int) -> List[int]:
    hashmap = {}
    for i in range(len(nums)):
        hashmap[nums[i]] = i 
    for i in range(len(nums)):
        sub = target - nums[i]
        if sub in hashmap and hashmap[sub] != i:
            return [i, hashmap[sub]]
    return False

# We can do a small optimization by using just 1 loop -> Try it everytime you review

