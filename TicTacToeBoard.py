class TicTacToeBoard:
    field =[['*']*3 for i in range (3)]

    def new_game(self):
        print('New game has been started')
        TicTacToeBoard.field =[['*']*3 for i in range (3)]
    
    def get_field(self):
        for i in range (3):
            for j in range (3):
                print (TicTacToeBoard.field[i][j], end = ' ')
            print()
        
    def check_field(self,check):
        if (self.check_head_gorizontal(check)==True or self.check_side_gorizontal(check) == True or self.check_line(check)==True):
            return True
        return False

    def check_head_gorizontal(self, check):
        result = 0
        for i in range (3):
            for j in range (3):
                if i == j and self.field[i][j] == check:
                    result+=1
        if result == 3:
            return True
        return False
    
    def check_side_gorizontal(self,check):
        result = 0
        for i in range (3):
            for j in range (3):
                if i == (4-i) and self.field[i][j] == check:
                    result+=1
        if result == 2:
            return True
        return False

    def check_line (self,check):
        resultHorizontal = 0
        resultVertical = 0
        for i in range (3):
            for j in range (3):
                if(self.field[i][j]==check):
                    resultHorizontal+=1
                if j+2<3:
                    if(self.field[i][j+1]!=check and self.field[i][j+1]!='*' ):
                        resultHorizontal=0
            if(resultHorizontal==3):
                return True
                break
            resultHorizontal=0
        for j in range (3):
            for i in range (3):
                if(self.field[i][j]==check):
                    resultVertical+=1
                if i+2<3:
                    if(self.field[i+1][j]!=check and self.field[i+1][j]!='*' ):
                            resultVertical=0
            if(resultVertical==3):
                return True
                break
            resultVertical=0
    def is_field_full (self):
        for i in range (3):
            for j in range (3):
                if self.field[i][j]=='*':
                    return False
        return True

    def make_move(self,param):
        print('Make your turn. Enter data in format (row col)')
        value=input()
        value.split()
        row = int(value[0])-1
        col = int(value[2])-1
        if(row > 3 or col > 3 or param > 1 ):
            print ('data is wrong')
            print('Make your turn. Enter data in format (row col)')
            value=input()
            value.split()
            row = int(value[0])-1
            col = int(value[2])-1
        elif(self.check_free_point(row,col)==False):
            print('It is impossible to make a move - the cell is occupied')
            print('Make your turn. Enter data in format (row col)')
            value=input()
            value.split()
            row = int(value[0])-1
            col = int(value[2])-1
        TicTacToeBoard.field[row][col]=param

    def check_free_point(self,row,col):
        if self.field[row][col]!='*':
            return False
        return True 

game=TicTacToeBoard()
