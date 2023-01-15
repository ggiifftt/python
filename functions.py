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

def disp_board(board):

def input_pos(board):

def victory(whose):