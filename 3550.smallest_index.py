 
class Solution:
    def smallestIndex(self, nums) -> int:
        for i,value in enumerate(nums):
            digit=0
            while value>0:
                digit+=value%10
                value=value//10
            if digit==i:
                return i
        return -1
    
'''
the second method is converting the num into str and then add the element 
class Solution:
    def smallestIndex(self, nums) -> int:
        for i,value in enumerate(nums):
            digit=sum(int(c) for c in str(value))
            if digit==i:
                return i
        return -1

'''