#changes discord account status matching the weather
#status has the form "Watching {emoji}" where emoji matches the weather
#weather matches that of Vancouver, BC, Canada


import discord
import dotenv
import os

dotenv.load_dotenv()

TOKEN_AUTH = os.getenv("TOKEN_AUTH")

client = discord.Client()

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Activity(name="cum", type=discord.ActivityType.watching))

client.run(TOKEN_AUTH, bot=False)