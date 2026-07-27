class Solution:

    def isValidRow(self, row: List[str]) -> bool:
        s = set()
        for ch in row:
            if ch in s and ch!='.':
                return False
            else:
                s.add(ch)

        return True

    def isValidMat(self, board: List[List[str]], i, j) -> bool:
        s = set()
        for start in range(i,i+3):
            for end in range(j, j+3):
                ch = board[start][end]
                if ch in s and ch!='.':
                    return False
                else:
                    s.add(ch)

        return True

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # 1. First check rows
        # 2. Check all colums
        # 3. Finally check all matrices of 3x3

        # Checks #1
        for row in board:
            if not self.isValidRow(row):
                return False
        
        # Checks #2
        for row in zip(*board):
            if not self.isValidRow(row):
                return False

        # Checks #3
        for i in range(0, len(board), 3):
            for j in range(0, len(board[0]), 3):
                if not self.isValidMat(board, i, j): 
                    return False


        return True


        