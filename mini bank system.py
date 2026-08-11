import json
try:
    with open("accounts.json", "r") as file:
        accounts = json.load(file)
except FileNotFoundError:
    accounts = {}
except json.JSONDecodeError:
    accounts = {}
def create():
    history=[]
    num=int(input('Enter the account number: '))
    if num not in accounts:
        name=str(input('enter the name: '))
        balance=int(input('enter the initial balance: '))
        accounts[num]={}
        accounts[num]['name']=name
        accounts[num]['balance']=balance
        accounts[num]['history']=history
        
        
    else:
        print('the number in already exist')
    
def show():
    print('===== Accounts =====')
    if not accounts:
        print('there is not accounts.')
    else:
        for key, value in accounts.items():
            print(f"Account: {key}\n Name: {value['name']}\n Balance: {value['balance']}SAR")
        
def deposit():
    ch=int(input('choose the account number: '))
    if ch not in accounts:
        print('account not exist.')
    else:
        depo=int(input('how much you want to depose: '))
        accounts[ch]['balance']+=depo
        print('depose success.')
        accounts[ch]['history'].append((f"deposit:+{depo} SAR"))
    
def withdraw():
    ch=int(input('choose the account number: '))
    if ch not in accounts:
        print('account not exist.')
    else:
        wit=int(input('how much you want to withdraw: '))
        if wit<=accounts[ch]['balance']:
            accounts[ch]['balance']-=wit
            print('withdraw success.')
            accounts[ch]['history'].append((f"withdraw: -{wit} SAR"))

        else:
            print('you can not withdraw mony more than you have in account.')
    
def transfer():
    ch=int(input('choose the account number: '))
    if ch not in accounts:
        print('account not exist.')
    else:
        ch1=int(input('choose the account number you want to transfer to it: '))
        if ch1 not in accounts:
            print('account not exist.')
        else:
            num=int(input('how much amount you want to transfer: '))
            if num>accounts[ch]['balance']:
                print('the amount  does not accept')
            else:
                accounts[ch]['balance']-=num
                accounts[ch1]['balance']+=num
                print('transfer success')
                accounts[ch]['history'].append((f"transfer to{ch1}:-{num} SAR"))
                accounts[ch1]['history'].append((f"transfer to {ch}: +{num} SAR"))
def history():
    ch1=int(input('choose the account number: '))
    if ch1 not in accounts:
        print('account not exist.')
    else:
        print('===== Transaction History =====')
        print(accounts[ch1]['history'])
        
    
    
def save():
    with open("accounts.json", "w") as file:
        json.dump(accounts,file)
    
    
while True:
    print('====Bank System====\n 1.create account\n 2.show account\n 3.deposit money\n 4.withdraw money\n 5.transfer money\n 6.the history\n 7.save data\n 8.Exit')
    ans=int(input('choose: '))
    if ans==1:
        create()
    elif ans==2:
        show()
    elif ans==3:
        deposit()
    elif ans==4:
        withdraw()
    elif ans==5:
        transfer()
    elif ans==6:
        history()
    elif ans==7:
        save()
    elif ans==8:
        break
