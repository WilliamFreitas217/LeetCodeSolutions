class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums_dict = {}
        for n in nums:
            if str(n) in nums_dict.keys():
                nums_dict[str(n)] += 1
            else:
                nums_dict[str(n)] = 1

        for k, v in nums_dict.items():
            if v > 1:
                for i in range(v - 1):
                    nums.remove(int(k))

        return len(nums)
