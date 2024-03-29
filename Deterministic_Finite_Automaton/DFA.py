# Finite automaton - any

#%% USER SETTINGS (free to edit)

Q = {0, 1, 2}   # states (numbers should start from 0)
S = {'0','1'}   # alphabet
q0 = 0          # start state (should be member of Q)
F = {2}         # set(!) of accept states (members of Q)

# transition function (dict: keys should be members of S, values should be tuples with members of Q)
d = {'0': (0,0,2),
     '1': (1,2,2)}
# e.g. transition when getting letter 'a' when in state 2: d['a'][2] will output 3


# automaton
M = (Q, S, d, q0, F) 



#%% FUNCTIONS (do not edit!)
def simulateDFA(M, inputWord):

    # extract elements
    Q = M[0]
    S = M[1]
    d = M[2]
    q0 = M[3]
    F = M[4]

    currentState = q0

    for letter in inputWord:
        print(f'letter: {letter} | state: {currentState}')

        if letter not in S:
            return "REJECT"
        
        currentState = d[letter][currentState]
        print(f'Moved to state: {currentState}')

    # after processing all input letters
    if currentState in F:
        return "ACCEPT"
    
    return "REJECT"
            


#%% SIMULATE (do not edit!)

# give it some words
decision = 1

while decision:
    print('Give input word containing only letters from the alphabet:\n')
    for s in S:
        print(f'{s}', end=' ')

    word = input('\n\nUser input: ')
    
    result = simulateDFA(M, word)
    print(result)
    decision = int(input('Try again? (1 - yes, 0 - no) : '))

print('It was fun! Bye!')
