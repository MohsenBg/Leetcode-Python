class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left_pointer = 0
        right_pointer = len(nums) - 1

        while left_pointer <= right_pointer:
            mid = (right_pointer + left_pointer) // 2
            if(target == nums[mid]):
                return mid
        
            if(target > nums[mid]):
                left_pointer = mid + 1       
            else:
                right_pointer = mid - 1   

        return right_pointer + 1


def main():
    nums = [1,3,5,6]
    target = 0
    solution =  Solution()
    print(solution.searchInsert(nums,target))



if __name__ == "__main__":
    main()
