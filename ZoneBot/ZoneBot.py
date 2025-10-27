import discord
from discord.ext import commands
import yt_dlp
import asyncio
import os
from googleapiclient.discovery import build

# For the Bot Setup
# This part is to define the bot and its intents. The Message Content is needed for reading commands.
intents = discord.Intents.default()
intents.message_content = True

