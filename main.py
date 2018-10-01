# Import needed modules
import json
import discord
import accountManagement
from discord.ext import commands

#Load Config
with open("config.json", "r") as config_file:
    config = json.load(config_file)

#Create a new bot object
bot = commands.Bot(command_prefix='$')

#Let the user know that we've connected
@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
#Example commands
@bot.command()
async def createaccount(ctx, password: str):
    await ctx.send("Your account number is: " + str(accountManagement.createAccount(password)))

@bot.command()
async def transfer(ctx, fromAccount: str, toAccount: str, password: str, resource: str, amount: int):
    returnValue = accountManagement.transfer(str(fromAccount), str(toAccount), password, resource, amount)
    if returnValue[0] == 0:
        await ctx.send("Success: " + returnValue[1])
    else:
        await ctx.send("Failure: " + returnValue[1])
@bot.command()
async def checkbalance(ctx, accountNumber: int, password: str):
    returnValue = accountManagement.checkBalance(str(accountNumber), password)
    if returnValue[0] == 0:
        balance = returnValue[1] 
        stringToSend = ""
        stringToSend = stringToSend + "Balance for account: " + str(accountNumber) + "\n"
        for i,x in balance.items():
            stringToSend = stringToSend + str(i) + ": " + str(x) + "\n"
        await ctx.send(stringToSend)
    else:
        await ctx.send("Failure: " + returnValue[1])

#Run the bot
bot.run(config["TOKEN"])
