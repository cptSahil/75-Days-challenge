class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        l=[[0 for i in range(len(board[0]))] for j in range(len(board))]

        x=[1,1,1,0,0,-1,-1,-1]
        y=[1,-1,0,1,-1,1,-1,0]

        def isvalid(a,b):
            if 0<=a<len(board) and 0<=b<len(board[0]):
                return True 
        for i in range(len(l)):
            for j in range(len(l[0])):
                count=0
                for k in range(8):
                    a=x[k]+i
                    b=y[k]+j
                    if isvalid(a,b) and board[a][b]==1:
                        count+=1
                l[i][j]=count
            
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j]==1 and l[i][j]<2:
                    board[i][j]=0
                elif board[i][j]==1 and l[i][j]>3:
                    board[i][j]=0
                elif board[i][j]==0 and l[i][j]==3:
                    board[i][j]=1 