def log_in(input_ID, input_PW):
    real_id = ""
    real_pw = ""
    file = open("login.txt", "r", encoding="utf8")
    lines = file.readlines()
    for line in lines:
        key,value = line.split()
        if value[-2] == '\n':
            value = value.replace('\n', '')
        if key == "ID:":
            real_id = value
        else:
            real_pw = value
            if real_id == input_ID and real_pw == input_PW:
                return True
    return False
def sellect():
    computer = ''
    while True:
        player = input("원하는 문양을 입력하세요. (O/X): ")
        if player in ['O', 'X']:
            if player == 'O':
                computer += 'X'
            else:
                computer += 'O'
            break
        else:
            print('O 또는 X중 입력해주세요.')

def disp_board(board):
    board = ['*'] * 9
    for i in range(3): # 0~2
        print('⌜-----------⌝')
        print('| ' + board[i*3] + ' | ' + board[i*3+1]+ ' | ' + board[i*3+2] + ' |')
    print('⌞-----------⌟')
# ⌜-----------⌝
# | * | * | * |
# -------------
# | * | * | * |
# -------------
# | * | * | * |
# ⌞-----------⌟

def input_pos(board):
    while True:
        pos = int(input('원하는 자리를 입력하세요. '))
        if pos in range(len(board)):
            if board[pos] == '*':
                board.replace(board[pos],player)
            else:
                print('이미 선택된 자리입니다.')
        else:
            print('범위를 벗어났습니다.')
# def victory(whose):
