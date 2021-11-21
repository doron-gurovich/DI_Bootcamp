# -*- coding: utf-8 -*-

def display_board(*args):
    
    """
    Info: To display the Tic Tac Toe board (GUI).
    """
    
    str_len = 16
    
    s1 = ""
    for i in range(0, str_len):
        if i == 0 or i == str_len - 1:
            s1 += '*'
        elif i%5 == 0:
            s1 += '|'
        else:
            s1 += ' '
    
    s1 = ''.join(s1)
    
    s2 = ""
    for i in range(0, str_len):
        if i == 0 or i == str_len - 1:
            s2 += '*'
        elif i%5 == 0:
            s2 += '|'
        elif i == 1 or i == str_len - 2:
            s2 += ' '
        else:
            s2 += '_'
    
    s2 = ''.join(s2)
    
    s1_1 = s1
    s1_2 = s1
    s1_3 = s1
    
    input_matrix = list(args).copy()
    
    if input_matrix[0][0] != "Empty":
        temp = list(s1_1)
        temp[3] = input_matrix[0][0]
        
        s1_1 = ''.join(temp)
    if input_matrix[0][1] != "Empty":
        temp = list(s1_1)
        temp[7] = input_matrix[0][1]
        
        s1_1 = ''.join(temp)
    if input_matrix[0][2] != "Empty":
        temp = list(s1_1)
        temp[12] = input_matrix[0][2]
        
        s1_1 = ''.join(temp)
    if input_matrix[1][0] != "Empty":
        temp = list(s1_2)
        temp[3] = input_matrix[1][0]
        
        s1_2 = ''.join(temp)
    if input_matrix[1][1] != "Empty":
        temp = list(s1_2)
        temp[7] = input_matrix[1][1]
        
        s1_2 = ''.join(temp)
    if input_matrix[1][2] != "Empty":
        temp = list(s1_2)
        temp[12] = input_matrix[1][2]
        
        s1_2 = ''.join(temp)
    if input_matrix[2][0] != "Empty":
        temp = list(s1_3)
        temp[3] = input_matrix[2][0]
        
        s1_3 = ''.join(temp)
    if input_matrix[2][1] != "Empty":
        temp = list(s1_3)
        temp[7] = input_matrix[2][1]
        
        s1_3 = ''.join(temp)
    if input_matrix[2][2] != "Empty":
        temp = list(s1_3)
        temp[12] = input_matrix[2][2]
        
        s1_3 = ''.join(temp)
    
    
    dict_result = {
        1: ''.join(['*' for i in range(0, str_len)]),
        2: s1_1,
        3: s2,
        4: s1_2,
        5: s2,
        6: s1_3,
        7: s1,
        8: ''.join(['*' for i in range(0, str_len)])
        }  
    
    result = f"""
        {list(dict_result.values())[0]}
        {list(dict_result.values())[1]}
        {list(dict_result.values())[2]}
        {list(dict_result.values())[3]}
        {list(dict_result.values())[4]}
        {list(dict_result.values())[5]}
        {list(dict_result.values())[6]}
        {list(dict_result.values())[7]}
    """

    print(result)


def which_player(player):
    """
    Info: define which player we talking with. Convert bool --> string
    """
    
    return "first" if player else "second"

def which_player_sign(player):
    """
    Info: define which player we talking with. Convert bool --> string
    """
    
    return "X" if player else "0"


def player_input(player, *args):
    """
    Info: To get the position from the player.
    """
    
    result_matrix = list(args).copy()
    
    x = int(input("enter raw: ")) - 1
    y = int(input("enter column: ")) - 1
    
    result_matrix[x][y] = which_player_sign(player)
    
    return result_matrix

def check_win(*args):
    
    """
    Info: To check whether there is a winner or not
    """
    
    result = False
        
    for el in list(args):
       if el.count('X') == 3 or el.count('0') == 3:
           result = True
    
    tr_args = list(zip(*(list(args)))) # transpose the list of strings
    
    for el in list(tr_args):
       if el.count('X') == 3 or el.count('0') == 3:
           result = True
    
    return result

def play():
    """
    Info: The main function, which calls all the functions created above.
    """
    
    player_is_first = True
    matrix = [["Empty", "Empty", "Empty"],
              ["Empty", "Empty", "Empty"],
              ["Empty", "Empty", "Empty"]]

    
    try:
        while True:
            display_board(*matrix)
            matrix = player_input(player_is_first, *matrix)
            
            print(matrix)
            
            if check_win(*matrix):
                print(f"we have a winner! congrats ({which_player(player_is_first)})!")
                display_board(*matrix)
                break
            
            player_is_first = not player_is_first
            
    except:
        print("something went wrong :( ")
    
    return matrix

p1 = play()