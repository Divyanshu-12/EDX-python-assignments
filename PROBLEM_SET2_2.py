def remaining_bal(bal, annualIR, monthly_PR):
  minimum_pay = bal * monthly_PR
  unpaid_bal = bal - minimum_pay
  updated_bal = unpaid_bal * (annualIR / 12)
  remaining = unpaid_bal + round(updated_bal, 2)
    
  return(round(remaining, 2), annualIR, monthly_PR)
    
m = 12
balance = 42
annualInterestRate = 0.2
monthlyPaymentRate = 0.04
while(m > 0):
  balance, annualInterestRate, monthlyPaymentRate = remaining_bal(balance, annualInterestRate, monthlyPaymentRate)
  m -= 1
print(f"Remaining balance: {balance}")
