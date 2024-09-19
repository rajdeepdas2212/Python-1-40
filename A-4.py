def SI(p,r,t):
    return (p*r*t) / 100

p = int(input('Enter the principal: '))
r = int(input('Enter the rate: '))
t = int(input('Enter the time: '))

print(f'Simple interest is: {SI(p,r,t)}')