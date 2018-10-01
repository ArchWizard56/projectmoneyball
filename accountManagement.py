#Import modules
import random
import json
#Load our accounts from the JSON file
global accounts
with open('accounts.json', 'r') as infile:  
    accounts = json.load(infile)

#Function to create a new account with a password
def createAccount(password):
    #Generate a random account number
    accountNumber = random.randint(100000,999999)

    #Create a dictionary entry with password and starting balance
    accounts.update({accountNumber:{
            "password": password,
            "balance": {
                "gold": 100
                }
            }})
    #Dump the new accounts to the file
    with open('accounts.json', 'w') as outfile:  
        json.dump(accounts, outfile)

    return accountNumber

def checkBalance(accountNumber, password):
    #Check the account balance if the account number is right and if the password is right
    try:
        if accounts[accountNumber]["password"] == password:
            return 0, accounts[accountNumber]["balance"]
        else:
            return 1, "Access Denied"
    except KeyError:
        return 1, "Wrong Account Number"

def transfer(fromAccount,toAccount,password,resource,amount):
    #Check that the account numbers are right and that the password is correct
    amount = abs(amount)
    try:
        if accounts[fromAccount]["password"] == password:
                returnString = "Transferred "
                #Update the account balance if the account has enough balance
                if accounts[fromAccount]["balance"][resource] - amount >= 0:  
                    accounts[toAccount]["balance"][resource] = accounts[toAccount]["balance"][resource] + amount
                    accounts[fromAccount]["balance"][resource] = accounts[fromAccount]["balance"][resource] - amount
                    returnString = returnString + str(amount) + " " + str(resource)
                else:
                    return 1, "Not enough balance to transfer " + str(amount) + " " + str(resource)
                returnString = returnString + " to " + str(toAccount)
                with open('accounts.json', 'w') as outfile:  
                    json.dump(accounts, outfile)
                return 0, returnString 
        else:
            return 1, "Access Denied"
    except KeyError:
        return 1, "Wrong Account Number"
print(transfer("257935", "635248", "helloWorld", "gold", -10))
