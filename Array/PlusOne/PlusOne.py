from typing import List


class Solution(object):
    def plusOne(self, digits:List[int]):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        index = len(digits) - 1
        digits[index] += 1
        while index >= 0:   
            if(digits[index] >= 10):
                digits[index] = 0
                if(index == 0):
                    digits.insert(0, 1)
                else:
                    digits[index - 1] += 1
                index -=1
            else: 
                break
            
          
        return digits





def main():
   solution =  Solution()
   input = [9,9,9]
   print(solution.plusOne(input))




if  __name__ == "__main__":
    main()