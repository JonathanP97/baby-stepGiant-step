import math

# n^x = g mod p
def get_answer(n, g, p):  
    large_steps = []
    baby_steps = []
    x = 0
    y = 0
    T = int(math.sqrt(p))
    print('!!!!!!!  Now solving {n}^x = {g} mod {p}  !!!!!!!\n'.format(n = n, g =g, p=p))
    
    # Generates 'traps' and appends to list
    ### too much time
    for i in range(0,100):
        temp = i*T
        y = (n**(temp)) % p
        large_steps.append(y)

    print('Here are your large steps', large_steps, '\nLooking for multiples now...\n')

    # Baby Steps
    for i in range(0,T):    
        # if i % 100 == 0:
        #     print('At ', i, 'steps')
        x = g*n**i % p
        baby_steps.append(x)
        if x in large_steps:
            if len(baby_steps) < 20:
                print(baby_steps)
            b_steps = large_steps.index(x) * T
            answer = b_steps - i
            return '''{x} appears twice\n{g}* (2^{i}) mod {p} = {x} = {n} ^ {b} mod {p}  It took {i} steps so...\n{n}^{a} = {g} mod {p}'''.format(x =x, g =g, i =i, p =p, n =n, a =answer,b = b_steps)                    
        
print(get_answer(2, 37, 101))
print(get_answer(3, 26, 463))
print(get_answer(5, 122104, 859051))

# not working 
### print(get_answer(7, 9777493488, 57688682951))