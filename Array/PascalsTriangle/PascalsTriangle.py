class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        # n[0][0] , n[0][0]
        # n[1][0] , n[1][0] + n[1][1] , n[1][1] 
        # n[2][0] , n[2][0] + n[2][1] , n[2][1] + n[2][2] , n[2][2]

        n = [[1]]
        for i in range(1,numRows):
            n.append([1])
            for j in range(1,i):
                n[i].append(n[i-1][j-1]+ n[i-1][j])

            n[i].append(1)
        return n






def main():
   solution =  Solution()
   input = 5
   print(solution.generate(input))




if  __name__ == "__main__":
    main()