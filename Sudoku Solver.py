#Sudoku solving code
#X for where the number should not be
#0 for where the number might be

#Creating the board that will represent our game view
board = [[0, 0, 1, 7, 0, 2, 9, 0, 0],
         [8, 7, 0, 0, 0, 0, 0, 4, 2],
         [0, 0, 0, 0, 4, 0, 0, 0, 0],
         [6, 0, 0, 0, 5, 0, 7, 0, 9],
         [7, 0, 0, 0, 1, 0, 0, 0, 3],
         [4, 0, 2, 0, 8, 0, 0, 0, 1],
         [0, 0, 0, 0, 6, 0, 0, 0, 0],
         [2, 3, 0, 0, 0, 0, 0, 1, 6],
         [0, 0, 4, 5, 0, 3, 8, 0, 0],]

def print_board(board):
    print("\n")
    for i in board:
        print("-------------------------------------")
        print("|", i[0], "|", i[1],"|", i[2],"|", i[3],"|", i[4],"|", i[5],"|", i[6],"|", i[7],"|", i[8], "|")
        
    print("\n")

def row_checker(n, board):
    #checks each row in the board to see where n is missing and where n should not be
    #we make a copy of the board in order to manipulate it
    board_copy = board.copy()
    #print(board_copy)
    for i in board:
        if n not in i:
            if i.count(0) == 1:
                i[i.index(0)] = n

        else:
            for x in range(len(i)):
                if i[x] == 0:
                    i[x] = "X"     
    return board
    

def column_checker(n, board):
    board_copy = board.copy()
    for i in range(len(board)):
        column = [board[x][i] for x in range(9)]
        if n not in column:
            if column.count(0) == 1:
                board[i][column.index(0)] = n
        else:
            for a in range(len(column)):
                if board[a][i] == 0:
                    board[a][i] = "X"
    return board
        
        #column_list = [board[0][i], board[1][i], board[2][i], board[3][i], board[4][i], board[4][i], board[6][i], board[7][i], board[8][i], ]

def box_checker(n, board):
    box1 = [board[0][0], board[0][1], board[0][2], board[1][0], board[1][1], board[1][2], board[2][0], board[2][1], board[2][2]]
    dict1 ={"0": "00", "1": "01", "2": "02", "3": "10", "4": "11", "5": "12", "6": "20", "7": "21", "8":"22"}
    box2 = [board[0][3], board[0][4], board[0][5], board[1][3], board[1][4], board[1][5], board[2][3], board[2][4], board[2][5]]
    dict2 ={"0": "03", "1": "04", "2": "05", "3": "13", "4": "14", "5": "15", "6": "23", "7": "24", "8":"25"}
    box3 = [board[0][6], board[0][7], board[0][8], board[1][6], board[1][7], board[1][8], board[2][6], board[2][7], board[2][8]]
    dict3 ={"0": "06", "1": "07", "2": "08", "3": "16", "4": "17", "5": "18", "6": "26", "7": "27", "8":"28"}
    box4 = [board[3][0], board[3][1], board[3][2], board[4][0], board[4][1], board[4][2], board[5][0], board[5][1], board[5][2]]
    dict4 ={"0": "30", "1": "31", "2": "32", "3": "40", "4": "41", "5": "42", "6": "50", "7": "51", "8":"52"}
    box5 = [board[3][3], board[3][4], board[3][5], board[4][3], board[4][4], board[4][5], board[5][3], board[5][4], board[5][5]]
    dict5 ={"0": "33", "1": "34", "2": "35", "3": "43", "4": "44", "5": "45", "6": "53", "7": "54", "8":"55"}
    box6 = [board[3][6], board[3][7], board[3][8], board[4][6], board[4][7], board[4][8], board[5][6], board[5][7], board[5][8]]
    dict6 ={"0": "36", "1": "37", "2": "38", "3": "46", "4": "47", "5": "48", "6": "56", "7": "57", "8":"58"}
    box7 = [board[6][0], board[6][1], board[6][2], board[7][0], board[7][1], board[7][2], board[8][0], board[8][1], board[8][2]]
    dict7 ={"0": "60", "1": "61", "2": "62", "3": "70", "4": "71", "5": "72", "6": "80", "7": "81", "8":"82"}
    box8 = [board[6][3], board[6][4], board[6][5], board[7][3], board[7][4], board[7][5], board[8][3], board[8][4], board[8][5]]
    dict8 ={"0": "63", "1": "64", "2": "65", "3": "73", "4": "74", "5": "75", "6": "83", "7": "84", "8":"85"}
    box9 = [board[6][6], board[6][7], board[6][8], board[7][6], board[7][7], board[7][8], board[8][6], board[8][7], board[8][8]]
    dict9 ={"0": "66", "1": "67", "2": "68", "3": "76", "4": "77", "5": "78", "6": "86", "7": "87", "8":"88"}

    board_list = [box1, box2, box3, box4, box5, box6, box7, box8, box9]
    dict_list = [dict1, dict2, dict3, dict4, dict5, dict6, dict7, dict8, dict9]

    for box in board_list:
        if n in box:
            for i in range(9):
                if box[i] == 0:
                    my_dict = dict_list[board_list.index(box)]
                    pos = my_dict[str(i)]
                    board[int(pos[0])][int(pos[1])] = "X"
                    #box1[i] = "X"
                    
        else:
            if box.count(0) == 1:
                my_dict = dict_list[board_list.index(box)]
                pos = my_dict[str(box.index(0))]
                board[int(pos[0])][int(pos[1])] = n
    

    return board

def fix_board(board):
    #Fixes all the board, replaces all X's with 0's
    for i in board:
        for x in range(9):
            if i[x] == "X":
                i[x] = 0
    
    print_board(board)

def status(board):
    the_status = 0
    for i in board:
        for x in i:
            if x == "X":
                the_status += 1
            if x == 0:
                the_status += 1
    if the_status == 0:
        return True
    else:
        return False

            
def main():
    game_status = status(board)
    while game_status == False:
        game_status = status(board)
    #for a in range(3):
        for i in range(1,10):
            for x in range(2):
                box_checker(i, column_checker(i, row_checker(i, board)))
            fix_board(board)
    
main()
