class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        max_wealth = sum(accounts[0])

        for i in range(1,len(accounts)):
            current_customer_wealth = 0
            
            for value in accounts[i]:
                 current_customer_wealth +=value
            
            if(current_customer_wealth > max_wealth):
                max_wealth = current_customer_wealth

        return max_wealth
        

def main():
    solution = Solution()
    inp = [[1,5],[7,3],[3,5]]
    
    # Input: [[1,5],[7,3],[3,5]]
    # Output: 10
    print(solution.maximumWealth(inp))

if __name__ == "__main__":
    main()
        