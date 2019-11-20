import numpy as np

def setup():
    arr = np.array([['' for i in range(0,3)] for j in range(0,3)])
    return arr

def check_input(arr,x,y):
    try:
        arr[x,y]
    except:
        print("Enter the right coordinates!")
        return False
    if arr[x,y] == '':
        pass
    else:
        print("Place already full, try again")
        return False
    return True

def enter(arr, turn, player):
    try:
        x,y = [int(i) for i in input(f"Enter Coordinates for {player}: ").split(',')]
    except:
        print("Invalid Input Try Again")
        raise Exception
    if not check_input(arr,x,y):
        raise Exception
    if turn == True:
        arr[x,y] = 'X'
    else:
        arr[x,y] = 'O'
    return arr, x, y
    

def check_strike(arr,x,y, strike):
    print(arr, x, y, strike)
    if len(set(arr[:,y])) == 1:
        strike = True
    elif len(set(arr[x,:])) ==1:
        strike = True
    elif x == y:
        if(len(set(arr.diagonal()))) == 1:
            strike = True
    elif (x,y) in [(2,1), (0,2),(1,1)]:
        if(len(set(arr.diagonal(1)))) == 1:
            strike = True
    return strike

def display(arr):
    print(arr)

if __name__ == "__main__":
    arr = setup()
    display(arr)
    strike = False
    turn = True
    while not strike:
        if '' in arr:
            player = 'X' if turn else 'O'
            try:
                arr,x,y = enter(arr, turn, player)
            except:

                continue
            display(arr)
            strike = check_strike(arr,x,y,strike)
            turn = not turn
            if(strike):
                print(f"Congratulations,{player} won, papa pee pee")
        else:
            print("Its Draw!");