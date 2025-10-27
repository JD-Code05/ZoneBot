import discord
from discord.ext import commands
import yt_dlp
import asyncio
import os
from googleapiclient.discovery import build

#For the Configuration
# Values to be filled: Discord Bot Token, Youtube API Key, Youtube Channel ID and Notification Channel ID

DISCORD_BOT_TOKEN = #Discord Bot Token Here
YOUTUBE_API_KEY = #Youtube API Key Here
YOUTUBE_CHANNEL_ID = #Youtube Channel ID Here
NOTIFICATION_CHANNEL_ID = #Notificaiton 

# For the Bot Setup
# This part is to define the bot and its intents. The Message Content is needed for reading commands.
intents = discord.Intents.default()
intents.message_content = True


