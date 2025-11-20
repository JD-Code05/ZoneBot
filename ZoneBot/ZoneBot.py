import discord
from discord.ext import commands, tasks
import yt_dlp
import asyncio
import os
import subprocess
from googleapiclient.discovery import build

# import discord - The main library for interacting with Discord
# from discord.ext import commands, tasks - helps create commands and it helps run background loops
# import yt_dlp - The library that does the heavy lifting of downloading videos from YouTube
# import asyncio - A standard Python Library for handling asynchronous operations, (doing multiple things at once)
# import os - Allows Python to talk to your computer's operating system (to handle files, to delete filesm check file sizes, etc)
# import subprocess -  Allows Python to run other progras on your computer (Like FFMPEG) in the command line
# from googleapiclient.discovery import build - Official Google Library to talk to Youtube's API

#For the Configuration
# Values to be filled: Discord Bot Token, Youtube API Key, Youtube Channel ID and Notification Channel ID

# DISCORD_BOT_TOKEN = Discord Bot Token Here
# YOUTUBE_API_KEY = Youtube API Key Here
# YOUTUBE_CHANNEL_ID = Youtube Channel ID Here
# NOTIFICATION_CHANNEL_ID =  #Notificaiton ID Here

# For the Bot Setup
# This part is to define the bot and its intents. The Message Content is needed for reading commands.
intents = discord.Intents.default()
intents.message_content = True 
bot = commands.Bot(command_prefix='!', intents=intents)

# Build the Youtube Service Object: Remove the (#) After This
# if YOUTUBE_API_KEY != Youtube API Key Here:
#  youtube = build('youtube', 'v3', developerKey = YOUTUBE_API_KEY)
# else:
#  youtube = None

#  last_known_video_id = None

@bot.event
async def on_ready():
    print(f' Logged in as {bot.user}')
    if youtube:
        check_for_new_videos.start()
        print(' Bot is ready and tracking YouTube channel.')
    else:
        print(' Bot is ready, but YouTube tracking is OFF (API key not set).')

#For running the Bot
#Important line(Remove Later)
#This is still a temp or WIP 
try:
    bot.run(DISCORD_BOT_TOKEN) except discord.LoginFailure:
        print("Error: Invalid DISCORD_BOT_TOKEN. Please check your token and try again.")
except Exception as e:
print(f"An error occurred: {e}")









