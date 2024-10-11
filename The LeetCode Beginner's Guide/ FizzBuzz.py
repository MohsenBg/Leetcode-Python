class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """


        result = []
        for i in range (1,n+1):
            value = ''
            if(i % 3 == 0):
                value +='Fizz'
            if(i % 5 == 0):
                value += 'Buzz'
            result.append(str(i) if value == '' else value)

        return result


def main():
    solution = Solution()

    
    input = 15
    print(input,":",solution.fizzBuzz(input))


if __name__ == "__main__":
    main()