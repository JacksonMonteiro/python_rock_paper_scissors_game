import random
isTie = True

def checkWinner(choices):
    """
    Check the choices values. If the player and computer chose the same thing, it's a tie. 
    if the choices values are different, the player win or lose the game.

    choices: a dictionary with two keys: 'player' and 'computer'
    """
    global isTie

    print('You chose {} and the computer chose {}'.format(choices['player'], choices['computer']))

    if choices['player'] == choices['computer']:
        print('It\'s a tie')
    elif choices['player'] == 'rock':
        if choices['computer'] == 'scissor':
            print("You won the game")
            isTie = False
        else:
            print("You lost the game")
            isTie = False
    elif choices['player'] == 'paper':
        if choices['computer'] =='rock':
            print("You won the game")
            isTie = False
        else:
            print("You lost the game")
            isTie = False
    elif choices['player'] == 'scissor':
        if choices['computer'] =='paper':
            print("You won the game")
            isTie = False
        else: 
            print("You lost the game")
            isTie = False


# A while loop that will keep running until the user wins or loses.
while isTie == True:
    def getChoices(): 
        playerChoice = input('Select your choice(rock, paper, scissor): ')
        computerChoice = random.choice(['rock', 'paper', 'scissor'])

        return {
            'player': playerChoice, 
            'computer': computerChoice
        }
    
    checkWinner(getChoices())