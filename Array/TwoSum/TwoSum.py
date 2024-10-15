class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        values = dict()
        
        for i in range(len(nums)):
            complement = target - nums[i] 
            if complement in values:
                    return [values[complement],i]

            value = nums[i]
            if value not in values:  
                values[value] = i  
        
        return []
        

def main():
    solution = Solution()

    # Input: nums = [2,7,11,15], target = 9
    # Output: [0,1]
    # Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

    input = [5,8,12,3,3]
    target = 6
    print(input,":",solution.twoSum(input,target))


if __name__ == "__main__":
    main()