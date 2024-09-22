def checkWinner(a):
    if (a[0]==a[1]==a[2]) or (a[3]==a[4]==a[5]) or (a[6]==a[7]==a[8]) or (a[0]==a[3]==a[6]) or (a[1]==a[4]==a[7]) or (a[2]==a[5]==a[8]) or (a[0]==a[4]==a[8]) or (a[2]==a[4]==a[6]):
        return 1
    else:
        return 0

a=[1,2,3,4,5,6,7,8,9]
turn=0
counter=1
print(f"{a[0]}|{a[1]}|{a[2]}")
print(f"{a[3]}|{a[4]}|{a[5]}")
print(f"{a[6]}|{a[7]}|{a[8]}")
while 1:
    if turn==0:
        print("Player 1 turn")
        player1=int(input("Enter a number to fix position"))
        while a[player1-1]!="0":
            a[player1-1]='X'
            turn=1
            break

    else:
        print("Player 2 turn")
        player2=int(input("Enter a number to fix position"))
        while a[player2-1]!="X":
            a[player2-1]='0'
            turn=0
            break
    
    print(f"{a[0]}|{a[1]}|{a[2]}")
    print(f"{a[3]}|{a[4]}|{a[5]}")
    print(f"{a[6]}|{a[7]}|{a[8]}")
    isWinner=checkWinner(a)
    if isWinner==1:
        if turn==1:
            print("Player 1 is winner")
        else:
            print("Player 2 is winner")
        break
    else:
        pass