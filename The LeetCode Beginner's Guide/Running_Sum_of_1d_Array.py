class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """ 
        for index in range(1,len(nums)):
            nums[index] = nums[index]+ nums[index -1]
        return nums


def main():
    solution = Solution()
    nums = [1,2,3,4]
    
    #Input: nums = [1,2,3,4]
    # Output: [1,3,6,10]
    print(solution.runningSum(nums))

if __name__ == "__main__":
    main()
        