class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        r = len(matrix)
        c = len(matrix[0])

        top = 0
        bottom = r - 1

        while top <= bottom:
            mid = (top + bottom) // 2

            if target < matrix[mid][0]:
                bottom = mid - 1
            elif target > matrix[mid][-1]:
                top = mid + 1

            else:
                left = 0
                right = c - 1

                

                while left <= right:
                    col_mid = (left + right) // 2
                    
                    if matrix[mid][col_mid] == target:
                        return True
                    elif matrix[mid][col_mid] < target:
                        left = col_mid + 1
                    else:
                        right = col_mid - 1
                    
                return False

        return False        
        





    



        
        

        