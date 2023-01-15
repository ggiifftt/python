from functions import log_in
cnt = 0
while True:
    i = input('아이디를 입력하세요: ')
    j = input('비밀번호를 입력하세요: ')
    if (log_in(i,j)):
        print(i + '님이 로그인 되었습니다.')
        break
    else:
        print("아이디나 비밀번호를 확인해주세요.")
    cnt += 1
    if cnt > 3:
        print("로그인 횟수가 3회를 초과했습니다. 종료합니다.")
        exit()

input("원하는 문양을 입력하세요 (O/X)")

board = ['*'] * 9
disp_board(board)

while True:
    input_pos(board)

    disp_board

    victory(board_player)