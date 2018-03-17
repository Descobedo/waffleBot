import discord
from discord.ext.commands import Bot
from discord.ext import commands

Client = discord.Client()


bot_prefix = ""
client = commands.Bot(command_prefix=bot_prefix)

@client.event
async def on_ready():
    print("Waf Ready!")
    #print("Name: {}".fromat(client.user.name))
    #print("ID: {}".format(client.user.id))
@client.command(pass_context=True)
async def _func(ctx):
    await client.say("Teacher Boy\nOwner of pair o' dice\n ")
@client.command(pass_context=True)
async def perritopan(ctx):
    await client.say("Tall Boy\nDave Franco esque\n ")
@client.command(pass_context=True)
async def VirginQuest(ctx):
    await client.say("Teacher Boy\nOwner of pair o' dice\n ")
@client.command(pass_context=True)
async def nereids(ctx):
    await client.say("Soy Boy\nForceful ruler of the discord\n")
@client.command(pass_context=True)
async def FishLove(ctx):
    await client.say("Lil' Boy\nA gamer\n ")
@client.command(pass_context=True)
async def Kevdawg(ctx):
    await client.say("Musical Boy \nbengy\n ")
@client.command(pass_context=True)
async def n98(ctx):
    await client.say("Full Scholarship Boy\n Spy for the government\n ")
@client.command(pass_context=True)
async def Chrutercraft(ctx):
    await client.say("Gnome Boy\n*power drill*\n")
@client.command(pass_context=True)
async def Chapparal(ctx):
    await client.say("Warhammer Boy\nHas a kid/needs a brewski\n ")

client.run("NDI0NDAxNzQ0ODk5MDgwMjAy.DY4a5Q.Azg8XeK5rnm_zBgPc9OsDUlCpKs")
