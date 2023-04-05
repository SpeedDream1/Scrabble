POINT_LETTRE = {'A':1, 'B':3, 'C':3, 'D':2, 'E':1, 'F':4, 'G':2, 'H':4, 'I':1, 
'J':8, 'K':10, 'L':1, 'M':2, 'N':1, 'O':1, 'P':3, 'Q':8, 'R':1, 'S':1, 'T':1, 
'U':1, 'V':4, 'W':10, 'X':10, 'Y':10, 'Z':10, '*': 0}

QTT_LETTRES = {'A':9, 'B':2, 'C':2, 'D':3, 'E':15, 'F':2, 'G':2, 'H':2, 'I':8, 
'J':1, 'K':1, 'L':5, 'M':3, 'N':6, 'O':6, 'P':2, 'Q':1, 'R':6, 'S':6, 'T':6, 'U':6, 
'V':2, 'W':1, 'X':1, 'Y':1, 'Z':1} # , '*': 2

O, T, t, D, d = '/', 'T', 't', 'D', 'd'
PLATEAU_CASE = [
    [T, O, O, d, O, O, O, T, O, O, O, d, O, O, T],
    [O, D, O, O, O, t, O, O, O, t, O, O, O, D, O], 
    [O, O, D, O, O, O, d, O, d, O, O, O, D, O, O], 
    [d, O, O, D, O, O, O, d, O, O, O, D, O, O, d], 
    [O, O, O, O, D, O, O, O, O, O, D, O, O, O, O], 
    [O, t, O, O, O, t, O, O, O, t, O, O, O, t, O], 
    [O, O, d, O, O, O, O, O, O, O, O, O, d, O, O], 
    [T, O, O, d, O, O, O, D, O, O, O, d, O, O, T], 
    [O, O, d, O, O, O, O, O, O, O, O, O, d, O, O], 
    [O, t, O, O, O, t, O, O, O, t, O, O, O, t, O], 
    [O, O, O, O, D, O, O, O, O, O, D, O, O, O, O], 
    [d, O, O, D, O, O, O, d, O, O, O, D, O, O, d], 
    [O, O, D, O, O, O, d, O, d, O, O, O, D, O, O], 
    [O, D, O, O, O, t, O, O, O, t, O, O, O, D, O], 
    [T, O, O, d, O, O, O, T, O, O, O, d, O, O, T],
]
del O, T, t, D, d

PLATEAU_DEPART = [['/']*15 for i in range(15)]