### Problem: **Merge Sorted Array**

You are given two integer arrays `nums1` and `nums2`, sorted in non-decreasing order, and two integers `m` and `n`, representing the number of elements in `nums1` and `nums2`, respectively.

You need to merge `nums2` into `nums1` in-place, such that the resulting array is sorted in non-decreasing order.

- `nums1` has a size of `m + n`, where the first `m` elements denote the elements of `nums1`, and the rest are zeroes, which will be replaced by `nums2` elements.

#### Example:
**Input**:  
`nums1 = [1,2,3,0,0,0]`, `m = 3`,  
`nums2 = [2,5,6]`, `n = 3`  

**Output**:  
`[1,2,2,3,5,6]`

---

### Approach: **Two-Pointer Method (From the End)**

1. **Pointers Setup**:  
   - `num1_pointer`: Points to the last valid element of `nums1` (i.e., `m - 1`).
   - `num2_pointer`: Points to the last element of `nums2` (i.e., `n - 1`).
   - `current_pointer`: Points to the last position in `nums1` (i.e., `m + n - 1`), where the largest element of the merged array will be placed.

2. **Merge from the End**:  
   Since both arrays are sorted, compare elements from the back:
   - If `nums1[num1_pointer] >= nums2[num2_pointer]`, place `nums1[num1_pointer]` in the current position and move `num1_pointer` back.
   - If `nums2[num2_pointer] > nums1[num1_pointer]`, place `nums2[num2_pointer]` in the current position and move `num2_pointer` back.
   - After each step, decrease the `current_pointer` by 1.

3. **Handle Remaining Elements**:  
   If there are still elements left in `nums2` after the first loop (i.e., `num2_pointer >= 0`), copy them into `nums1`. There is no need to copy the remaining elements of `nums1`, as they are already in place.

4. **End Condition**:  
   The process stops when `num2_pointer` becomes `-1` or all elements have been processed.

---

### Example Walkthrough:

**Input**:  
`nums1 = [1, 2, 3, 0, 0, 0]`, `m = 3`,  
`nums2 = [2, 5, 6]`, `n = 3`

1. Start with the last elements:
   - Compare `nums1[2] = 3` and `nums2[2] = 6`. Since `6 > 3`, set `nums1[5] = 6` and decrease `num2_pointer` to `1` and `current_pointer` to `4`.

2. Next comparison:
   - Compare `nums1[2] = 3` and `nums2[1] = 5`. Since `5 > 3`, set `nums1[4] = 5` and decrease `num2_pointer` to `0` and `current_pointer` to `3`.

3. Next comparison:
   - Compare `nums1[2] = 3` and `nums2[0] = 2`. Since `3 > 2`, set `nums1[3] = 3` and decrease `num1_pointer` to `1` and `current_pointer` to `2`.

4. Next comparison:
   - Compare `nums1[1] = 2` and `nums2[0] = 2`. Set `nums1[2] = 2` and decrease `num2_pointer` to `-1` and `current_pointer` to `1`.

5. Since `nums2_pointer` is now `-1`, the process ends. The final array is `[1, 2, 2, 3, 5, 6]`.

---

### Time and Space Complexity:
- **Time Complexity**: O(m + n) — iterate over both arrays once.
- **Space Complexity**: O(1) — modify `nums1` in-place without additional space.
--- 

