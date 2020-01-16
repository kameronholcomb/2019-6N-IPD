import random

def move(my_history, their_history, my_score, their_score):

    if len(my_history)==0: # It's the first round; collude.
        return 'c'
    elif my_history[-1]=='c' and their_history[-1]=='b':
        return 'b' # Betray if they were severely punished last time,
    else:
        return 'c' # otherwise collude.
        
    random_letter = random.choice('cb')
    print (random_letter)

print()
answer = input('Will you collude (c) or betray (b)? ')
if answer == 'collude' or 'c':
    print ('c')
if answer == 'betray' or 'b':
    print ('b')