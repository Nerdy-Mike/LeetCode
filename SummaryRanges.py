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
	return re

nums = [0,2,3,4,6,8,9]

print(summaryRanges(nums))
