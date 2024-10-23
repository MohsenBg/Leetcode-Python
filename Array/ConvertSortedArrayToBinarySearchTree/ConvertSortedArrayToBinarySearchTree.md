### Problem: **Convert Sorted Array to Binary Search Tree**

Given an integer array `nums` where the elements are sorted in ascending order, you need to convert it into a height-balanced binary search tree (BST).

- A **height-balanced BST** is a binary tree in which the depth of the two subtrees of every node never differs by more than one.

#### Example:

**Input**:  
`nums = [-10,-3,0,5,9]`

**Output**:  
A binary search tree:

   0
  / \
-10  5
  \    \
  -3    9


---

### Approach: **Recursive Divide and Conquer**

The goal is to construct a balanced BST from the sorted array. To achieve this, you can recursively select the middle element as the root, and then build the left and right subtrees from the left and right halves of the array, respectively.

#### Steps:
1. **Recursive Helper Function**:
   - The function `sortToBinaryTree(l, r)` is defined to build a BST from the subarray `nums[l:r+1]`.
   - If `l > r`, the subarray is invalid (base case), so return `None`.

2. **Find the Middle Element**:
   - The middle index `mid = (r + l) // 2` is chosen, and the middle element `nums[mid]` becomes the root of the current subtree.

3. **Recursive Construction**:
   - Recursively build the left subtree by calling `sortToBinaryTree(l, mid - 1)` with the left half of the array.
   - Recursively build the right subtree by calling `sortToBinaryTree(mid + 1, r)` with the right half of the array.

4. **Return the Root**:
   - Finally, return the `tree_node`, which is the root of the subtree for the current range.

5. **Start from the Full Array**:
   - The initial call `sortToBinaryTree(0, len(nums) - 1)` begins the construction from the full array.

---

### Example Walkthrough:

**Input**:  
`nums = [-10, -3, 0, 5, 9]`

1. The middle element `0` becomes the root.
2. The left subarray `[-10, -3]` is used to build the left subtree.
   - `-3` becomes the left child of `0`.
   - `-10` becomes the left child of `-3`.
3. The right subarray `[5, 9]` is used to build the right subtree.
   - `5` becomes the right child of `0`.
   - `9` becomes the right child of `5`.

Final Tree:
    0
   / \
 -3   5
 /     \
-10     9


---

### Time and Space Complexity:

- **Time Complexity**: O(n) — You visit each element of the array exactly once to construct the tree.
- **Space Complexity**: O(log n) — The recursion depth is O(log n) because the tree is balanced, and we do not use any extra data structures apart from the recursion stack.

---

This solution efficiently converts the sorted array into a height-balanced binary search tree using divide and conquer.
