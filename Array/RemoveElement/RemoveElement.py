from typing import List


class Solutions:
    def removeElements(self,nums,val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        left_pointer = 0
        right_pointer = len(nums) - 1
      
        while right_pointer >= left_pointer:
            if(nums[left_pointer] == val):
                nums[left_pointer] = nums[right_pointer]
                right_pointer-=1

            else:
                left_pointer += 1                
            
        return right_pointer + 1





def main():
    nums =[3,2,2,3]
    val = 3

    solution = Solutions()
    print(solution.removeElements(nums,val))



if __name__ == "__main__":
    main()

