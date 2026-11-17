import tkinter as tk
import random

wins = 0
losses = 0
ties = 0
cardsExist = ['2','3','4','5','6','7','8','9','10','J','Q','K','highA']
cardsValues = {
    'lowA':1,
    "2":2,
    '3':3,
    '4':4,
    '5':5,
    '6':6,
    '7':7,
    '8':8,
    '9':9,
    '10':10,
    'J':10,
    'Q':10,
    'K':10,
    'highA':11,
}
deck = cardsExist*4
playerCards = []
dealerCards = []

def endRound(message):
    results.config(text=message)
    restartButton.config(state='normal')
    standButton.config(state='disabled')
    hitButton.config(state='disabled')
    wlt.config(text=f"Wins/Losses/Ties: {wins}/{losses}/{ties}")

def hit():
    global losses
    playerCards.append(deck.pop())
    if handValue(playerCards)>21:
        losses += 1
        endRound(f"You have {playerCards}, with a value of {handValue(playerCards)}, which is over 21, meaning you lose")
    else:
        results.config(text=f"You have {playerCards}, with a value of {handValue(playerCards)}, and dealer has {dealerCards[0]}")
        
        
def stand():
    global wins, losses, ties
    while handValue(dealerCards)<17:
        dealerCards.append(deck.pop())
    dealerValue = handValue(dealerCards)
    playerValue = handValue(playerCards)
    if dealerValue > 21:
        wins += 1
        endRound(f"Dealer busts with {dealerCards}, or {dealerValue}")
    elif dealerValue > playerValue:
        losses += 1
        endRound(f"Dealer has {dealerCards}, which is higher than your {playerCards}")
    elif playerValue > dealerValue:
        wins += 1
        endRound(f"You win with {playerCards}, which is higher than the dealer's {dealerCards}")
    else:
        ties += 1
        endRound(f"It is a tie, with your {playerCards} equaling the dealer's {dealerCards}")

def handValue(cards):
    value = 0
    for c in cards:
        value+=cardsValues[c]
    while value >21 and cards.count('highA')>0:
        indexOf = cards.index('highA')
        cards[indexOf] = 'lowA'
        value = 0
        for c in cards:
            value+=cardsValues[c]
    value = 0
    for c in cards:
        value+=cardsValues[c]
    return value

def newGame():
    restartButton.config(state='disabled')
    for c in (hitButton,standButton):
        c.config(state='normal')
    global playerCards, dealerCards, deck
    playerCards = []
    dealerCards = []
    deck = cardsExist*4
    random.shuffle(deck)
    for _ in range(2):
        playerCards.append(deck.pop())
        dealerCards.append(deck.pop())
    results.config(text=f"You have {playerCards}, with a value of {handValue(playerCards)}, and dealer has {dealerCards[0]}")

root = tk.Tk()
root.title('Ok')
root.geometry('800x600')

results = tk.Label(root,text='Results will be here')
results.pack(padx=10,pady=10)

buttonRow = tk.Frame(root)
buttonRow.pack(pady=10)

hitButton = tk.Button(buttonRow,text='Hit',command=hit)
standButton = tk.Button(buttonRow,text="Stand",command=stand)
restartButton = tk.Button(buttonRow,text='Restart',command=newGame)
hitButton.pack(padx=10,side='left')
standButton.pack(padx=10,side='left')
restartButton.pack(padx=10,side='left')


wlt = tk.Label(root,text='Wins/Losses/Ties: 0/0/0')
wlt.pack(side='left',padx=10,pady=10)

newGame()

root.mainloop()
