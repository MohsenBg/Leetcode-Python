from typing import List

class Solution(object):
    def merge(self, nums1:List[int], m:int, nums2:List[int], n:int):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        num1_pointer = m-1;
        num2_pointer = n-1;
        current_pointer = m + n - 1

        
        while num2_pointer >= 0 and num1_pointer >= 0:
            if(nums1[num1_pointer] >= nums2[num2_pointer]):
                nums1[current_pointer] = nums1[num1_pointer]
                num1_pointer-=1;
            else:
                nums1[current_pointer] = nums2[num2_pointer]
                num2_pointer-=1;
            
            current_pointer-=1;
            
        # it already sorted cause no need loop for pointer 1 
        # while num1_pointer >= 0 :
        #     nums1[current_pointer] = nums1[num1_pointer]
        #     current_pointer -=1
        #     num1_pointer -=1

        while num2_pointer >= 0 :
            nums1[current_pointer] = nums2[num2_pointer]
            current_pointer -=1
            num2_pointer -=1    


def main():
   solution =  Solution()
   nums1 = [1,2,3,0,0,0]
   m = 3

   nums2 = [2,5,6]
   n = 3

   solution.merge(nums1,m,nums2,n)

   print(nums1)




if  __name__ == "__main__":
    main()