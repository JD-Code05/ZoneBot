import discord
from discord.ext import commands, tasks
import yt_dlp
import asyncio
import os
from googleapiclient.discovery import build

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

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')
    # check_for_new_videos.start() #Start the background task to check for new videos
    print('Bot is ready and tracking Youtube Channel.')

#For running the Bot
#Important line(Remove Later)
#This is still a temp or WIP 
try:
    bot.run(DISCORD_BOT_TOKEN) except discord.LoginFailure:
        print("Error: Invalid DISCORD_BOT_TOKEN. Please check your token and try again.")
except Exception as e:
print(f"An error occurred: {e}")




