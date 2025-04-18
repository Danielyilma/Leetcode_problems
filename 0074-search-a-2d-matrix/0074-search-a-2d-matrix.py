class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        low = 1
        high = len(matrix) * len(matrix[0])
        cols = len(matrix[0])

        while low <= high:
            mid = (low + high) // 2

            row = (mid - 1) // cols
            col = (mid - 1) % cols

            if matrix[row][col] == target:
                return True
            elif matrix[row][col] > target:
                high = mid - 1
            else:
                low = mid + 1
        
        return False
