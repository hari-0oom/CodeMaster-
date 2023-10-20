import discord
import os
from mytoken import CToken 
import apilogic
import pandas as pd
import datetime

intents = discord.Intents.default() # permissions that my bot intents to use
intents.message_content = True

client = discord.Client(intents=intents) # creating a bot client using intents we just defined above 

@client.event
async def on_ready():
    print(f'We have logged in as {client.user.name}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith(">>"):
        message.content=message.content[2:]  # dtring slicing helps make a fresh copy
        
        
        if message.content in ("hello", "Hello"):
            await message.channel.send(f'Hello! {message.author}')


        elif message.content in ("help", "Help", "!"):
            with open("help.txt", 'r') as f:
                bothelpreply = f.read()
                embed = discord.Embed(
                    title="HERE IS HOT USE USE ME:",
                    description=bothelpreply,
                    color=discord.Color.from_rgb(191, 255, 0)
                )
            await message.channel.send(embed=embed) ## file name changes the name of the copy of the otiginal file

        elif message.content in ("date", "time", "datetime"):
            current_date_time = datetime.datetime.now()
            await message.channel.send(f'{current_date_time}')
            


        # elif message.content.startwith("rating"):
        #     apilogic.getHandleInfo(message.content[7:])
        #     userdata=pd.read_csv("data.csv")
        #     await message.channel.send(f'Here is the requested data\n\n {userdata}')


        elif message.content.startswith("putDown"):
            apilogic.getHandleInfo(message.content[8:])
            userdata=pd.read_csv("data.csv")
            embed = discord.Embed(
                title="LIST OF USERS : ",
                description=userdata,
                color=discord.Color.from_rgb(191, 255, 222)
            )
            await message.channel.send(embed=embed) ## file name changes the name of the copy of the otiginal file



        elif message.content.startswith('graphUsers_rating_change'):
            apilogic.graphUsersRatingChange(message.content[25:])
            with open("graph_user_rating_change.png", 'rb') as f:
                graph_file = discord.File(f)
            await message.channel.send(file=graph_file)
            if os.path.exists("graph_users_image.png"):
                os.remove("graph_users_image.png")



        elif message.content.startswith('graphUsers_rating'):
            apilogic.graphUsers(message.content[18:])
            with open("graph_users_image.png", 'rb') as f:
                graph_file = discord.File(f)
            await message.channel.send(file=graph_file)
            if os.path.exists("graph_users_image.png"):
                os.remove("graph_users_image.png")
        

        else:
            await message.channel.send(f"{message.author.name}  404 command not found")
           

client.run(CToken)
