import random
from wordlist import abcd
n = random.randint(0,2464)
w = abcd[n]
l = len(w)
possible = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

answer = []
for k in range(l):
    answer.append(w[k])
board = []

for i in range(l):
    board.append('_')

def indices(word, letter):
    ind = []
    for i in range(len(word)):
        if word[i] == letter:
            ind.append(i)
    return ind

def guess():
    count = 0
    print(' '.join(board))
    while count<10:
        g = input("Enter your guess: ")
        if g=="quit":
            return
        if g not in possible:
            print("You have already guessed this!")
            continue
        if g in w:
            print("Correct guess!")
            for n in indices(w,g):
                board[n]=g
            print(' '.join(board))
            possible.remove(g)
        else:
            print("Wrong guess!")
            count+=1
            possible.remove(g)
            print(f"{10-count} chances left!")
            if count==10:
                print("You lose!")
                print(f"The word was {w}")
        if board==answer:
            print("You win!")
            return

guess()