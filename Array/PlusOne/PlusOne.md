### Problem: **Plus One**

Given a non-empty array of decimal digits representing a non-negative integer, increment the integer by one.

The most significant digit is at the head of the array, and each element in the array contains a single digit. You may assume the integer does not contain any leading zero, except for the number `0` itself.

#### Example:
**Input**: `[1, 2, 9]`  
**Output**: `[1, 3, 0]`  
Explanation: The array represents the number 129. Adding 1 results in 130.

**Input**: `[9, 9, 9]`  
**Output**: `[1, 0, 0, 0]`  
Explanation: The array represents the number 999. Adding 1 results in 1000.

---

### Approach: **In-Place Increment (Without String Conversion)**

We can solve this problem by **directly modifying the array** of digits, treating it like a number in its decimal form. Starting from the least significant digit, we propagate any carry resulting from adding 1.

#### Steps:
1. **Start from the rightmost digit**: Begin with the last element of the array (the least significant digit).
2. **Add 1 to the digit**: Add 1 to the current digit.
   - If the result is less than 10, the carry is done, and we can return the array.
   - If the result is 10, set the current digit to `0` and carry over the `1` to the next digit on the left.
3. **Continue until the leftmost digit**: If you reach the leftmost digit and still have a carry (i.e., the number was all `9`s), insert a `1` at the start of the array.

#### Edge Case:
- If all digits are `9` (e.g., `[9, 9, 9]`), after processing all digits, the result will be `[1, 0, 0, 0]`.

---

### Example Walkthrough:

#### Example 1:
**Input**: `[1, 2, 9]`  
- Start from the last digit `9`. Add 1 to get `10`, so set the last digit to `0` and carry over `1`.
- Move to the next digit `2`. Add the carry to get `3`. No further carry is needed, so the result is `[1, 3, 0]`.

**Output**: `[1, 3, 0]`

#### Example 2:
**Input**: `[9, 9, 9]`  
- Start from the last digit `9`. Add 1 to get `10`, so set the last digit to `0` and carry over `1`.
- Move to the next digit, which is also `9`. Add the carry to get `10`, so set this digit to `0` and carry over `1`.
- Repeat for the leftmost `9`. Add the carry to get `10`, so set it to `0` and carry over `1`.
- Since all digits are `0`, insert `1` at the front of the list.

**Output**: `[1, 0, 0, 0]`

---

### Time and Space Complexity:
- **Time Complexity**: O(n), where `n` is the number of digits. In the worst case, we have to iterate over all the digits when there is a carry that propagates through the entire array.
- **Space Complexity**: O(1) extra space, as the modification is done in-place except for the case where we need to insert a `1` at the front, which takes O(n) space to create a new list.

---

This approach efficiently solves the **Plus One** problem without converting the digits array into a string, adhering to the constraint of working with the array directly.