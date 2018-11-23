states = dict()
F, P, N = 0, 0, 0

line = input()
while line != '-1':
    state, status = line.split()
    if state not in states:
        states[state] = 0
    states[state] += 1
    if status is 'F':
        F += 1
    if status is 'P':
        P += 1
    if status is 'N':
        N += 1
    line = input()

print('Different States Surveyed = {}\nTotal Full Eclipses Reported = {}\nTotal Partial Eclipses Reported = {}\nTotal No Eclipses Reported = {}\nState With Most Responses = {}'\
.format(len(states), F, P, N, max(states, key=states.get)))