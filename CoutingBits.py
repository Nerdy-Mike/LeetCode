# Leetcode 338: Counting Bits
# Runtime: top 21%
# Memory Usage: top 23%
# Time Complexity: O(n)

from typing import List

def countBits(n: int) -> List[int]:
    return [len(bin(i)[2:].replace("0","")) for i in range(0,n+1)]

n = 5
print(countBits(n))


