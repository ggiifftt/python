from functions import *

cnt = 0
while True:
    i = input('아이디를 입력하세요: ')
    j = input('비밀번호를 입력하세요: ')
    if (log_in(i,j)):
        print(i + '님이 로그인 되었습니다.')
        break
    else:
        cnt += 1
        print("아이디나 비밀번호를 확인해주세요.")
    if cnt > 3:
        print("로그인 횟수가 3회를 초과했습니다. 종료합니다.")
        exit()
sellect()
board = ['*'] * 9
disp_board(board)

while True:
    input_pos(board)
    disp_board(board)
    # if victory(board_player):
    #     print('Player Win!')