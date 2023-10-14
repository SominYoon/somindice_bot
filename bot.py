import os

import discord
from discord import app_commands as app_
from discord.ext import commands

from random import randint

from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
APP_ID = os.getenv("APP_ID")


intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='.', intents=intents, application_id=APP_ID)

# 함수------------

def dice(a: int = 1, s: int = 6, f: bool = False):
    rlist :list = []
    a = abs(a)
    if (not f):
        for i in range(a):
            rlist.append(randint(1, s))
    else:
        for i in range(a):
            rlist.append(randint(-1, 1))
    
    return {"sum":sum(rlist), "list":rlist}

# ------------
@bot.event
async def on_ready():
    print(f'[ {bot.user} : Online ]')
    try:
        synced = await bot.tree.sync()
        print(f"Synced {len(synced)} commands.")
    except Exception as e:
        print(e)

@bot.tree.command(name="roll", description="일반 주사위 굴림")
async def roll(interaction: discord.Interaction, amount:app_.Range[int,1,200], side:app_.Range[int,1,1000], repeat:app_.Range[int,1,20]= 1, highlight:bool= True):
    r_str:str = ""
    sum_str:str = ""

    if highlight:
        for i in range(repeat):
            roll = dice(a= amount, s=side) 
            for i,n in enumerate(roll["list"]):
                if side = 100:
                    if n==1:
                        roll["list"][i] = f'__`[0{n}]`__'
                    elif n==side:
                        roll["list"][i] = f'**__`[00]`__**'
                    elif n>10:
                        roll["list"][i] = f'`[0{n}]`'
                    else:
                        roll["list"][i] = f'`[{n}]`'


                else:
                    if n==1:
                        roll["list"][i] = f'__`[{n}]`__'
                    elif n==side:
                        roll["list"][i] = f'**__`[{n}]`__**'
                    else:
                        roll["list"][i] = f'`[{n}]`'

            sum_str += f"\n`{str(roll['sum'])}`"
            r_str += "\n"+' '.join(str(i) for i in roll["list"])

            if repeat > 1:
                r_str += ","
    else: 
        for i in range(repeat):
            roll = dice(a= amount, s=side) 
            for i,n in enumerate(roll["list"]):                    
                roll["list"][i] = f'`[{n}]`'

            sum_str += f"\n`{str(roll['sum'])}`"
            r_str += "\n"+' '.join(str(i) for i in roll["list"])

            if repeat > 1:
                r_str += ","

    d_box=discord.Embed(title=f"***{side}**-sided **DICE***", color=0xa51d2d)
    d_box.add_field(name="SUM", value=sum_str)
    d_box.add_field(name=f'Amount : [{amount}]', value=r_str)
    d_box.set_footer(text="somindice.bot")

    await interaction.response.send_message(embed=d_box, ephemeral=False)
@bot.tree.command(name="fudge", description="퍼지 주사위 굴림")
async def fudge(interaction: discord.Interaction, amount:app_.Range[int,1,200], repeat:app_.Range[int,1,20]= 1, sum_highlight:app_.Range[int,-10,+10]= 0):
    r_str:str = ""
    sum_str:str = ""
    for i in range(repeat):
        roll = dice(a= amount, f=True) 
        for i,n in enumerate(roll["list"]):
            if n==0:
                roll["list"][i] = '[ ]'
            if n==1:
                roll["list"][i] = '[+]'
            if n==-1:
                roll["list"][i] = '[-]'
        
        if sum_highlight == roll["sum"]:
            sum_str += f"\n**__`{str(roll['sum'])}`__**"
        else:
            sum_str += f"\n`{str(roll['sum'])}`"
        r_str += "\n`"+' '.join(str(i) for i in roll["list"])+"`"

        if repeat > 1:
            r_str += ","

    d_box=discord.Embed(title="***FUDGE DICE***", color=0xa51d2d)
    d_box.add_field(name="SUM", value=sum_str)
    d_box.add_field(name=f'Amount : [{amount}]', value=r_str)
    d_box.set_footer(text="somindice.bot")

    await interaction.response.send_message(embed=d_box, ephemeral=False)


bot.run(TOKEN)
