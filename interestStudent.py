def greeting():
    print('This interest calculator will ask you to select an interest rate,')
    print('followed by a principal value.  It will then calculate and display')
    print('the principal, interest rate, and balance after one year.  You will')
    print('then be invited to execute the process again or terminate.')
#---------------------------------------------------------------------------------
def getRate(choices):
    print('Please select an interest rate: ')
    for a,b in enumerate(choices, 65):
        print(chr(a)+')    '+str(b)+'%')
        
    letters = ['A','B','C','D','E','F']
    choices_str = list(map(str,choices))
    match = [i for i in zip(choices_str, letters) if None not in i]
    I=input('Enter a letter: ').upper()
    for x in match:
        if I == x[1]:
            Rate = int(x[0]) * 0.01
            break
        else:
            print('That is not a valid selection.')
            print('Please select an interest rate: ')
            for a,b in enumerate(choices, 65):
                print(chr(a)+')    '+str(b)+'%')
        
            letters = ['A','B','C','D','E','F']
            choices_str = list(map(str,choices))
            match = [i for i in zip(choices_str, letters) if None not in i]
            I=input('Enter a letter: ')
            I = I.upper()
    return float(Rate)
#---------------------------------------------------------------------------------
def getPrincipal(limit):
    while True:
        try:
            P=input('Enter the principal (limit '+str(limit)+'): ')
            if '.' in P:
                S = P.split('.')
                decimals = S[1]   
            else:
                decimals='00'
            if '$' in P:
                New=P.split('$')
                Principal=float(New[1])
            else:
                Principal=float(P)
            if Principal < 0:
                print('You must enter a positive amount')
            elif len(decimals) > 2:
                print('The principal must be specified in dollars and cents')
            elif Principal > limit:
                print('The principal can be at most '+str(limit))
            else:
                print(Principal)
                return(Principal)
        except ValueError:
            print('Please enter a number')
#---------------------------------------------------------------------------------
def computeBalance(Principal, rate):
   balance = Principal + (Principal * rate)
   balance = round(balance, 2)
   return balance
#---------------------------------------------------------------------------------
def displayTable(Principal, rate, balance):
    results = [(Principal, rate, balance)]
    labels=['Initial Principal', 'Interest Rate', 'End of Year Balance']
    header = f'{labels[0]:20}'+f'{labels[1]:20}'+f'{labels[2]:20}'
    print(header)
    print('===========================================================')
    results=f'{Principal:<20}'+f'{rate:<20}'+f'{balance:<20}'
    print(results)  
#---------------------------------------------------------------------------------
def askYesNo(prompt):
    valid=False
    while not valid:
        ans=input(prompt)
        if ans[0]=='y' or ans[0]=='Y':
            valid=True
            return True
        elif ans[0]=='n' or ans[0]=='N':
            valid=True
            return False
        else:
            valid=False
