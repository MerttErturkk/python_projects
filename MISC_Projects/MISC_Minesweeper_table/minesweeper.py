def minesweeper(bombs,n_rows,n_cols):
    
    field = [[0 for i in range(n_cols)]for j in range(n_rows)]
    for bomb_c,bomb_r in bombs:
        field[bomb_c][bomb_r]= "X"
    for x in range(n_cols):
        for y in range(n_rows):
            if field[x][y] =="X":
                if y != 0:
                    if x !=0:
                        try:
                            field[x-1][y-1] +=1
                        except:
                            pass
                    try:
                        field[x][y-1] +=1
                    except:
                        pass
                    try:
                        field[x+1][y-1] +=1
                    except:
                        pass
                if x !=0:    
                    try:
                        field[x-1][y] +=1
                    except:
                        pass
                    try:
                        field[x-1][y+1] +=1
                    except:
                        pass
                try:
                    field[x+1][y] +=1
                except:
                    pass            
                try:
                    field[x][y+1] +=1
                except:
                    pass
                try:
                    field[x+1][y+1] +=1
                except:
                    pass
    return field

a= minesweeper([[0,2],[4,4]],5,5)
