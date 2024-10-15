### General Explanation for Removing Duplicates from a Sorted Array

The **Remove Duplicates from Sorted Array** problem requires modifying a sorted array in place so that each element appears only once. After the removal, we return the new length of the array.

#### Problem Understanding

1. **Input**: A sorted array of integers.
2. **Output**: The length of the modified array with duplicates removed.

#### Key Observations

- Since the array is sorted, duplicate elements will always be adjacent to each other.
- This property allows us to efficiently identify and remove duplicates without needing to compare each element with every other element.

#### Approach

To solve the problem, we can use the **two-pointer technique**:

1. **Two Pointers**:
   - Use one pointer to track the position of the last unique element found (`last_unique_idx`).
   - Use another pointer to iterate through the array (`current_idx`).

2. **Iterate through the Array**:
   - As we iterate with the `current_idx` pointer, we compare the current element with the last unique element (pointed to by `last_unique_idx`).
   - If they are different, it means we have found a new unique element.

3. **Update the Array**:
   - Increment the `last_unique_idx` to the next position and place the new unique element at that index.

4. **Return the Result**:
   - After processing all elements, the length of the modified array is `last_unique_idx + 1`, since array indices start at 0.

#### Complexity Analysis

- **Time Complexity**: O(n), where `n` is the number of elements in the array. We traverse the array once.
- **Space Complexity**: O(1), as we modify the array in place without using additional data structures.

### Summary

By leveraging the properties of sorted arrays and employing a two-pointer strategy, we can efficiently remove duplicates in a single pass, achieving optimal performance in both time and space.
