import random

def roll():
    return random.randint(1,6)

players=[0 for x in range(4)]

while(max(players)<50):
    for i in range(len(players)):
        print('Player',i, 'turn')
        current_score=players[i]
        print('Your current score is:',current_score)
        want_to_play="y"
        while(want_to_play)=='y':
            value=roll()
            print("You rolled:",value)
            if value==1 or current_score>=50:
                break
            else:
                current_score+=value
            want_to_play=input("Do you want to continue?(y)")

        players[i]=current_score

    print(players)

print(players)
