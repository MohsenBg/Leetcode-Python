# Pascal's Triangle

## Problem:
Given an integer `numRows`, generate the first `numRows` of Pascal's Triangle.

- Each row in Pascal's Triangle represents the coefficients of the binomial expansion.
- The first and last element of each row are always `1`.
- Each element in between is the sum of the two elements directly above it from the previous row.

## Approach:

### 1. **Initialization**:
   - The first row of Pascal's Triangle is always `[1]`.
   - We start by initializing the triangle with this row as the base case.

### 2. **Building Each Row**:
   - For each subsequent row:
     - Begin by appending a `1` at the start.
     - For the middle elements, calculate the sum of the two elements directly above it from the previous row.
     - Append a `1` at the end of the row.

### 3. **Time Complexity**:
   - The time complexity is **O(numRows²)**, because for each row, we perform a linear number of operations relative to its length.

## Example:

If `numRows = 5`, the Pascal's Triangle would look like this:

```plaintext
[
     [1],
    [1, 1],
   [1, 2, 1],
  [1, 3, 3, 1],
 [1, 4, 6, 4, 1]
]
```
# Explanation

### First Row:
   - The first row is `[1]`.

### Second Row:
   - Start with `[1]`.
   - There are no middle elements, so append another `1` → `[1, 1]`.

### Third Row:
   - Start with `[1]`.
   - Middle element = sum of the two elements directly above from the second row → `1 + 1 = 2`.
   - Append `1` at the end → `[1, 2, 1]`.

### Subsequent Rows:
   - Repeat the process for additional rows:
     - Append `1` at the start and end.
     - Calculate the middle elements as the sum of the two values directly above from the previous row.

---

# Conclusion:

### For any row `i`:
   - The first element is always `1`.
   - For each middle element `j`, the value is `triangle[i-1][j-1] + triangle[i-1][j]`.
   - The last element is always `1`.

### Efficiency:
   - This approach ensures that each row is built efficiently based on the previous row.
