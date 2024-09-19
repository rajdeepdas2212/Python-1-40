def compund_interest(Priencipal,rate,time):
    Amount = Priencipal * (pow((1 + rate / 100),time))
    CI = Amount - Priencipal
    return CI

p = int(input('Enter the Priencipal balance: '))
r = int(input('Enter the rate of interest: '))
t = int(input('Enter the time period: '))

print(f'Compund interest is: {compund_interest(p,r,t)}')