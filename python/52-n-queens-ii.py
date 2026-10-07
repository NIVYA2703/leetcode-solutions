class Solution:
    def totalNQueens(self, n):
        
        count = 0
        
        # Columns where queens are already placed
        columns = set()
        
        # Diagonal: row - column
        diagonal1 = set()
        
        # Diagonal: row + column
        diagonal2 = set()
        
        def backtrack(row):
            nonlocal count
            
            # All queens have been placed
            if row == n:
                count += 1
                return
            
            for col in range(n):
                
                # Check if this position is under attack
                if col in columns:
                    continue
                
                if row - col in diagonal1:
                    continue
                
                if row + col in diagonal2:
                    continue
                
                # Place queen
                columns.add(col)
                diagonal1.add(row - col)
                diagonal2.add(row + col)
                
                # Move to next row
                backtrack(row + 1)
                
                # Remove queen (backtracking)
                columns.remove(col)
                diagonal1.remove(row - col)
                diagonal2.remove(row + col)
        
        backtrack(0)
        
        return count
        
