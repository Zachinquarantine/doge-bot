import discord
import random
from discord.ext import commands
import time
from discord.utils import get
from discord.ext.commands import Bot
import asyncio
import typing
from discord.ext.commands import has_permissions, CheckFailure
from discord.utils import get
import logging
import keep_alive
import inspect
from PIL import Image
import os

client = commands.Bot(command_prefix = "!")
client.remove_command("help")

@client.event
async def on_ready():
  await client.change_presence(status=discord.Status.online, activity=discord.Activity(name="discord doge?! Very wow!", type=discord.ActivityType.listening))
  print('Bot is now online.')

# I initially added a !privacy command here (due to listing requirements for certain bot sites), but have removed it in the Open Source version. If you wish to add it, go to (url) and copy and paste the code from that file to the line directly below this message. Remember to replace Owner#1234 with your Discord Username and Identifier or a website containing the Privacy Policy statement.

# This is where you can add more very Doge images. To do this, just add a new URL between new "", and keep the bracket at the end.
@client.command()
async def doge(ctx):
  doges = ["https://upload.wikimedia.org/wikipedia/en/5/5f/Original_Doge_meme.jpg","https://vignette.wikia.nocookie.net/dogelore/images/9/97/Doge.jpg/revision/latest/top-crop/width/360/height/450?cb=20190205113053","https://i.guim.co.uk/img/static/sys-images/Guardian/Pix/pictures/2013/12/19/1387462292398/c447b512-ea0b-423e-b5f4-7f66b0db44bb-620x372.jpeg?width=700&quality=85&auto=format&fit=max&s=dd1750cb380f94509dee7dddfe43dff5","https://i.guim.co.uk/img/static/sys-images/Guardian/Pix/pictures/2014/1/20/1390229376041/1773f12e-7ddc-4f65-ae31-ef0fbba4f4d4-620x372.png?width=300&quality=85&auto=format&fit=max&s=cadf62d6d550c9765ab914ffb3056b66","https://images.theweek.com/sites/default/files/styles/tw_image_9_4/public/57106_article_full.jpg?itok=GYSA3LBO&resize=450x200","https://moderndogmagazine.com/sites/default/files/styles/slidehsow-banner/public/images/articles/top_images/DogeMeme.jpg?itok=hjcCz0PV", "https://blogs.unimelb.edu.au/sciencecommunication/files/2016/10/my-doge-zzb6qh-300x300.png","https://i.imgflip.com/3mrzmm.jpg"]
  await ctx.send(random.choice(doges))

@commands.cooldown(3, 15, commands.BucketType.user)

@client.event
async def on_command_error(ctx,error):
  if isinstance(error, commands.CommandOnCooldown):
    await ctx.send("**Error: You are on a cooldown for running this command. Please retry after %.2fs.**"% error.retry_after)






keep_alive.keep_alive()
client.run("bot_token_here")