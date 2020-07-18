#...............................................................................

secret_number = 10
life = 0


while life < 5 :
    picked_number = int(input("pick a number from 0 to 15 :  "))

#removes a life if picked number is wrong
    if picked_number != secret_number :
        life += 1
#if you choose the right number you will win
    else :
        print('You won ')
        break
#says if the player don't respects the rules
    if picked_number > 15:
        print("Read the rules my boy")
#endgame statement
else:
    print('You lose')
