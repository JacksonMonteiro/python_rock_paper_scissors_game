import random
isTie = True

def checkWinner(choices):
    global isTie

    print('You chose {} and the computer chose {}'.format(choices['player'], choices['computer']))

    if choices['player'] == choices['computer']:
        print('It\'s a tie')
    elif choices['player'] == 'rock':
        if choices['computer'] == 'paper':
            isTie = False
            print("You won the game")
        else:
            print("You lost the game")
            isTie = False
    elif choices['player'] == 'paper':
        if choices['computer'] =='scissor':
            print("You won the game")
            isTie = False
        else:
            print("You lost the game")
            isTie = False
    elif choices['player'] == 'scissor':
        if choices['computer'] =='rock':
            print("You won the game")
            isTie = False
        else: 
            print("You lost the game")
            isTie = False


while isTie == True:
    def getChoices(): 
        playerChoice = input('Select your choice(rock, paper, scissor): ')
        computerChoice = random.choice(['rock', 'paper', 'scissor'])

        return {
            'player': playerChoice, 
            'computer': computerChoice
        }
    
    checkWinner(getChoices())

