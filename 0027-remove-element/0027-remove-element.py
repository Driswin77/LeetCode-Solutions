class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        l=[]
        for i in nums:
            if i!=val:
                l.append(i)
        nums[:]=l #Replace all the elements of nums with the elements of temp, while keeping the same list object
        return  len(l)       