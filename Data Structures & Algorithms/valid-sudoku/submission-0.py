class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for r in range(9):
            for c in range(9):
                num = board[r][c]
                if num == ".":
                    continue
                
                #check row
                if num in rows[r]:
                    return False
                rows[r].add(num)

                #check col
                if num in cols[c]:
                    return False
                cols[c].add(num)

                #check boxes
                box_idx = (r // 3) * 3 + (c // 3)
                if num in boxes[box_idx]:
                    return False
                boxes[box_idx].add(num)
        
        return True

        