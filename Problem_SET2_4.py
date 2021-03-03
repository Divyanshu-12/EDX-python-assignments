balance =28774.23

annualInterestRate = 0.2


monthlyIntRate = annualInterestRate/12.0
low = balance/12.0
high = (balance *(1 + monthlyIntRate)**12) / 12.0
lowestPayment = (low+high)/2
finding = True

def payment(balance,annualInterestRate,lowestPayment):
    month = 1
    while month <= 12:
 
        balance -= lowestPayment
        balance += (monthlyIntRate*balance)
        month +=1
        
    return balance
        
while finding:
    
    x=payment(balance,annualInterestRate,lowestPayment)
    
    if  round(x) < 0:
        high = lowestPayment
        lowestPayment = (high + low)/2
    elif round(x) > 0:
        low = lowestPayment
        lowestPayment = (high + low)/2
    elif round(x) == 0:
        finding = False
        print('Lowest Payment:',round(lowestPayment,2))
