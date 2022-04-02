# Leetcode 228: Summary Ranges
# Runtime: 32ms top 15%
# Memory Usage: 14 MB top 40%
# Time complexity: O(n)

from typing import List
def summaryRanges( nums: List[int]) -> List[str]:  
    temp = []
    re = []
    for i in nums:
        if (len(temp)==0):
            temp.append(i)
        elif (temp[-1] +1 == i):
            temp.append(i)
        else:
            re.append(temp)
            temp = [i]
    if(len(temp) >0): re.append(temp)
    ls= []
    for array in re:
        if(len(array)>1):
            ls.append(str(array[0]) + "->" +str(array[-1]))
        else:
            ls.append(str(array[0]))
    return ls

testcase1 = [0,2,3,4,6,8,9]
testcase2 = [0,1,2,4,5,7]

print(summaryRanges(testcase1))
print(summaryRanges(testcase2))
