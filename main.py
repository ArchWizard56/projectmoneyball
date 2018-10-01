# Import needed modules
import json
import discord
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
async def add(ctx, a: int, b: int):
    await ctx.send(a+b)

@bot.command()
async def checkbalance(ctx, accountNumber: int):
    stringToSend = ""
    stringToSend = stringToSend + "Balance for account: " + str(accountNumber) + "\n"
    for i,x in balance.items():
        stringToSend = stringToSend + str(i) + ": " + str(x) + "\n"
    await ctx.send(stringToSend)

#Run the bot
bot.run(config["TOKEN"])
