import discord
import os
import sys
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

TOKEN = os.getenv("DISCORD_TOKENS", "")

if not TOKEN:
    logger.error("❌ DISCORD_TOKENS not set!")
    sys.exit(1)

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    logger.info(f"✅ Bot is ONLINE as {client.user}")
    await client.change_presence(status=discord.Status.online)

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if isinstance(message.channel, discord.DMChannel):
        logger.info(f"📨 DM from {message.author}: {message.content}")

try:
    client.run(TOKEN)
except Exception as e:
    logger.error(f"❌ Failed to start: {e}")
    sys.exit(1)
