import os

import discord
from discord.ext import commands
import yaml

settings = yaml.safe_load(open("config.yml", "r").read())
client = commands.Bot(command_prefix=".", self_bot=True)


        
@client.event
async def on_ready():
    for filename in os.listdir('./cmds'):
        if filename.endswith('.py'):
            await client.load_extension(f'cmds.{filename[:-3]}')
    print(f"Logged in {client.user}")
    
client.run(settings["token"])