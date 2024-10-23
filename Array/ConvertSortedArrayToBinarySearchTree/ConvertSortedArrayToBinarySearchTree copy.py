class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    

class Solution(object):
    def sortedArrayToBST(self, nums) -> TreeNode:
        """
        :type nums: List[int]
        :rtype: Optional[TreeNode]
        """
        
        def sortToBinaryTree(l,r):

            if(l > r):
                return None
            
            mid = (r + l) // 2
            tree_node = TreeNode(nums[mid])

            tree_node.left = sortToBinaryTree(l,mid - 1)
            tree_node.right = sortToBinaryTree(mid + 1,r)

            return tree_node
        
        return sortToBinaryTree(0,len(nums) - 1)


def main():
   solution =  Solution()
   input = [-10,-3,0,5,9]

   print(solution.sortedArrayToBST(input))




if  __name__ == "__main__":
    main()