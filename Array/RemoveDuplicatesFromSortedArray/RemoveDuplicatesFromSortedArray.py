class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        last_unique_idx = 0
        current_idx =0

        while current_idx < len(nums):
            if(nums[last_unique_idx] != nums[current_idx]):
                last_unique_idx +=1
                nums[last_unique_idx]=nums[current_idx]

            current_idx+=1

        return (last_unique_idx,nums[:last_unique_idx])
def main():
    solution = Solution()

    # Input: nums = [0,0,1,1,1,2,2,3,3,4]
    # Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]

    input = [0,0,1,1,1,2,2,3,3,4]
    
    print(input,":",solution.removeDuplicates(input))


if __name__ == "__main__":
    main()