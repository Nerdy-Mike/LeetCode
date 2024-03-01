# There is 2 way to solve this problem, we can you hash map or 2 pointer methods as the array is sorted
# 2 pointer method:
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) -1
        while left < right:
            curr_sum = numbers[left] + numbers[right]
            if curr_sum == target:
                return [left +1, right +1]
            elif curr_sum > target:
                right -=1
            else:
                left +=1


