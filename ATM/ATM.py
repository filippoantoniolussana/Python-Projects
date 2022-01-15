import sys

# Variable to store account balance 
account_balance = float(500.25)


# Function to display the current balance
def balance(account_balance):
  print('Your current balance:' + str(account_balance))
  

# Function for deposit
def deposit(account_balance, deposit_amount):
  account_balance = account_balance + deposit_amount
  return 'Deposit was $%.2f' % deposit_amount + ', current balance is $' + str(account_balance)
  
  
# Function for withdrawal
def withdrawal(account_balance, withdrawal_amount):
  if withdrawal_amount <= account_balance:
    account_balance = account_balance - withdrawal_amount
    return 'Withdrawal amount was $%.2f' %withdrawal_amount + ', ' + 'current balance is $%.2f' % account_balance
  elif withdrawal_amount > account_balance:
    return '$%.2f' %withdrawal_amount + ' is greater than your account balance of $' + str(account_balance)

  
# Conditional statement to call function based on user input
userchoice = input ("What would you like to do?\n")

if (userchoice == 'D'):
  deposit_amount = float(input('How much would you like to deposit today?\n'))
  print (deposit(account_balance, deposit_amount))   
elif (userchoice == 'W'):
  withdrawal_amount = float(input('How much would you like to withdraw today?\n'))
  print(withdrawal(account_balance, withdrawal_amount)) 
elif (userchoice == 'B'):
    balance(account_balance)
elif (userchoice == 'Q'):
  print('Thank you for banking with us.')
